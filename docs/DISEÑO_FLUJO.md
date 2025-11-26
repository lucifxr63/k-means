# Diseño del Flujo de Trabajo - Análisis K-Means

## 📋 Objetivo General
Aplicar el algoritmo K-Means para identificar patrones de congestión vehicular en Santiago utilizando el dataset `Congestion_Santiago.csv`.

---

## 🔄 Flujo de Trabajo

### **FASE 1: Carga y Exploración de Datos**

```
├── 1.1 Importar librerías necesarias
│   ├── pandas, numpy (manipulación de datos)
│   ├── sklearn (clustering y preprocessing)
│   └── matplotlib, seaborn (visualización)
│
├── 1.2 Cargar dataset
│   └── congestion-1.csv (70 columnas, múltiples registros)
│
└── 1.3 Exploración inicial
    ├── Verificar dimensiones del dataset
    ├── Identificar valores nulos
    ├── Analizar tipos de datos
    └── Estadísticas descriptivas
```

**Salida:** Comprensión de la estructura y calidad de los datos

---

### **FASE 2: Preparación de Datos**

```
├── 2.1 Selección de variables
│   ├── Filtrar variables numéricas
│   ├── Excluir variables categóricas no codificadas
│   └── Mantener variables one-hot encoded
│
├── 2.2 Limpieza de datos
│   ├── Eliminar filas con valores nulos
│   └── Verificar consistencia de datos
│
└── 2.3 Escalado de variables ⭐
    ├── Aplicar StandardScaler
    ├── Media = 0, Desviación = 1
    └── Normalizar todas las variables numéricas
```

**Salida:** Dataset limpio y escalado listo para clustering

---

### **FASE 3: Determinación del Número Óptimo de Clusters**

```
├── 3.1 Método del Codo (Elbow Method) 📊
│   ├── Probar K = 2 a 10
│   ├── Calcular inercia (WCSS) para cada K
│   ├── Graficar Inercia vs K
│   └── Identificar el "codo" en la curva
│
├── 3.2 Método Silhouette 📊
│   ├── Calcular Silhouette Score para K = 2 a 10
│   ├── Graficar Score vs K
│   └── Seleccionar K con mayor score (cercano a 1)
│
└── 3.3 Método Gap Statistic 📊
    ├── Comparar dispersión real vs datos random
    ├── Calcular Gap para cada K
    ├── Graficar Gap vs K
    └── Seleccionar K donde Gap es máximo
```

**Salida:** Número óptimo de clusters (K) determinado por consenso de métodos

---

### **FASE 4: Implementación de K-Means**

```
├── 4.1 Entrenar modelo final
│   ├── Configurar KMeans con K óptimo
│   ├── random_state=42 (reproducibilidad)
│   ├── n_init=20 (múltiples inicializaciones)
│   └── Ajustar modelo a datos escalados
│
├── 4.2 Asignar clusters
│   ├── Predecir cluster para cada observación
│   └── Agregar columna 'Cluster' al dataset original
│
└── 4.3 Evaluar modelo
    ├── Calcular Silhouette Score final
    ├── Obtener inercia final
    └── Analizar distribución de observaciones por cluster
```

**Salida:** Modelo K-Means entrenado con asignaciones de cluster

---

### **FASE 5: Visualización e Interpretación**

```
├── 5.1 Boxplots de variables clave 📊
│   ├── Duration_hrs por cluster
│   ├── Length_km por cluster
│   ├── Speed_km/h por cluster
│   └── Peak_Time por cluster
│
├── 5.2 Estadísticas descriptivas por cluster
│   ├── Media, mediana, desviación estándar
│   └── Comparación entre clusters
│
├── 5.3 Visualización geográfica 🗺️
│   ├── Scatter plot Latitud vs Longitud
│   └── Coloreado por cluster
│
├── 5.4 Heatmap de características 🔥
│   ├── Valores promedio por cluster
│   └── Identificación de patrones
│
└── 5.5 Análisis de Silhouette detallado
    ├── Gráfico de silhouette por cluster
    └── Evaluación de cohesión interna
```

**Salida:** Gráficos y métricas para interpretar los clusters

---

### **FASE 6: Interpretación y Documentación**

```
├── 6.1 Perfil de cada cluster
│   ├── Características distintivas
│   ├── Tamaño del cluster
│   ├── Variables más relevantes
│   └── Interpretación del negocio
│
├── 6.2 Exportar resultados
│   ├── resultados_kmeans.csv (datos + clusters)
│   └── centroides_clusters.csv
│
└── 6.3 Conclusiones
    ├── Patrones identificados
    ├── Insights sobre congestión
    └── Recomendaciones
```

**Salida:** Informe completo con interpretación de resultados

---

## 📊 Diagrama de Flujo Visual

```
┌─────────────────────┐
│  Cargar Datos CSV   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Explorar y Limpiar  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Escalar Variables   │ ⭐ CRÍTICO
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Determinar K       │
│  ├─ Elbow           │
│  ├─ Silhouette      │
│  └─ Gap Statistic   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Aplicar K-Means     │
│ con K óptimo        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Visualizar          │
│ ├─ Boxplots         │
│ ├─ Mapas            │
│ ├─ Heatmaps         │
│ └─ Silhouette       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Interpretar y       │
│ Documentar          │
└─────────────────────┘
```

---

## 🎯 Puntos Clave del Análisis

### ✅ Requisitos Cumplidos

1. **Preparar datos (escalar)** ✓
   - StandardScaler aplicado a todas las variables numéricas
   - Verificación de normalización (media ≈ 0, std ≈ 1)

2. **Identificar número óptimo de clusters** ✓
   - Método del Codo (Elbow)
   - Silhouette Score
   - Gap Statistic

3. **Implementar K-Means** ✓
   - Con número óptimo de centroides
   - Múltiples inicializaciones para estabilidad
   - Reproducibilidad garantizada

4. **Gráficos para interpretar resultados** ✓
   - Boxplots de variables clave
   - Visualizaciones geográficas
   - Heatmaps de características
   - Análisis de silhouette

---

## 🔧 Tecnologías Utilizadas

| Librería | Propósito |
|----------|-----------|
| **pandas** | Manipulación de datos |
| **numpy** | Operaciones numéricas |
| **scikit-learn** | Clustering y preprocessing |
| **matplotlib** | Visualización básica |
| **seaborn** | Visualización estadística |

---

## 📁 Archivos Generados

1. **analisis_kmeans_congestion.ipynb** - Notebook principal con todo el análisis
2. **resultados_kmeans.csv** - Dataset original + columna de clusters
3. **centroides_clusters.csv** - Coordenadas de los centroides
4. **DISEÑO_FLUJO.md** - Este documento (diseño del flujo)

---

## 🚀 Cómo Ejecutar el Análisis

1. Abrir **analisis_kmeans_congestion.ipynb** en Jupyter Notebook/Lab
2. Ejecutar todas las celdas en orden secuencial
3. Revisar gráficos y métricas generadas
4. Analizar interpretaciones y conclusiones

---

## 💡 Interpretación de Resultados

Los clusters identificados representan **patrones distintos de congestión**:

- **Cluster 0**: Posiblemente congestión leve (alta velocidad, corta duración)
- **Cluster 1**: Posiblemente congestión moderada
- **Cluster 2**: Posiblemente congestión severa (baja velocidad, larga duración)
- *[Ajustar según resultados reales]*

### Variables Clave para Interpretación

- **Duration_hrs**: Tiempo de duración de la congestión
- **Speed_km/h**: Velocidad promedio (menor = más congestión)
- **Length_km**: Longitud del tramo congestionado
- **Peak_Time**: Indicador de hora pico
- **Ubicación geográfica**: Latitud/Longitud

---

## 📝 Notas Importantes

- El análisis es **completamente reproducible** (random_state fijado)
- Los datos están **escalados** antes del clustering (requisito crítico)
- Se utilizan **tres métodos** para validar el número óptimo de clusters
- Las visualizaciones facilitan la **interpretación del negocio**

---

**Fecha de creación:** Noviembre 2024  
**Curso:** Minería de Datos  
**Tema:** Análisis de Clustering con K-Means
