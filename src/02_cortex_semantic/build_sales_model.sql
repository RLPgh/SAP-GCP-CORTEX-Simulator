-- ====================================================================
-- Simulador SAP GCP Cortex - Fase 3: Capa Semántica (Business Models)
-- ====================================================================

-- Nota: Reemplaza `tu_proyecto` con el ID real de tu proyecto en GCP.
-- CREATE SCHEMA IF NOT EXISTS `tu_proyecto.cortex_semantic`;

-- Vista de Negocio: Consolidado de Ventas (Traduciendo SAP a un Modelo Analítico)
CREATE OR REPLACE VIEW `tu_proyecto.cortex_semantic.vw_ventas_consolidadas` AS
SELECT
    -- =======================================
    -- Información de Cabecera (Order Header)
    -- =======================================
    vbak.VBELN AS SalesDocument,
    -- Transformamos la fecha formato YYYYMMDD string a objeto DATE
    CAST(PARSE_DATE('%Y%m%d', vbak.ERDAT) AS DATE) AS CreationDate,
    
    -- =======================================
    -- Información del Cliente (Customer Info)
    -- =======================================
    vbak.KUNNR AS CustomerNumber,
    kna1.NAME1 AS CustomerName,
    kna1.LAND1 AS CountryCode,
    kna1.ORT01 AS City,
    kna1.REGIO AS Region,
    
    -- =======================================
    -- Información de la Posición (Item Info)
    -- =======================================
    vbap.POSNR AS ItemNumber,
    vbap.MATNR AS MaterialNumber,
    vbap.ARKTX AS MaterialDescription,
    
    -- =======================================
    -- Métricas (Measures)
    -- =======================================
    vbap.KWMENG AS OrderQuantity,
    vbap.NETPR AS NetPrice,
    -- Calculamos el valor total de la línea
    (vbap.KWMENG * vbap.NETPR) AS TotalItemValue,
    vbap.WAERK AS Currency

FROM
    `tu_proyecto.sap_raw.vbak` AS vbak
INNER JOIN
    `tu_proyecto.sap_raw.vbap` AS vbap
    ON vbak.VBELN = vbap.VBELN
LEFT JOIN
    `tu_proyecto.sap_raw.kna1` AS kna1
    ON vbak.KUNNR = kna1.KUNNR;
