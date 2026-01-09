"""
MCP server that hosts the ether0 chemistry reasoning model from Hugging Face.

The server exposes a single MCP tool (`ether0_reasoning`) that accepts a prompt
and returns the model's completion, plus parsed reasoning/answer blocks when the
model uses ether0's XML-style tags (<|think_start|>, <|think_end|>,
<|answer_start|>, <|answer_end|>).
"""
from __future__ import annotations

import os
from typing import Any, Dict, Optional

from fastmcp import FastMCP
from transformers import AutoModelForCausalLM, AutoTokenizer

THINK_START = "<|think_start|>"
THINK_END = "<|think_end|>"
ANSWER_START = "<|answer_start|>"
ANSWER_END = "<|answer_end|>"
DEFAULT_SYSTEM_PROMPT = (
    "You are ether0, a chemistry-focused assistant. Think step by step about "
    "mechanisms, synthesis plans, and safety. Place your reasoning between "
    f"{THINK_START} and {THINK_END}, and the final answer between "
    f"{ANSWER_START} and {ANSWER_END}."
)


def _extract_segments(text: str) -> tuple[Optional[str], Optional[str]]:
    """Pull thought and answer segments from a completion string."""
    thought = None
    answer = None

    if THINK_START in text and THINK_END in text:
        try:
            thought = text.split(THINK_START, 1)[1].split(THINK_END, 1)[0].strip()
        except (IndexError, ValueError):
            thought = None

    if ANSWER_START in text and ANSWER_END in text:
        try:
            answer = text.split(ANSWER_START, 1)[1].split(ANSWER_END, 1)[0].strip()
        except (IndexError, ValueError):
            answer = None

    return thought, answer


class Ether0MCPServer:
    def __init__(self, model_id: str):
        token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")
        # trust_remote_code accommodates custom modeling code if the repo defines it
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_id, trust_remote_code=True, token=token
        )
        # Pad token is occasionally missing on causal models
        if self.tokenizer.pad_token is None and self.tokenizer.eos_token is not None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            torch_dtype="auto",
            trust_remote_code=True,
            token=token,
        )
        # Generation defaults tuned for chemistry reasoning stability
        self.default_max_new_tokens = int(os.getenv("ETHER0_MAX_NEW_TOKENS", "512"))
        self.default_temperature = float(os.getenv("ETHER0_TEMPERATURE", "0.2"))
        self.default_top_p = float(os.getenv("ETHER0_TOP_P", "0.9"))
        self.model_id = model_id

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        max_new_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
    ) -> Dict[str, Any]:
        sys_prompt = system_prompt or DEFAULT_SYSTEM_PROMPT
        messages = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt},
        ]

        template = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self.tokenizer(
            template, return_tensors="pt", padding=True, truncation=False
        )
        # Align tensors with the model device
        inputs = {k: v.to(self.model.device) for k, v in inputs.items()}

        gen_kwargs = {
            "max_new_tokens": max_new_tokens or self.default_max_new_tokens,
            "temperature": temperature
            if temperature is not None
            else self.default_temperature,
            "top_p": top_p if top_p is not None else self.default_top_p,
            "do_sample": (
                temperature if temperature is not None else self.default_temperature
            )
            > 0,
            "pad_token_id": self.tokenizer.eos_token_id,
        }

        output_ids = self.model.generate(**inputs, **gen_kwargs)
        decoded = self.tokenizer.decode(output_ids[0], skip_special_tokens=False)

        # Remove the prompt portion if present
        completion = decoded[len(template) :].strip() if decoded.startswith(template) else decoded
        thought, answer = _extract_segments(completion)
        result_answer = answer or completion.strip()

        return {
            "answer": result_answer,
            "thought": thought,
            "raw_completion": completion,
            "context_info": [
                f"model_id={self.model_id}",
                f"max_new_tokens={gen_kwargs['max_new_tokens']}",
                f"temperature={gen_kwargs['temperature']}",
                f"top_p={gen_kwargs['top_p']}",
                "Parsed ether0 XML tags" if answer else "No answer tags found; returning raw completion",
            ],
        }


server = FastMCP("ether0 MCP Server")
model_id = os.getenv("ETHER0_MODEL_ID", "futurehouse/ether0")
_ether0 = Ether0MCPServer(model_id=model_id)


@server.tool()
def ether0_reasoning(
    prompt: str,
    system_prompt: Optional[str] = None,
    max_new_tokens: Optional[int] = None,
    temperature: Optional[float] = None,
    top_p: Optional[float] = None,
):
    """
    Run the ether0 chemistry model via MCP.

    Args:
        prompt: Natural-language chemistry question or task.
        system_prompt: Optional override for system guidance.
        max_new_tokens: Generation cap (defaults to 512 if unset).
        temperature: Sampling temperature (defaults to 0.2).
        top_p: Nucleus sampling (defaults to 0.9).
    """
    return _ether0.generate(
        prompt=prompt,
        system_prompt=system_prompt,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_p=top_p,
    )


if __name__ == "__main__":
    host = os.getenv("ETHER0_MCP_HOST", "0.0.0.0")
    port = int(os.getenv("ETHER0_MCP_PORT", "8004"))
    print(f"Starting ether0 MCP server on {host}:{port} using model {model_id}")
    server.run(transport="streamable-http", host=host, port=port, stateless_http=True)
