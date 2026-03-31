# SAP GCP Cortex Simulator

_A Proof of Concept (PoC) that simulates the extraction flow of transactional data (SAP S/4HANA), its semantic modeling in Google BigQuery inspired by the Cortex Framework, and its consumption via a Conversational Agent using the Gemini API._

[Leer en Español](README.es.md)

## Executive Summary
This project is a simulation of an enterprise data integration flow. It uses Python to mock third-party ingestion tools (like AecorSoft) for data extraction, BigQuery to mock the Cortex foundational semantic layer, and the Gemini API to mock a conversational AI interface (like AgentSpace).

Since we do not have reference to the real raw data, the project is designed to be highly modular and flexible, accommodating any data structure variations if needed in the future.

## Project Architecture

![Architecture Diagram](docs/architecture_diagram.png)

1. **Extraction Mock:** Synthetic data generation mocking "SAP".
2. **Cortex Semantic Layer:** Raw storage & transformation into Business Models on BigQuery.
3. **AgentSpace Mock:** Text-to-SQL Conversational Agent.

## Tech Stack
* **Python:** For data extraction simulation and orchestrating the conversational agent.
* **Google BigQuery:** Data Warehouse for both the Raw and Semantic layers.
* **SQL:** To define business logic (Data foundations).
* **Gemini API:** Foundational Language Model (LLM) for processing natural language.

## How it works
* **Phase 1:** Synthetic generation of `vbak`, `vbap`, and `kna1` tables in Python, exporting them as CSVs (`src/01_extraction_mock/generate_sap_data.py`).
* **Phase 2:** Loading and transformation in BigQuery via SQL DDLs to create enterprise business views (`src/02_cortex_semantic`).
* **Phase 3:** Dynamic natural language querying using a console agent (`src/03_agentspace_mock`).

## How to run

1. **Clone repository and install dependencies:**
   ```bash
   git clone <REPOSITORY_URL>
   cd sap-gcp-cortex-simulator
   pip install -r requirements.txt
   ```
2. **Generate Fake Data:**
   ```bash
   python src/01_extraction_mock/generate_sap_data.py
   ```
   *This outputs CSV files into `data_mock/`.*

3. **Load data to BigQuery:**
   * Create a free personal Google Cloud Project.
   * Execute the scripts in `src/02_cortex_semantic/`.
   
4. **Run the Conversational Agent:**
   * Provide a `.env` file with `GEMINI_API_KEY=your_key` and GCP credentials.
   ```bash
   python src/03_agentspace_mock/data_agent.py
   ```
