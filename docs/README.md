# Architecture Diagrams

A text representation (Mermaid format) is available natively in the root `.md` files so GitHub can render them automatically without needing image blobs.

If you ever wish to generate a beautiful `.png`/`.jpg` visualization using tools like **ChatGPT**, **Excalidraw**, or **Draw.io**, copy and paste this prompt:

---

### Prompt to Generate an Architecture Diagram:

> "Please create an architecture diagram showing a data integration and querying pipeline for a Proof of Concept (PoC). The flow goes like this:
>
> 1. A **Python Script (AecorSoft Mock)** generates fake transactional SAP data (VBAK, VBAP, KNA1) and exports them as CSV files. Draw an arrow pointing from this to BigQuery.
> 2. **Google BigQuery** acts as our Data Warehouse. It has two layers: 
>    - The first is the **Raw Dataset (`sap_raw`)** where the CSV files land.
>    - The second is the **Semantic Dataset (`cortex_semantic`)** which is created from the raw data using SQL Views (joins and translations). Show an arrow indicating data flowing from Raw to Semantic.
> 3. An upper-level application called **AgentSpace Mock (Python + Gemini API)** sits on top of this.
> 4. The **User** interacts with the AgentSpace by asking business questions in Natural Language (e.g. 'What were the total sales in 2025?'). Show an arrow from the User to AgentSpace.
> 5. **AgentSpace** takes the question, sends it along with the BigQuery Schema to the **Gemini API** returning a SQL query (Text-to-SQL).
> 6. The **AgentSpace** executes this generated SQL strictly against the **Semantic Dataset** in BigQuery, gets the results, and displays the final Answer to the User.
> 
> Keep the design corporate and technological (cloud icons, database cylinders for BigQuery, python logos, Gemini logo, etc.)."
