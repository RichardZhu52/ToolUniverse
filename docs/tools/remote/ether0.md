````markdown
# ether0 Chemistry Reasoning MCP Tool

A lightweight MCP server that wraps the open-source **ether0** chemistry model (weights on Hugging Face at `futurehouse/ether0`) so ToolUniverse can call it remotely for synthesis/analysis reasoning. The server loads the model with `transformers` and exposes a single MCP tool that accepts a prompt and returns thought+answer XML segments when present.

## What this gives you
- Remote MCP endpoint you can host anywhere (GPU recommended) to run ether0.
- MCP auto-loader entry (`mcp_auto_loader_ether0`) so ToolUniverse can register the tool by URL.
- JSON return with parsed `thought`, `answer`, and the raw completion for downstream use.

## Prerequisites
- Python 3.10+
- `pip install "torch>=2.2" transformers>=4.37 accelerate fastmcp`
- GPU is strongly recommended; CPU works but is slow.
- Optional: `HF_TOKEN` (or `HUGGINGFACEHUB_API_TOKEN`) if the model requires authentication.

## Quickstart: run the MCP server
```bash
# 1) Create an isolated env
uv venv ether0-mcp --python 3.10
source ether0-mcp/bin/activate

# 2) Install dependencies
uv pip install "torch>=2.2" transformers>=4.37 accelerate fastmcp

# 3) (Optional) set a private HF token
export HF_TOKEN="<your_hf_token>"

# 4) Start the server (defaults: model futurehouse/ether0, host 0.0.0.0, port 8004)
python src/tooluniverse/remote/ether0/ether0_mcp_server.py
```
You will see logs that the model is loading, then the MCP server binding to `0.0.0.0:8004` with `streamable-http` transport.

### Server configuration knobs
Set these before launching if you need overrides:
- `ETHER0_MODEL_ID`: Hugging Face model id (default `futurehouse/ether0`).
- `ETHER0_MCP_HOST`: Bind address (default `0.0.0.0`).
- `ETHER0_MCP_PORT`: Bind port (default `8004`).
- `HF_TOKEN` / `HUGGINGFACEHUB_API_TOKEN`: auth token if the model is gated.

## Wire ToolUniverse to the server (client side)
On the machine running ToolUniverse, set the MCP host (include port if not 8004) and load the auto-loader tool:
```bash
export ETHER0_MCP_SERVER_HOST="your-hostname:8004"
```
Then in Python:
```python
from tooluniverse import ToolUniverse

u = ToolUniverse()
u.load_tools(["mcp_auto_loader_ether0"])
response = u.run_tool(
    "ether0_reasoning",
    {
        "prompt": "Suggest a stable synthetic route to aspirin.",
        "max_new_tokens": 256,
        "temperature": 0.2,
    },
)
print(response)
```
`mcp_auto_loader_ether0` connects to `http://${ETHER0_MCP_SERVER_HOST}/mcp` and registers the `ether0_reasoning` MCP tool.

## Tool contract
**Name:** `ether0_reasoning`

**Parameters:**
- `prompt` (string, required): Natural-language chemistry question or task.
- `system_prompt` (string, optional): Override default system instructions for ether0.
- `max_new_tokens` (integer, default 512): Generation cap.
- `temperature` (number, default 0.2): Sampling temperature.
- `top_p` (number, default 0.9): Nucleus sampling.

**Return payload:**
- `answer` (string): Parsed `<|answer_start|>...<|answer_end|>` content when present; falls back to the raw completion.
- `thought` (string | null): Parsed `<|think_start|>...<|think_end|>` if produced.
- `raw_completion` (string): Full decoded generation (sans the prompt prefix).
- `context_info` (array[str]): Model id, sampling settings, and parse notes.

## Troubleshooting
- **Model download/auth:** set `HF_TOKEN` if downloads fail or the repo is gated.
- **GPU memory errors:** lower `max_new_tokens` or move to a larger GPU; CPU mode works but is slow.
- **Empty `answer`:** ether0 may not emit XML tags for some prompts; use `raw_completion` and adjust your prompt/system prompt to request structured output.
````
