# 📊 Carpeta de Resultados

Esta carpeta contiene todos los archivos generados por el análisis K-Means.

## Archivos que se generan

### Al ejecutar `test_rapido.py`:
- `test_resultados.csv` - Resultados con muestra de datos (10,000 filas)
- `grafico_elbow.png` - Gráfico del método del codo (muestra)

### Al ejecutar `analisis_kmeans.py`:
- `resultados_kmeans.csv` - Dataset completo con columna de clusters
- `centroides_clusters.csv` - Coordenadas de los centroides
- `grafico_elbow.png` - Método del Codo
- `grafico_silhouette.png` - Análisis de Silhouette
- `boxplots_clusters.png` - Boxplots de variables clave
- `mapa_geografico.png` - Distribución geográfica de clusters
- `heatmap_clusters.png` - Heatmap de características por cluster

## Nota

Los archivos CSV y PNG generados están en `.gitignore` para evitar subir archivos pesados al repositorio.
