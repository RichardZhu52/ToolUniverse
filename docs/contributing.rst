Contributing to ToolUniverse
============================

We welcome contributions to ToolUniverse! This guide covers both general contributions and specialized tool contributions.

Quick Start
-----------

1. Fork and clone the repository
2. Set up development environment:

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ./setup_precommit.sh

3. Make your changes and test:

.. code-block:: bash

   pytest
   black src/tooluniverse/
   flake8 src/tooluniverse/

4. Submit a pull request

Development Standards
---------------------

Code Style
~~~~~~~~~~

- Use Black for formatting: ``black src/tooluniverse/``
- Follow PEP 8 guidelines
- Include type hints for all new code
- Write comprehensive docstrings

Testing
~~~~~~~

- Write tests for all new functionality
- Aim for >90% test coverage
- Run tests with: ``pytest --cov=tooluniverse``

Documentation
~~~~~~~~~~~~~

- Document all public APIs
- Include usage examples
- Update guides for new features
- Use Google-style docstrings

Tool Contributions
------------------

Adding New Tools
~~~~~~~~~~~~~~~~

ToolUniverse supports both local and remote tools. Here's how to add a new tool:

Required Steps
^^^^^^^^^^^^^^

Good news! ToolUniverse now uses an **automated discovery system**. You do NOT need to modify ``src/tooluniverse/__init__.py``.

To add a new tool:

1.  Create a new file in ``src/tooluniverse/`` (or any subdirectory except excluded ones).
2.  Use the ``@register_tool`` decorator on your class.

That's it! The tool will be automatically discovered, lazy-loaded, and available via ``tooluniverse.MyTool``.

**Example**:

.. code-block:: python

   from tooluniverse.tool_registry import register_tool
   from tooluniverse.base_tool import BaseTool

   @register_tool("MyNewTool")
   class MyNewTool(BaseTool):
       ...

**Validation Steps**:

.. code-block:: python

   from tooluniverse import MyNewTool  # Should work immediately
   print(MyNewTool)

Local Tool Example
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from tooluniverse.tool_registry import register_tool
   from typing import Dict, Any

   @register_tool('MyTool', config={
       "name": "my_tool",
       "type": "MyTool",
       "description": "Tool description",
       "parameter": {
           "type": "object",
           "properties": {
               "input": {
                   "type": "string",
                   "description": "Input parameter"
               }
           },
           "required": ["input"]
       },
       "examples": [
           {
               "description": "Example usage",
               "arguments": {"input": "example_value"}
           }
       ],
       "tags": ["category", "subcategory"],
       "author": "Your Name <your.email@example.com>",
       "version": "1.0.0",
       "license": "MIT"
   })
   class MyTool:
       """Tool description."""

       def __init__(self, tool_config=None):
           self.tool_config = tool_config or {}

       def run(self, arguments):
           """Execute tool."""
           try:
               input_value = arguments["input"]
               # Your tool logic here
               result = self._process(input_value)
               return {"result": result, "success": True}
           except Exception as e:
               return {"error": str(e), "success": False}

       def _process(self, input_value):
           """Process input."""
           return {"processed": input_value}

Remote Tool Example
^^^^^^^^^^^^^^^^^^^

For remote tools, create an MCP server:

.. code-block:: python

   from fastapi import FastAPI, HTTPException
   from pydantic import BaseModel
   from typing import Dict, Any

   app = FastAPI(title="My Tool MCP Server")

   class ToolRequest(BaseModel):
       input: str
       options: Dict[str, Any] = {}

   class ToolResponse(BaseModel):
       success: bool
       result: Dict[str, Any]
       error: str = None

   @app.post("/process", response_model=ToolResponse)
   async def process_request(request: ToolRequest):
       """Process tool request."""
       try:
           # Your tool logic here
           result = {"processed": request.input}
           return ToolResponse(success=True, result=result)
       except Exception as e:
           return ToolResponse(success=False, result={}, error=str(e))

   if __name__ == "__main__":
       import uvicorn
       uvicorn.run(app, host="0.0.0.0", port=8000)

Then create a client configuration file:

.. code-block:: json

   {
       "tools": [
           {
               "name": "my_remote_tool",
               "type": "MyRemoteTool",
               "description": "Remote tool description",
               "parameter": {
                   "type": "object",
                   "properties": {
                       "input": {
                           "type": "string",
                           "description": "Input parameter"
                       }
                   },
                   "required": ["input"]
               },
               "settings": {
                   "server_url": "http://localhost:8000",
                   "timeout": 30,
                   "retries": 3
               },
               "tags": ["category", "remote"],
               "author": "Your Name <your.email@example.com>",
               "version": "1.0.0",
               "license": "MIT"
           }
       ]
   }

Complete Tool Development Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When adding a new tool, follow this complete workflow to ensure proper integration:

1. **Create your tool file** in ``src/tooluniverse/tools/`` (e.g., ``my_new_tool.py``)
2. **Implement your tool class** following the BaseTool interface
3. **Modify __init__.py** (critical step - see Required __init__.py Modifications above)
4. **Create comprehensive tests** in ``tests/unit/`` or ``tests/integration/``
5. **Add documentation** in ``docs/tools/``
6. **Update tool registry** if using custom registration
7. **Test the complete integration** to ensure your tool is properly exposed

**Step-by-step**:

.. code-block:: bash

   # 1. No need to modify __init__.py!
   # The automated discovery system will find your tool.

   # 2. Just ensure your class uses @register_tool("MyTool")

**Common mistakes to avoid**:
- Forgetting to add the tool to all four locations
- Adding the import in the wrong section (lazy vs non-lazy)
- Incorrect module name in the lazy import proxy
- Missing quotes around the tool name in the __all__ list
- Not testing the import after making changes

Testing Your Tool
~~~~~~~~~~~~~~~~~

Create tests for your tool:

.. code-block:: python

   import pytest
   from tooluniverse.my_tool import MyTool

   class TestMyTool:
       def setup_method(self):
           self.tool = MyTool()

       def test_success(self):
           """Test successful execution."""
           result = self.tool.run({"input": "test_value"})
           assert result["success"] is True
           assert "processed" in result["result"]

       def test_error(self):
           """Test error handling."""
           result = self.tool.run({"input": ""})
           assert result["success"] is False
           assert "error" in result

Documentation
~~~~~~~~~~~~~

Create documentation for your tool:

.. code-block:: rst

   My Tool
   =======

   Tool description and features.

   Usage
   -----

   .. code-block:: python

      from tooluniverse import ToolUniverse

      tu = ToolUniverse()
      tu.load_tools()

      result = tu.run_one_function({
          "name": "my_tool",
          "arguments": {"input": "example_value"}
      })

   Parameters
   ----------

   - **input** (string, required): Input parameter description

Contributing Workflow
---------------------

1. Create a feature branch:

.. code-block:: bash

   git checkout -b feature/my-feature

2. Make your changes and commit:

.. code-block:: bash

   git add .
   git commit -m "feat: add my new tool

   - Implement MyTool class
   - Add comprehensive tests
   - Update documentation"

3. Push and create a pull request:

.. code-block:: bash

   git push origin feature/my-feature

Commit Types
~~~~~~~~~~~~

- ``feat``: New features
- ``fix``: Bug fixes
- ``docs``: Documentation updates
- ``test``: Test additions or modifications
- ``refactor``: Code refactoring
- ``style``: Code style changes
- ``chore``: Build/maintenance tasks

Review Process
--------------

All contributions go through:

1. **Automated Checks**: CI runs tests, linting, and type checking
2. **Manual Review**: Maintainers review code quality and design
3. **Documentation Review**: Ensure docs are clear and complete
4. **Testing**: Verify functionality works as expected

Troubleshooting Tool Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your tool is not being imported correctly, check these common issues:

**ImportError: cannot import name 'MyTool'**
- Verify the class is decorated with ``@register_tool("MyTool")``
- Ensure the file is a ``.py`` file in the ``src/tooluniverse/`` tree
- Ensure the file is NOT in an excluded directory (e.g. ``scripts/``, ``tests/``)

**AttributeError: module 'tooluniverse' has no attribute 'MyTool'**
- Verify the tool name in ``@register_tool`` matches what you are trying to access
- If the file was just added, try reloading the package or restarting the interpreter

**Debugging Discovery**
- You can inspect ``tooluniverse._lazy_registry`` to see what tools were discovered
- Run ``build_lazy_registry()`` manually to force a fresh scan

**Testing your integration**:

.. code-block:: python

   # Test 1: Direct import
   from tooluniverse import MyTool
   print(f"Tool class: {MyTool}")
   
   # Test 2: Check if it's in __all__
   from tooluniverse import __all__
   print(f"MyTool in __all__: {'MyTool' in __all__}")
   
   # Test 3: Instantiate the tool
   tool = MyTool()
   print(f"Tool instance: {tool}")

Getting Help
------------

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Email**: shanghuagao@gmail.com

Types of Contributions
----------------------

Bug Reports
~~~~~~~~~~~

Include:
- Python version and OS
- ToolUniverse version
- Minimal code to reproduce
- Full error traceback
- Expected vs actual behavior

Feature Requests
~~~~~~~~~~~~~~~~

Provide:
- Clear use case description
- Proposed API design
- Implementation suggestions
- Impact on existing code

Documentation Improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~

Help by:
- Fixing typos and grammar
- Adding missing examples
- Clarifying confusing sections
- Translating to other languages

Thank you for contributing to ToolUniverse! 🧬🔬