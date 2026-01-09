Space Configuration System
==============================

Space is a powerful configuration system that allows you to easily load, share, and manage tool configurations for ToolUniverse. It supports both simple presets and complex workspaces with AI integration.

Quick Start
-----------

Load a Space configuration in just one line:

.. code-block:: python

   from tooluniverse import ToolUniverse
   
   tu = ToolUniverse()
   
   # Load from local file
   config = tu.load_space("./my-config.yaml")
   
   # Or load from GitHub
   config = tu.load_space(
       "https://raw.githubusercontent.com/mims-harvard/ToolUniverse/main/examples/spaces/protein-research.yaml"
   )

Command Line Usage
------------------

Use Space configurations with MCP servers:

.. code-block:: bash

   # Load local file
   tooluniverse-smcp-stdio --load "./my-config.yaml"
   
   # Load from GitHub
   tooluniverse-smcp-stdio --load "https://raw.githubusercontent.com/mims-harvard/ToolUniverse/main/examples/spaces/protein-research.yaml"

What is Space?
------------------

Space is a unified system for managing tool configurations that supports:

- **Presets**: Simple tool collections for specific domains
- **Workspaces**: Complete environments with tools, AI config, and workflows
- **Sharing**: Easy sharing via HuggingFace Hub, HTTP URLs, or local files

Available Space Configurations
-------------------------------

ToolUniverse provides pre-configured Space configurations for various research domains. All Spaces are available on GitHub and can be loaded directly via HTTP URLs.

Domain-Specific Spaces
~~~~~~~~~~~~~~~~~~~~~~

**Protein Research** (`protein-research.yaml`)
   Comprehensive tools for protein structure, function, and interaction research.
   Includes: UniProt, RCSB PDB, AlphaFold, HPA, InterPro, protein visualization
   `GitHub <https://github.com/mims-harvard/ToolUniverse/blob/main/examples/spaces/protein-research.yaml>`_

**Genomics** (`genomics.yaml`)
   Tools for genomics and genetics research.
   Includes: GWAS, Ensembl, ClinVar, dbSNP, gnomAD, GTEx, ENCODE, GDC
   `GitHub <https://github.com/mims-harvard/ToolUniverse/blob/main/examples/spaces/genomics.yaml>`_

**Bioinformatics** (`bioinformatics.yaml`)
   Bioinformatics analysis and pathway research tools.
   Includes: BLAST, Gene Ontology, KEGG, Reactome, Enrichr, HumanBase, WikiPathways
   `GitHub <https://github.com/mims-harvard/ToolUniverse/blob/main/examples/spaces/bioinformatics.yaml>`_

**Structural Biology** (`structural-biology.yaml`)
   Protein and molecular structure analysis tools.
   Includes: RCSB PDB, AlphaFold, EMDB, 3D visualization
   `GitHub <https://github.com/mims-harvard/ToolUniverse/blob/main/examples/spaces/structural-biology.yaml>`_

**Cheminformatics** (`cheminformatics.yaml`)
   Chemical compound research and ADMET prediction tools.
   Includes: PubChem, ChEMBL, ADMET AI, molecular visualization
   `GitHub <https://github.com/mims-harvard/ToolUniverse/blob/main/examples/spaces/cheminformatics.yaml>`_

**Disease Research** (`disease-research.yaml`)
   Disease research and target-disease association tools.
   Includes: OpenTargets, Monarch, disease target scoring, GWAS, HPA
   `GitHub <https://github.com/mims-harvard/ToolUniverse/blob/main/examples/spaces/disease-research.yaml>`_

**Drug Discovery** (`drug-discovery.yaml`)
   Essential tools for drug discovery research.
   Includes: ChEMBL, Clinical Trials, OpenTargets, FDA, PubChem, DrugBank, ADMET AI
   `GitHub <https://github.com/mims-harvard/ToolUniverse/blob/main/examples/spaces/drug-discovery.yaml>`_

**Literature Search** (`literature-search.yaml`)
   Scientific literature search and analysis tools.
   Includes: EuropePMC, Semantic Scholar, PubTator, arXiv, Crossref, PubMed
   `GitHub <https://github.com/mims-harvard/ToolUniverse/blob/main/examples/spaces/literature-search.yaml>`_

**Clinical Research** (`clinical-research.yaml`)
   Clinical research and regulatory affairs tools.
   Includes: Clinical Trials, FDA, Clinical Guidelines, Monarch, EFO, HPA
   `GitHub <https://github.com/mims-harvard/ToolUniverse/blob/main/examples/spaces/clinical-research.yaml>`_

Comprehensive Workspace
~~~~~~~~~~~~~~~~~~~~~~~

**Full Workspace** (`full-workspace.yaml`)
   Complete research environment with all major domains (449 tools from 32 categories).
   Includes: LLM configuration, hooks, comprehensive tool coverage
   `GitHub <https://github.com/mims-harvard/ToolUniverse/blob/main/examples/spaces/full-workspace.yaml>`_

Loading Pre-configured Spaces
-----------------------------

All Space configurations can be loaded directly from GitHub or local files:

.. code-block:: python

   from tooluniverse import ToolUniverse
   
   tu = ToolUniverse()
   
   # Load from GitHub raw URL
   config = tu.load_space(
       "https://raw.githubusercontent.com/mims-harvard/ToolUniverse/main/examples/spaces/protein-research.yaml"
   )
   
   # Or download and load from local file
   config = tu.load_space("./examples/spaces/protein-research.yaml")
   
   # Use the loaded tools
   print(f"Loaded {len(tu.all_tools)} tools from {config.get('name')}")

For more details and configuration options, see `examples/spaces/README.md <https://github.com/mims-harvard/ToolUniverse/blob/main/examples/spaces/README.md>`_.

Creating Your Own Space
------------------------

You can create custom Space configurations by creating a YAML file:

.. code-block:: yaml

   name: "My Research Toolkit"
   version: "1.0.0"
   description: "Tools for my research"
   
   tools:
     include_tools:
       - "UniProt_get_entry_by_accession"
       - "gwas_search_associations"
       - "PubChem_get_CID_by_compound_name"

Then load it:

.. code-block:: python

   tu = ToolUniverse()
   config = tu.load_space("./my-research-toolkit.yaml")

For more examples and detailed configuration options, see `examples/spaces/README.md <https://github.com/mims-harvard/ToolUniverse/blob/main/examples/spaces/README.md>`_.

Configuration File Structure
-----------------------------

Here's a complete example with all available fields explained:

.. code-block:: yaml

   # Required fields
   name: "My Research Workspace"        # Space name (required)
   version: "1.0.0"                     # Version number (required)
   
   # Optional metadata
   description: "Complete research environment"  # Description of this Space
   tags: ["research", "custom"]         # Keywords for categorization
   
   # Tool configuration - choose one or combine methods
   tools:
     # Method 1: Explicit tool list (recommended for clarity)
     include_tools:
       - "UniProt_get_entry_by_accession"
       - "gwas_search_associations"
       - "PubChem_get_CID_by_compound_name"
     
     # Method 2: Load by categories (convenience method)
     # categories:
     #   - "uniprot"
     #   - "gwas"
     #   - "pubchem"
     
     # Method 3: Include by tool type
     # include_tool_types:
     #   - "OpenTarget"
     #   - "UniProtRESTTool"
     
     # Exclusions (works with any method above)
     exclude_tools:                      # Exclude specific tools
       - "old_tool_name"
     # exclude_tool_types:               # Exclude by tool type
     #   - "Unknown"
   
   # LLM configuration (optional, only needed for workspaces with AI agents)
   llm_config:
     mode: "default"                    # "default", "fallback", or "env_override"
     default_provider: "CHATGPT"        # CHATGPT, GEMINI, OPENROUTER, or VLLM
     models:
       default: "gpt-4o"                # Model used by AgenticTools
     temperature: 0.3                   # 0.0-2.0 range
   
   # For vLLM, also set: export VLLM_SERVER_URL="http://your-server:8000"
   # See :doc:`vllm_support` for complete vLLM setup guide
   
   # Hooks for output processing (optional)
   hooks:
     - type: "SummarizationHook"        # Summarize long outputs
       enabled: true
       config:
         max_length: 500
         include_key_points: true
     
     - type: "FileSaveHook"             # Save outputs to files
       enabled: true
       config:
         output_dir: "./outputs"
         file_prefix: "analysis"
   
   # Environment variables documentation (optional, for reference only)
   required_env:
     - "AZURE_OPENAI_API_KEY"
     - "AZURE_OPENAI_ENDPOINT"

Creating Your Own Space
------------------------

1. Create a YAML file with the structure above
2. Choose your tools using ``include_tools`` (recommended) or ``categories``
3. Add LLM config and hooks if needed
4. Validate: ``python -c "from tooluniverse.space import validate_yaml_file_with_schema; print('✅ Valid' if validate_yaml_file_with_schema('my-space.yaml')[0] else '❌ Invalid')"``
5. Load: ``tu.load_space("./my-space.yaml")``

See `examples/spaces/ <https://github.com/mims-harvard/ToolUniverse/tree/main/examples/spaces>`_ for more examples.
