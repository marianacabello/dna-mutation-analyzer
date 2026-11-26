
# Analizador de Mutaciones de ADN

## 1. Descripción del proyecto

El Analizador de Mutaciones de ADN es un proyecto desarrollado como parte de la Maestría en Bioinformática.

El objetivo es desarrollar una herramienta en Python que compare secuencias de ADN con una secuencia de referencia e identifique diferencias entre ellas.

El primer gen seleccionado para el proyecto piloto es BRCA1.

## 2. Funcionalidades actuales

- Cargar secuencias de referencia desde archivos FASTA.
- Calcular la longitud de una secuencia de ADN.
- Contabilizar los nucleótidos A, T, C, G y N.
- Comparar dos secuencias de igual longitud.
- Detectar sustituciones entre secuencias previamente alineadas.
- Exportar las diferencias detectadas a un archivo CSV.

## 3. Estructura del proyecto

```text
dna-mutation-analyzer/
├── data/
│   └── BRCA1.fasta
├── scripts/
│   └── variant_analyzer.py
├── results/
│   └── brca1_results.csv
├── docs/
├── README.md
├── .gitignore
└── LICENSE
```

## 4. Requisitos

- Python 3.
- No se requieren bibliotecas externas adicionales para la versión actual.

## 5. Instrucciones de ejecución

Desde la carpeta principal del proyecto, ejecutar el siguiente comando en la terminal:

```bash
python3 scripts/variant_analyzer.py
```

El programa solicitará una secuencia de ADN y la comparará con un fragmento de la referencia BRCA1.

## 6. Limitaciones actuales

- La comparación requiere secuencias de igual longitud.
- Actualmente, solo se detectan sustituciones.
- El programa no realiza alineamiento de secuencias.
- Las posiciones reportadas son relativas al archivo de referencia y todavía no están validadas como coordenadas genómicas.
- El programa no identifica ni clasifica variantes clínicas documentadas.
- Las sustituciones utilizadas en las pruebas son artificiales y no representan hallazgos clínicos.

## 7. Mejoras futuras

- Fortalecer la validación de las secuencias y el manejo de errores.
- Incorporar alineamiento de secuencias.
- Detectar inserciones y deleciones.
- Establecer coordenadas genómicas y orientación de referencia correctas.
- Investigar la integración de bases de datos confiables de variantes, como ClinVar.
- Implementar pruebas automatizadas.
- Mejorar la presentación y documentación de los resultados.

## 8. Trabajo colaborativo

El proyecto se desarrolla en equipo y contempla la distribución de actividades entre programación, investigación biológica, validación de resultados y documentación.
