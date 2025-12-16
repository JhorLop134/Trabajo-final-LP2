# 📝 Propuesta de Proyecto de Web Scraping
## I. 💡 Tema del Proyecto
### I.1. Título del Proyecto:
***"Info-Canasta: Análisis Comparativo de la Evolución de Precios de la Canasta Básica Familiar en Lima"***
### I.2. Descripción:
El proyecto consiste en un sistema automatizado que extrae semanalmente los precios de productos esenciales (arroz, aceite, leche) de supermercados online y los contrasta con datos oficiales del Banco Central de Reserva (BCRP) e INEI, para determinar la inflación real que enfrenta el consumidor frente a los indicadores macroeconómicos.
## II. 🎯 Justificación, Relevancia y Aporte
### II.1. Importancia:
En un contexto de incertidumbre económica, los ciudadanos perciben que los precios en góndola suben a un ritmo diferente al de los reportes oficiales. Es vital contar con herramientas independientes que monitoreen la variación de costos de alimentos en tiempo real y su relación con factores como el tipo de cambio.
### II.2. Valor del aporte:
Este proyecto entregará un dataset estructurado y transparente que permitirá visualizar la **"micro-inflación"** semanal. Aportará valor académico al permitir contrastar la velocidad de ajuste de precios de los supermercados privados frente a la data oficial del Estado.
## III. 🌐 Fuentes de Datos a Extraer
### 1. Fuente de Web Scraping (El Mercado Real):
- **Sitios Web:** PlazaVea.com.pe (o Tottus).
- **Justificación:** Estructura HTML ordenada que facilita la extracción recurrente.
- **Datos a Extraer:** Nombre del Producto, Precio Actual, Precio Oferta, Marca, Categoría (Abarrotes).
- **Estrategia:** Se monitoreará una "Canasta Piloto" fija de 10 productos clave (ej. "Arroz Costeño 5kg", "Aceite Primor 1L") para garantizar la consistencia histórica.
### 2. Fuente API (El Dato Oficial - Gobierno Peruano):
- **API:** Servicio de Datos del BCRP (Banco Central de Reserva del Perú)
- **URL Base:** https://estadisticas.bcrp.gob.pe/estadisticas/series/api/
- **Justificación:** Fuente oficial del Estado Peruano, de acceso abierto y gratuito, que garantiza la veracidad académica de los datos sin barreras de pago o bloqueos de red.
- **Datos a Extraer:**
  - **Tipo de Cambio Interbancario (Serie: PD04637PD):** Para analizar la correlación entre el dólar y los precios de importados.
  - **Expectativas Macroeconómicas:** Para contrastar con la realidad del mercado.
### 3. Fuente CSV / Dataset (La Línea Base):
- **Fuente:** INEI (Instituto Nacional de Estadística e Informática) - Plataforma de Datos Abiertos.
- **Datos a Extraer:** Series históricas mensuales del Índice de Precios al Consumidor (IPC) de Lima Metropolitana (Archivo .csv).
- **Uso:** Servirá como "grupo de control" para comparar si nuestra medición de supermercado está por encima o por debajo de la inflación oficial.
## IV. 🏁 Objetivos
### A. Objetivo General
Implementar un flujo de extracción de datos (Pipeline ETL) colaborativo que recolecte, limpie y almacene precios de alimentos y variables económicas oficiales para generar un indicador independiente de variación de costos.
### B. Objetivos Específicos
**1.** Desarrollar un scraper en Python (usando BeautifulSoup y Requests) capaz de navegar
por las categorías de alimentos básicos y extraer precios de forma ética (respetando
robots.txt).

**2.** Implementar la conexión automatizada a la API del BCRP para enriquecer cada registro
de precios con el contexto económico del día.

**3.** Diseñar procesos de limpieza de datos para estandarizar formatos (soles, fechas) y
unificar las tres fuentes en una base de datos coherente.

**4.** Publicar el código fuente documentado en GitHub y generar un reporte de análisis con
los hallazgos.

## V. 🖼️ Producto Final
**1. Repositorio GitHub:** Código fuente completo con historial de commits de todos los
integrantes, incluyendo scripts de extracción (scraper.py) y limpieza.

**2. Base de Datos Unificada (.csv):** Archivo maestro con la estructura: Fecha, Producto,
Precio_Supermercado, Tipo_Cambio_BCRP, IPC_Oficial.

**3. Informe Técnico:** Documento detallando el diseño de la extracción, la lógica de
programación utilizada y un análisis gráfico de la correlación entre el Dólar (BCRP) y la
Canasta (Supermercado).

## Integrantes del Grupo:
**1.** ***López Ruiz Jhordy Fabrizio - GitHub: JhorLop134***

**2.** ***[Nombre Compañero] - GitHub: [Su Usuario]***

**3.** ***[Nombre Compañero] - GitHub: [Su Usuario]***
