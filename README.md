# 💻 Propuesta de Proyecto de Web Scraping - LP2 💻
![Logo UNALM](https://cdn2.lamolina.edu.pe/lamolina-comunica1/websites/4/imagenes%20de%20escudo/1703855732083.jpeg)

# Tema del Proyecto: 

## Análisis Comparativo de la Evolución de Precios de la Canasta Básica Familiar en Lima

## I. Importancia y Relevancia 
**¿Porqué es importante el cambio de precios de la canasta básica?**  
En un contexto de incertidumbre económica, los ciudadanos perciben que los precios en góndola suben a un ritmo diferente al de los reportes oficiales. En Lima, por ejemplo, son cerca de **400 ítems considerados y de todo tipo: Alimentación, Salud, Educación, Transporte entre otros, simulan un patrón de consumo y determinan esta canasta** **(Lozano I., 2020)**. Para ello, es vital contar con herramientas independientes que monitoreen la variación de costos de alimentos en tiempo real y su relación con factores como el tipo de cambio.

**¿Cuánto gasta el peruano promedio en alimentos?**  
La Canasta Básica Familiar (CBF) en Lima es costosa; para una familia de cuatro miembros, supera los **S/ 1,700** a S/ **2,200** mensuales para necesidades básicas y alimentos, según cifras recientes (2025), mostrando una brecha grande con los ingresos mínimos y afectando gravemente a hogares de bajos ingresos, que destinan gran parte de su presupuesto a comida y ven cómo su poder adquisitivo disminuye por la inflación, dificultando el acceso a una dieta nutritiva. **(INEI, 2025)**
Según, Paola del Carpio, economista de redes para el desarrollo, mencionó para Latina: "El gasto mensual de un hogar peruano en alimentos es, en promedio, **891 soles**, es decir, los hogares de menores ingresos destinan más del **50% de su ingreso a la compra de alimentos**". **(Espinoza A., 2025)** Este alto porcentaje limita la capacidad de los hogares para cubrir otras necesidades esenciales como vivienda, transporte, educación y salud.

**¿En qué consiste el proyecto?**  
Este proyecto va a consistir en un sistema automatizado  que extrae semanalmente los precios de **productos esenciales (arroz, aceite, leche)** de supermercados online y los contrasta con datos oficiales del Banco Central de Reserva (BCRP) e INEI, para determinar la inflación real que enfrenta el consumidor frente a los indicadores macroeconómicos.
Este proyecto entregará un dataset estructurado y transparente que permitirá visualizar la **"micro-inflación"** semanal. Aportará valor académico al permitir contrastar la velocidad de
ajuste de precios de los supermercados privados frente a la data oficial del Estado.



## III. 🏁 Objetivos del Proyecto

### 3.1. Objetivo General
Implementar un sistema automatizado en **Python** que integre la extracción de precios minoristas online con indicadores económicos oficiales del BCRP, consolidando una base de datos estructurada que permita el análisis estadístico comparativo de la canasta básica familiar.

### 3.2. Objetivos Específicos

1.  **Automatización de la Captura de Datos (Web Scraping):**
    Desarrollar scripts de extracción utilizando la librería `BeautifulSoup` para recolectar periódicamente precios y descripciones de productos seleccionados de supermercados locales, transformando información web no estructurada (HTML) en datos tabulares procesables.
    > *"El scraping permite transformar la web en una base de datos estructurada"* (Mitchell, 2018).

2.  **Integración de Fuentes Oficiales (API):**
    Establecer una conexión de consulta automática a la API del **Banco Central de Reserva del Perú (BCRP)** para obtener el Tipo de Cambio diario, garantizando que el análisis de precios cuente con un contexto macroeconómico oficial y actualizado sin intervención manual.

3.  **Consolidación y Limpieza de Datos (Data Cleaning):**
    Estructurar un dataset final unificado (formato `.csv`) que combine los precios extraídos (Scraping), el tipo de cambio (API) y el histórico del IPC (INEI), aplicando técnicas de limpieza para asegurar la consistencia numérica y temporal necesaria para su análisis estadístico.

4.  **Gestión Colaborativa del Desarrollo:**
    Utilizar **Git y GitHub** para la administración del código fuente, asegurando la integración del trabajo de todos los integrantes y la documentación del proceso de desarrollo, cumpliendo con los estándares de trabajo colaborativo exigidos por el curso.

---

### 📚 Referencias Bibliográficas
* **Banco Central de Reserva del Perú. (2025).** *API de Series Estadísticas*. Recuperado de: [https://estadisticas.bcrp.gob.pe](https://estadisticas.bcrp.gob.pe)
* **Espinoza, A. (16 de julio del 2025).** ¿Cuánto gasta el peruano promedio en alimentos?: Impacto de los bloqueos en la canasta básica. *Infobae*.[https://www.infobae.com/peru/2025/07/10/cuanto-gasta-el-peruano-promedio-en-alimentos-impacto-los-bloqueos-en-la-canasta-basica/]
* **INEI. (2025).** *INDICE DE PRECIOS AL CONSUMIDOR DE LIMA METROPOLITANA*. Recuperado de: [https://proyectos.inei.gob.pe/web/biblioineipub/bancopub/Est/Lib0135/cap0102.htm]
*  **Lozano, I. (4 de febrero del 2020)**. Canasta familiar: ¿Qué es y por qué es importante su actualización?. *El Comercio*. [https://elcomercio.pe/economia/peru/inei-canasta-familiar-que-es-y-por-que-es-importante-su-actualizacion-noticia/]
* **Mitchell, R. (2018).** *Web Scraping with Python: Collecting More Data from the Modern Web*. O'Reilly Media.
* **VanderPlas, J. (2016).** *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.

## Integrantes del Grupo:
**1.** ***López Ruiz Jhordy Fabrizio - GitHub: [JhorLop134]***

**2.** ***Montero Balcazar Maria Megumi - GitHub: [Megumi-cpu]***

**3.** ***[Nombre Compañero] - GitHub: [Su Usuario]***
