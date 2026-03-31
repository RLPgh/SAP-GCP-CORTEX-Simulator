import os
import re
from google.cloud import bigquery
from llm_connection import configure_gemini

# Configuración del esquema para el Prompt del LLM
TARGET_PROJECT_ID = os.getenv("GCP_PROJECT_ID", "tu_proyecto")
DATASET = "cortex_semantic"
TABLE = "vw_ventas_consolidadas"

# Le pasamos a Gemini el DDL Semántico para que sepa exactamente qué columnas existen
SCHEMA_CONTEXT = f"""
Table: {TARGET_PROJECT_ID}.{DATASET}.{TABLE}
Columns:
- SalesDocument (STRING) - El número de documento de venta / orden.
- CreationDate (DATE) - La fecha en la que se creó la orden.
- CustomerNumber (STRING) - El código de identificación del cliente.
- CustomerName (STRING) - El nombre del cliente.
- CountryCode (STRING) - País del cliente.
- City (STRING) - Ciudad del cliente.
- Region (STRING) - Región / Estado del cliente.
- ItemNumber (STRING) - El número de ítem/posición dentro de la orden.
- MaterialNumber (STRING) - El código del material comprado.
- MaterialDescription (STRING) - La descripción del material.
- OrderQuantity (INT64) - La cantidad comprada de ese material.
- NetPrice (FLOAT64) - El precio unitario.
- TotalItemValue (FLOAT64) - El precio total (Quantity * NetPrice).
- Currency (STRING) - Moneda de la transacción.
"""

def generate_sql(prompt, model):
    """Convierte la pregunta en natural a código SQL usando Gemini."""
    full_prompt = f"""
    You are an expert Google BigQuery Data Engineer. 
    Given the following Semantic Table Schema representing SAP Sales data:
    
    {SCHEMA_CONTEXT}
    
    Write a valid Google BigQuery SQL query to answer the user's question.
    Use ONLY the columns provided. Do not use markdown blocks like ```sql ... ```. 
    Return ONLY the raw SQL query text, without explanations.

    Question: {prompt}
    """
    response = model.generate_content(full_prompt)
    sql = response.text.strip()
    
    # Limpieza en caso de que el modelo retorne formato Markdown
    sql = re.sub(r'```sql', '', sql, flags=re.IGNORECASE)
    sql = re.sub(r'```', '', sql)
    
    return sql.strip()

def execute_query(sql_query):
    """Ejecuta la consulta en BigQuery."""
    try:
        # Esto requiere que la variable GOOGLE_APPLICATION_CREDENTIALS 
        # o clI autenticación de GCP esté configurada.
        client = bigquery.Client() 
        print(f"\n[Ejecutando SQL en BigQuery...]\n{sql_query}\n")
        
        query_job = client.query(sql_query)
        results = query_job.result()
        
        print("--- Resultados ---")
        rows = list(results)
        if not rows:
            print("No se encontraron resultados.")
        else:
            for row in rows:
                print(dict(row))
    except Exception as e:
        print(f"Error ejecutando la consulta en GCP: {e}")
        print("Asegúrate de haber configurado tu Default GCP Credentials \n(ej: `gcloud auth application-default login`) o la variable `GCP_PROJECT_ID`.")

def main():
    """Bucle principal de la consola del Agente (AgentSpace Mock)"""
    print("=========================================================")
    print("🤖 Iniciando AgentSpace Mock (Text-to-SQL con Gemini API)")
    print("=========================================================\n")
    
    try:
        model = configure_gemini()
    except Exception as e:
        print(f"Error de Configuración LLM: {e}")
        return
        
    print("Escribe 'salir' o 'exit' para terminar.\n")
    
    while True:
        question = input("Haz una pregunta de negocio (Ej: 'Cuáles fueron las ventas totales en 2025?'):\n> ")
        if question.lower().strip() in ['exit', 'salir', 'quit']:
            break
            
        if not question.strip():
            continue
            
        print("\n⏳ AgentSpace está pensando...")
        sql_query = generate_sql(question, model)
        execute_query(sql_query)
        print("-" * 60)

if __name__ == "__main__":
    main()
