# Project Internal Instructions (Agents)

This repository serves as a simulated environment mimicking the flow of AecorSoft -> SAP Raw in BigQuery -> Cortex Semantic -> AgentSpace/Gemini. 

Guidelines when generating or modifying code for this project:

1. **Flexibility**: The `src/01_extraction_mock` MUST be generic enough to allow scaling other tables besides just `vbak`, `vbap`, and `kna1`. Use schemas/configuration dicts to drive table generation if possible.
2. **SQL Best Practices**: The `src/02_cortex_semantic` files should closely map to real SAP Cortex examples with descriptive aliases (e.g. `VBELN AS SalesDocument`).
3. **Simplicity over Overengineering**: The text-to-SQL system in `src/03_agentspace_mock` is a PoC. Keep prompt handling robust but straightforward without relying on excessive abstractions. 
4. **Secrets Management**: DO NOT commit API keys, GCP credentials, or environments. They must be mapped in the `.gitignore`. Use `python-dotenv` natively across Python files.

**Prompting Gemini (Text-to-SQL)**:
- Explicitly inject the Cortex Semantic View DDL natively into the context of Gemini for robust Text-to-SQL behavior.
- Use `google-cloud-bigquery` library implicitly trusted by default credentials.
