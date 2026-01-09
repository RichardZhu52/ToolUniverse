RCSB Search Tools
=================

**Configuration File**: ``rcsb_search_tools.json``
**Tool Type**: Local
**Tools Count**: 1

This page contains all tools defined in the ``rcsb_search_tools.json`` configuration file.

Available Tools
---------------

**PDB_search_similar_structures** (Type: RCSBSearchTool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search for protein structures similar to a given PDB ID or sequence using RCSB PDB structure similarity search. Supports both sequence-based and structure-based similarity search. Suitable for antibodies, proteins, and other biologics.

.. dropdown:: PDB_search_similar_structures tool specification

   **Tool Information:**

   * **Name**: ``PDB_search_similar_structures``
   * **Type**: ``RCSBSearchTool``
   * **Description**: Search for protein structures similar to a given PDB ID or sequence using RCSB PDB structure similarity search. Supports sequence-based, structure-based, and text-based search. Suitable for antibodies, proteins, and other biologics. Use text search to find PDB IDs by drug name, protein name, or keywords.

   **Parameters:**

   * ``query`` (string) (required)
     PDB ID (e.g., '1ABC'), protein sequence (amino acids), or search text (e.g., drug name, protein name, keyword). For structure search, provide PDB ID. For sequence search, provide amino acid sequence. For text search, provide drug name, protein name, or keyword.

   * ``search_type`` (string) (optional, default: "sequence")
     Type of search: 'sequence' for sequence-based similarity search, 'structure' for structure-based similarity search using PDB ID, 'text' for text-based search by name or keyword

   * ``similarity_threshold`` (number) (optional, default: 0.7)
     Similarity threshold (0-1). Higher values return more similar structures. For sequence search, this is the identity cutoff. For structure search, this is the structure similarity threshold. Not used for text search.

   * ``max_results`` (integer) (optional, default: 20)
     Maximum number of results to return (1-100).

   **Example Usage:**

   Sequence-based search:

   .. code-block:: python

      from tooluniverse import ToolUniverse
      
      tu = ToolUniverse()
      tu.load_tools()
      
      query = {
          "name": "PDB_search_similar_structures",
          "arguments": {
              "query": "MKLLILTCLVAVALARPKHPIKHQGLPQEVLNENLLRFFVAPFPEVFGKEKVNEL",
              "search_type": "sequence",
              "similarity_threshold": 0.7,
              "max_results": 20
          }
      }
      result = tu.run(query)

   Structure-based search:

   .. code-block:: python

      query = {
          "name": "PDB_search_similar_structures",
          "arguments": {
              "query": "1ABC",
              "search_type": "structure",
              "similarity_threshold": 0.7,
              "max_results": 20
          }
      }
      result = tu.run(query)

   Text-based search (find PDB IDs by name or keyword):

   .. code-block:: python

      query = {
          "name": "PDB_search_similar_structures",
          "arguments": {
              "query": "Donanemab",
              "search_type": "text",
              "max_results": 20
          }
      }
      result = tu.run(query)
      
      # If results found, use the PDB ID for structure similarity search
      if result.get("results"):
          pdb_id = result["results"][0]["pdb_id"]
          similar_query = {
              "name": "PDB_search_similar_structures",
              "arguments": {
                  "query": pdb_id,
                  "search_type": "structure",
                  "similarity_threshold": 0.7,
                  "max_results": 20
              }
          }
          similar_result = tu.run(similar_query)

   **Use Cases:**

   * Finding PDB IDs by drug name, protein name, or keyword (text search)
   * Finding similar protein structures for antibodies and biologics
   * Searching for structures with similar sequences
   * Identifying related protein structures in PDB database
   * Completing the workflow: drug name → PDB ID → similar structures
   * Complementing small molecule search tools (e.g., ChEMBL_search_similar_molecules)

   **Notes:**

   * This tool is designed for biologics (proteins, antibodies, etc.) that cannot be searched using SMILES-based tools
   * For small molecules, use ``ChEMBL_search_similar_molecules`` or ``PubChem_search_compounds_by_similarity``
   * Text search allows finding PDB IDs from drug names, protein names, or keywords without knowing the PDB ID in advance
   * Sequence searches require valid amino acid sequences (at least 10 residues)
   * Structure searches require valid 4-character PDB IDs
   * Text search does not use similarity_threshold parameter

Navigation
----------

* :doc:`tools_config_index` - Back to Tools Overview
* :doc:`../guide/loading_tools` - Loading Local Tools
* :doc:`chembl_tools` - ChEMBL Tools (for small molecules)