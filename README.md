# Análisis K-Means - Congestión Vehicular Santiago

## 📌 Descripción
Análisis de clustering K-Means aplicado a datos de congestión vehicular en Santiago de Chile. Este proyecto identifica patrones de congestión utilizando técnicas de aprendizaje no supervisado.

## 📁 Estructura del Proyecto

```
k-means/
├── 📚 docs/                    # Documentación
│   ├── DISEÑO_FLUJO.md        # Flujo de trabajo detallado
│   ├── GUIA_RAPIDA.md         # Guía de ejecución
│   └── REPORTE_PRUEBAS.md     # Reporte de pruebas
│
├── 💻 scripts/                 # Código ejecutable
│   ├── analisis_kmeans_congestion.ipynb  ⭐ Notebook principal
│   ├── analisis_kmeans.py     # Script completo
│   └── test_rapido.py         # Script de prueba rápida
│
├── 📊 data/                    # Datos
│   └── congestion-1.csv       # Dataset (76,140 × 70)
│
├── 📈 resultados/              # Resultados generados
│   ├── *.csv                  # Resultados del clustering
│   └── *.png                  # Gráficos y visualizaciones
│
├── 📄 README.md               # Este archivo
└── 📋 requirements.txt        # Dependencias
```

## 🚀 Inicio Rápido

### 1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

### 2. Prueba rápida (recomendado primero):
```bash
python scripts/test_rapido.py
```

### 3. Análisis completo:

**Opción A - Notebook** ⭐ (Recomendado para presentación):
```bash
jupyter notebook scripts/analisis_kmeans_congestion.ipynb
```

**Opción B - Script Python:**
```bash
python scripts/analisis_kmeans.py
```

---

📊 **Dataset:** 76,140 filas × 70 columnas  
⏱️ **Tiempo de ejecución completo:** ~5-10 minutos  
🧪 **Tiempo de prueba rápida:** ~30 segundos

## 🎯 Objetivos Cumplidos

✅ **Preparar datos** - Escalado con StandardScaler  
✅ **Identificar K óptimo** - Métodos: Elbow, Silhouette, Gap Statistic  
✅ **Implementar K-Means** - Con número óptimo de clusters  
✅ **Visualizar resultados** - Boxplots, mapas, heatmaps  

## 📊 Metodología

1. **Exploración de datos** - Análisis inicial del dataset
2. **Preprocesamiento** - Limpieza y escalado de variables
3. **Selección de K** - Tres métodos de validación
4. **Clustering** - Aplicación de K-Means
5. **Interpretación** - Análisis de patrones identificados

## 📈 Resultados

El análisis identifica diferentes patrones de congestión basados en:
- Duración de la congestión
- Velocidad promedio
- Longitud del tramo
- Ubicación geográfica
- Horarios (hora pico)

## 👥 Información Académica

**Curso:** Minería de Datos  
**Tema:** Clustering - K-Means  
**Fecha:** Noviembre 2024
actividad mineria
