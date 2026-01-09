# ether0 MCP Server

This directory contains a minimal MCP server that wraps the [futurehouse/ether0](https://huggingface.co/futurehouse/ether0) chemistry model so ToolUniverse clients can call it over HTTP.

## Run locally
```bash
uv venv ether0-mcp --python 3.10
source ether0-mcp/bin/activate
uv pip install "torch>=2.2" transformers>=4.37 accelerate fastmcp

# Optional if the model is gated
export HF_TOKEN="<your_hf_token>"

# Bind host/port and launch
export ETHER0_MCP_HOST=0.0.0.0
export ETHER0_MCP_PORT=8004
python ether0_mcp_server.py
```
The server exposes the `ether0_reasoning` MCP tool at `http://$ETHER0_MCP_HOST:$ETHER0_MCP_PORT/mcp`.

## Client wiring in ToolUniverse
Set the host (include port) on the client machine and load the auto-loader tool:
```bash
export ETHER0_MCP_SERVER_HOST="your-host:8004"
```
```python
from tooluniverse import ToolUniverse

u = ToolUniverse()
u.load_tools(["mcp_auto_loader_ether0"])
result = u.run_tool(
    "ether0_reasoning",
    {"prompt": "Propose a robust aspirin synthesis."},
)
print(result)
```
