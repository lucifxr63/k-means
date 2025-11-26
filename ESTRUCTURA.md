# 📁 Estructura del Proyecto K-Means

## Organización por Carpetas

```
k-means/
│
├── 📄 README.md                    # Documentación principal del proyecto
├── 📋 requirements.txt             # Dependencias de Python
├── 🔒 .gitignore                   # Archivos ignorados por Git
├── 📐 ESTRUCTURA.md               # Este archivo
│
├── 📚 docs/                        # DOCUMENTACIÓN
│   ├── README.md                   # Índice de documentación
│   ├── DISEÑO_FLUJO.md            # Flujo de trabajo detallado
│   ├── GUIA_RAPIDA.md             # Guía de inicio rápido
│   └── REPORTE_PRUEBAS.md         # Reporte de validación
│
├── 💻 scripts/                     # CÓDIGO FUENTE
│   ├── README.md                   # Guía de scripts
│   ├── analisis_kmeans_congestion.ipynb  ⭐ Notebook principal
│   ├── analisis_kmeans.py         # Script Python completo
│   └── test_rapido.py             # Script de prueba rápida
│
├── 📊 data/                        # DATOS
│   ├── README.md                   # Descripción del dataset
│   └── congestion-1.csv           # Dataset principal (76,140 × 70)
│
└── 📈 resultados/                  # RESULTADOS GENERADOS
    ├── README.md                   # Descripción de resultados
    ├── .gitkeep                    # Mantiene carpeta en Git
    │
    ├── 📊 Archivos CSV:
    │   ├── resultados_kmeans.csv   # Dataset con clusters asignados
    │   ├── centroides_clusters.csv # Centroides de cada cluster
    │   └── test_resultados.csv     # Resultados de prueba rápida
    │
    └── 🎨 Gráficos PNG:
        ├── grafico_elbow.png       # Método del Codo
        ├── grafico_silhouette.png  # Análisis de Silhouette
        ├── boxplots_clusters.png   # Boxplots por cluster
        ├── mapa_geografico.png     # Distribución geográfica
        └── heatmap_clusters.png    # Heatmap de características
```

---

## 🎯 Propósito de cada Carpeta

### 📚 `docs/`
Contiene toda la documentación del proyecto:
- Flujo de trabajo metodológico
- Guías de uso y ejecución
- Reportes de pruebas y validación

**Ideal para:** Entender el proyecto, aprender la metodología, solucionar problemas

---

### 💻 `scripts/`
Todo el código ejecutable del análisis:
- Notebook interactivo para presentaciones
- Scripts automatizados para análisis completo
- Script de prueba rápida para validación

**Ideal para:** Ejecutar el análisis, modificar código, experimentar

---

### 📊 `data/`
Dataset original y documentación de datos:
- CSV con datos de congestión vehicular
- Descripción de variables y características

**Ideal para:** Acceder a los datos, entender las variables

---

### 📈 `resultados/`
Todos los archivos generados por el análisis:
- CSVs con clusters y centroides
- Gráficos de visualización
- Resultados de pruebas

**Ideal para:** Revisar resultados, presentar gráficos, análisis post-procesamiento

---

## 🚀 Comandos de Ejecución

### Desde la raíz del proyecto:

**Prueba rápida:**
```bash
python scripts/test_rapido.py
```

**Análisis completo (Script):**
```bash
python scripts/analisis_kmeans.py
```

**Análisis completo (Notebook):**
```bash
jupyter notebook scripts/analisis_kmeans_congestion.ipynb
```

---

## 📝 Notas Importantes

1. **Rutas relativas:** Todos los scripts usan rutas relativas (`../data/`, `../resultados/`)
2. **Ejecución desde raíz:** Los comandos deben ejecutarse desde la carpeta raíz del proyecto
3. **Git ignore:** Los archivos en `resultados/` están en `.gitignore` (no se suben al repo)
4. **READMEs:** Cada carpeta tiene su propio README con documentación específica

---

## 🔄 Flujo de Trabajo

```
1. Leer documentación → docs/
2. Instalar dependencias → requirements.txt
3. Revisar datos → data/
4. Ejecutar análisis → scripts/
5. Revisar resultados → resultados/
6. Presentar/Reportar → usar notebooks y gráficos
```

---

## 📦 Archivos en Raíz

| Archivo | Propósito |
|---------|-----------|
| `README.md` | Documentación principal, punto de entrada |
| `requirements.txt` | Dependencias de Python para instalar |
| `.gitignore` | Configuración de Git (excluir archivos pesados) |
| `ESTRUCTURA.md` | Este archivo (guía de organización) |

---

## ✅ Ventajas de esta Estructura

✅ **Organizada:** Fácil encontrar archivos por tipo
✅ **Profesional:** Estructura estándar de proyectos de ciencia de datos
✅ **Escalable:** Fácil agregar nuevos scripts o documentos
✅ **Documentada:** Cada carpeta tiene su README
✅ **Git-friendly:** Archivos pesados en `.gitignore`
✅ **Mantenible:** Separación clara de responsabilidades

---

**Fecha de reorganización:** 26 de noviembre de 2025
**Estructura:** Estándar de ciencia de datos
