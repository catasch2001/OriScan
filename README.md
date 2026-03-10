# OriScan

**OriScan** es una herramienta de bioinformática diseñada para la localización precisa de orígenes de replicación (*OriC*) en genomas bacterianos. Utiliza algoritmos de optimización de strings y análisis de desbalance de nucleótidos (GC-Skew).

---

## Propuesta de Valor
El análisis de genomas masivos requiere herramientas eficientes. OriScan implementa:
* **Análisis de Skew de C-G:** Identificación de las hebras líder y rezagada mediante el cálculo de asimetría de bases.
* **Detección de Patrones con Errores:** Algoritmos basados en la Distancia de Hamming para encontrar mensajes ocultos (DnaA boxes) con tolerancia a mutaciones.
* **Arquitectura Escalable:** Diseñado para integrarse en pipelines de Nextflow y entornos Docker.

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/catasch2001/OriScan.git](https://github.com/catasch2001/OriScan.git)
   cd OriScan