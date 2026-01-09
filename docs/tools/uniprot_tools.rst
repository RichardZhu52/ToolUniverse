Uniprot Tools
=============

**Configuration File**: ``uniprot_tools.json``
**Tool Type**: Local
**Tools Count**: 10

This page contains all tools defined in the ``uniprot_tools.json`` configuration file.

Available Tools
---------------

**UniProt_get_alternative_names_by_accession** (Type: UniProtRESTTool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract all alternative names (alternativeNames) from UniProtKB entry.

.. dropdown:: UniProt_get_alternative_names_by_accession tool specification

   **Tool Information:**

   * **Name**: ``UniProt_get_alternative_names_by_accession``
   * **Type**: ``UniProtRESTTool``
   * **Description**: Extract all alternative names (alternativeNames) from UniProtKB entry.

   **Parameters:**

   * ``accession`` (string) (required)
     UniProtKB accession, e.g., P05067.

   **Example Usage:**

   .. code-block:: python

      query = {
          "name": "UniProt_get_alternative_names_by_accession",
          "arguments": {
              "accession": "example_value"
          }
      }
      result = tu.run(query)


**UniProt_get_disease_variants_by_accession** (Type: UniProtRESTTool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract all variants (feature type = VARIANT) and their related annotations from UniProtKB entry.

.. dropdown:: UniProt_get_disease_variants_by_accession tool specification

   **Tool Information:**

   * **Name**: ``UniProt_get_disease_variants_by_accession``
   * **Type**: ``UniProtRESTTool``
   * **Description**: Extract all variants (feature type = VARIANT) and their related annotations from UniProtKB entry.

   **Parameters:**

   * ``accession`` (string) (required)
     UniProtKB accession, e.g., P05067.

   **Example Usage:**

   .. code-block:: python

      query = {
          "name": "UniProt_get_disease_variants_by_accession",
          "arguments": {
              "accession": "example_value"
          }
      }
      result = tu.run(query)


**UniProt_get_entry_by_accession** (Type: UniProtRESTTool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the complete JSON entry for a specified UniProtKB accession.

.. warning::

   This tool returns the complete UniProtKB entry, which can be extremely large
   (40,000+ lines for some entries like P00698) and may cause LLM context limits
   to be exceeded or crashes. For most use cases, consider using more specific
   extraction tools instead:
   ``UniProt_get_function_by_accession``, ``UniProt_get_sequence_by_accession``,
   ``UniProt_get_recommended_name_by_accession``, ``UniProt_get_organism_by_accession``,
   ``UniProt_get_subcellular_location_by_accession``, ``UniProt_get_disease_variants_by_accession``,
   or ``UniProt_get_ptm_processing_by_accession``.

.. dropdown:: UniProt_get_entry_by_accession tool specification

   **Tool Information:**

   * **Name**: ``UniProt_get_entry_by_accession``
   * **Type**: ``UniProtRESTTool``
   * **Description**: Get the complete JSON entry for a specified UniProtKB accession. WARNING: Returns complete UniProtKB entry which can be extremely large (40,000+ lines) and may exceed LLM context limits. Consider using specific extraction tools instead for most use cases.

   **Parameters:**

   * ``accession`` (string) (required)
     UniProtKB entry accession, e.g., P05067.

   **Example Usage:**

   .. code-block:: python

      query = {
          "name": "UniProt_get_entry_by_accession",
          "arguments": {
              "accession": "example_value"
          }
      }
      result = tu.run(query)


**UniProt_get_function_by_accession** (Type: UniProtRESTTool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract functional annotations from UniProtKB entry (Comment type = FUNCTION).

.. dropdown:: UniProt_get_function_by_accession tool specification

   **Tool Information:**

   * **Name**: ``UniProt_get_function_by_accession``
   * **Type**: ``UniProtRESTTool``
   * **Description**: Extract functional annotations from UniProtKB entry (Comment type = FUNCTION).

   **Parameters:**

   * ``accession`` (string) (required)
     UniProtKB accession, e.g., P05067.

   **Example Usage:**

   .. code-block:: python

      query = {
          "name": "UniProt_get_function_by_accession",
          "arguments": {
              "accession": "example_value"
          }
      }
      result = tu.run(query)


**UniProt_get_isoform_ids_by_accession** (Type: UniProtRESTTool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract all splice isoform IDs from UniProtKB entry (isoformNames).

.. dropdown:: UniProt_get_isoform_ids_by_accession tool specification

   **Tool Information:**

   * **Name**: ``UniProt_get_isoform_ids_by_accession``
   * **Type**: ``UniProtRESTTool``
   * **Description**: Extract all splice isoform IDs from UniProtKB entry (isoformNames).

   **Parameters:**

   * ``accession`` (string) (required)
     UniProtKB accession, e.g., P05067.

   **Example Usage:**

   .. code-block:: python

      query = {
          "name": "UniProt_get_isoform_ids_by_accession",
          "arguments": {
              "accession": "example_value"
          }
      }
      result = tu.run(query)


**UniProt_get_organism_by_accession** (Type: UniProtRESTTool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract the organism scientific name from UniProtKB entry.

.. dropdown:: UniProt_get_organism_by_accession tool specification

   **Tool Information:**

   * **Name**: ``UniProt_get_organism_by_accession``
   * **Type**: ``UniProtRESTTool``
   * **Description**: Extract the organism scientific name from UniProtKB entry.

   **Parameters:**

   * ``accession`` (string) (required)
     UniProtKB accession, e.g., P05067.

   **Example Usage:**

   .. code-block:: python

      query = {
          "name": "UniProt_get_organism_by_accession",
          "arguments": {
              "accession": "example_value"
          }
      }
      result = tu.run(query)


**UniProt_get_ptm_processing_by_accession** (Type: UniProtRESTTool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract all PTM and processing sites from UniProtKB entry (feature type = MODIFIED RESIDUE or SIG...

.. dropdown:: UniProt_get_ptm_processing_by_accession tool specification

   **Tool Information:**

   * **Name**: ``UniProt_get_ptm_processing_by_accession``
   * **Type**: ``UniProtRESTTool``
   * **Description**: Extract all PTM and processing sites from UniProtKB entry (feature type = MODIFIED RESIDUE or SIGNAL, etc.).

   **Parameters:**

   * ``accession`` (string) (required)
     UniProtKB accession, e.g., P05067.

   **Example Usage:**

   .. code-block:: python

      query = {
          "name": "UniProt_get_ptm_processing_by_accession",
          "arguments": {
              "accession": "example_value"
          }
      }
      result = tu.run(query)


**UniProt_get_recommended_name_by_accession** (Type: UniProtRESTTool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract the recommended protein name (recommendedName) from UniProtKB entry.

.. dropdown:: UniProt_get_recommended_name_by_accession tool specification

   **Tool Information:**

   * **Name**: ``UniProt_get_recommended_name_by_accession``
   * **Type**: ``UniProtRESTTool``
   * **Description**: Extract the recommended protein name (recommendedName) from UniProtKB entry.

   **Parameters:**

   * ``accession`` (string) (required)
     UniProtKB accession, e.g., P05067.

   **Example Usage:**

   .. code-block:: python

      query = {
          "name": "UniProt_get_recommended_name_by_accession",
          "arguments": {
              "accession": "example_value"
          }
      }
      result = tu.run(query)


**UniProt_get_sequence_by_accession** (Type: UniProtRESTTool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract the canonical sequence from UniProtKB entry.

.. dropdown:: UniProt_get_sequence_by_accession tool specification

   **Tool Information:**

   * **Name**: ``UniProt_get_sequence_by_accession``
   * **Type**: ``UniProtRESTTool``
   * **Description**: Extract the canonical sequence from UniProtKB entry.

   **Parameters:**

   * ``accession`` (string) (required)
     UniProtKB accession, e.g., P05067.

   **Example Usage:**

   .. code-block:: python

      query = {
          "name": "UniProt_get_sequence_by_accession",
          "arguments": {
              "accession": "example_value"
          }
      }
      result = tu.run(query)


**UniProt_get_subcellular_location_by_accession** (Type: UniProtRESTTool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract subcellular localization annotations from UniProtKB entry (Comment type = SUBCELLULAR LOC...

.. dropdown:: UniProt_get_subcellular_location_by_accession tool specification

   **Tool Information:**

   * **Name**: ``UniProt_get_subcellular_location_by_accession``
   * **Type**: ``UniProtRESTTool``
   * **Description**: Extract subcellular localization annotations from UniProtKB entry (Comment type = SUBCELLULAR LOCATION).

   **Parameters:**

   * ``accession`` (string) (required)
     UniProtKB accession, e.g., P05067.

   **Example Usage:**

   .. code-block:: python

      query = {
          "name": "UniProt_get_subcellular_location_by_accession",
          "arguments": {
              "accession": "example_value"
          }
      }
      result = tu.run(query)


Navigation
----------

* :doc:`tools_config_index` - Back to Tools Overview
* :doc:`../guide/loading_tools` - Loading Local Tools
