-- ====================================================================
-- Simulador SAP GCP Cortex - Fase 3: Capa Cruda (Raw)
-- ====================================================================

-- Nota: Reemplaza `tu_proyecto` con el ID real de tu proyecto en GCP.
-- CREATE SCHEMA IF NOT EXISTS `tu_proyecto.sap_raw`;

-- 1. Maestro de Clientes (KNA1)
CREATE OR REPLACE TABLE `tu_proyecto.sap_raw.kna1` (
    KUNNR STRING,
    NAME1 STRING,
    LAND1 STRING,
    ORT01 STRING,
    REGIO STRING
);

-- 2. Cabecera de Documentos de Venta (VBAK)
CREATE OR REPLACE TABLE `tu_proyecto.sap_raw.vbak` (
    VBELN STRING,
    ERDAT STRING,
    ERZET STRING,
    KUNNR STRING,
    NETWR FLOAT64,
    WAERK STRING
);

-- 3. Posiciones de Documentos de Venta (VBAP)
CREATE OR REPLACE TABLE `tu_proyecto.sap_raw.vbap` (
    VBELN STRING,
    POSNR STRING,
    MATNR STRING,
    ARKTX STRING,
    KWMENG INT64,
    NETPR FLOAT64,
    WAERK STRING
);

-- Una vez creadas estas tablas, puedes usar la interfaz de BigQuery o el comando `bq load` 
-- para inyectar los CSVs generados en la carpeta `data_mock/` hacia estas tablas.
