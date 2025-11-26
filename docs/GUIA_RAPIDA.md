# 🚀 Guía Rápida de Ejecución

## Opción 1: Jupyter Notebook (Recomendado)

### Pasos:

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

2. **Abrir Jupyter:**
```bash
jupyter notebook
```

3. **Abrir el archivo:**
   - Navegar a `analisis_kmeans_congestion.ipynb`
   - Hacer clic en el archivo

4. **Ejecutar el análisis:**
   - `Cell` → `Run All` (o `Shift + Enter` en cada celda)

5. **Revisar resultados:**
   - Los gráficos se mostrarán en el notebook
   - Se generarán archivos CSV con resultados

---

## Opción 2: Script Python

### Pasos:

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

2. **Prueba rápida (recomendado primero):**
```bash
python test_rapido.py
```
Este script usa solo 10,000 filas para verificar que todo funciona (tarda ~30 segundos)

3. **Ejecutar el análisis completo:**
```bash
python analisis_kmeans.py
```
⚠️ Nota: Con 76,140 filas puede tardar 5-10 minutos

4. **Revisar resultados:**
   - Archivos CSV: `resultados_kmeans.csv`, `centroides_clusters.csv`
   - Gráficos PNG en la carpeta del proyecto

---

## 📊 Archivos que se generarán

### CSV (Datos)
- ✅ `resultados_kmeans.csv` - Dataset original + columna de clusters
- ✅ `centroides_clusters.csv` - Coordenadas de los centroides

### PNG (Gráficos) - Solo con script Python
- ✅ `grafico_elbow.png` - Método del codo
- ✅ `grafico_silhouette.png` - Análisis de silhouette
- ✅ `boxplots_clusters.png` - Boxplots de variables clave
- ✅ `mapa_geografico.png` - Distribución geográfica
- ✅ `heatmap_clusters.png` - Heatmap de características

---

## ⚠️ Requisitos Previos

- Python 3.8 o superior
- Jupyter Notebook (para Opción 1)
- Librerías: pandas, numpy, scikit-learn, matplotlib, seaborn

---

## 💡 Consejos para la Presentación

### Al presentar en clase:

1. **Abrir el notebook** antes de tu turno
2. **Ejecutar todas las celdas** para tener los resultados listos
3. **Revisar los gráficos** principales:
   - Método del codo (identificar K óptimo)
   - Silhouette score (validar elección)
   - Boxplots (interpretar clusters)
   - Mapa geográfico (visualizar distribución)

4. **Explicar la interpretación** de cada cluster:
   - ¿Qué caracteriza a cada grupo?
   - ¿Qué patrones de congestión se identifican?
   - ¿Qué recomendaciones se pueden hacer?

### Puntos clave a mencionar:

✅ **Escalado de datos:** Usamos StandardScaler para normalizar  
✅ **Tres métodos de validación:** Elbow, Silhouette, Gap Statistic  
✅ **K óptimo:** Basado en el consenso de los métodos  
✅ **Interpretación:** Clusters representan diferentes niveles de congestión  

---

## 🐛 Solución de Problemas

### Error: "No module named 'sklearn'"
```bash
pip install scikit-learn
```

### Error: "No such file or directory: 'congestion-1.csv'"
Asegúrate de estar en la carpeta correcta:
```bash
cd z:\DEV\Respos\Universidad\mineria\Actividad\k-means
```

### Jupyter no abre
```bash
# Reinstalar Jupyter
pip install --upgrade jupyter notebook
```

### Los gráficos no se ven
En Jupyter, añadir al inicio:
```python
%matplotlib inline
```

---

## 📝 Checklist de Presentación

- [ ] Dependencias instaladas
- [ ] Notebook ejecutado completamente
- [ ] Todos los gráficos generados
- [ ] Interpretación de clusters preparada
- [ ] Archivos CSV exportados
- [ ] Conclusiones listas

---

## 🎯 Estructura de la Presentación Sugerida

1. **Introducción** (1 min)
   - Objetivo del análisis
   - Dataset utilizado

2. **Metodología** (2 min)
   - Preparación de datos (escalado)
   - Métodos para determinar K óptimo

3. **Resultados** (3 min)
   - Mostrar gráficos principales
   - Número de clusters seleccionado
   - Características de cada cluster

4. **Conclusiones** (1 min)
   - Patrones identificados
   - Insights sobre congestión

**Tiempo total:** ~7 minutos

---

¡Buena suerte con la presentación! 🎉
