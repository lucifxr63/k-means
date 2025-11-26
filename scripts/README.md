# 💻 Scripts del Análisis

Esta carpeta contiene todo el código ejecutable del proyecto.

## 📝 Archivos

### `analisis_kmeans_congestion.ipynb` ⭐ RECOMENDADO
**Notebook Jupyter principal** con el análisis completo y visualizaciones interactivas.

**Cómo ejecutar:**
```bash
jupyter notebook analisis_kmeans_congestion.ipynb
```

**Contenido:**
- Exploración de datos
- Preparación y escalado
- Métodos: Elbow, Silhouette, Gap Statistic
- Implementación K-Means
- Visualizaciones interactivas
- Interpretación de resultados

---

### `analisis_kmeans.py`
**Script Python completo** que ejecuta todo el análisis automáticamente.

**Cómo ejecutar:**
```bash
cd ..
python scripts/analisis_kmeans.py
```

**Genera:**
- CSVs con resultados
- Gráficos PNG (todos los métodos)
- Reporte en consola

⚠️ **Nota:** Tarda ~5-10 minutos con el dataset completo (76,140 filas)

---

### `test_rapido.py`
**Script de prueba rápida** con muestra de datos (10,000 filas).

**Cómo ejecutar:**
```bash
cd ..
python scripts/test_rapido.py
```

**Propósito:**
- Verificar que todo funciona
- Prueba rápida (~30 segundos)
- Ideal para debugging

---

## 🚀 ¿Cuál usar?

| Situación | Script Recomendado |
|-----------|-------------------|
| Presentación en clase | `analisis_kmeans_congestion.ipynb` |
| Generar todos los gráficos | `analisis_kmeans.py` |
| Verificar instalación | `test_rapido.py` |
| Exploración interactiva | `analisis_kmeans_congestion.ipynb` |

---

## 📊 Rutas Importantes

Los scripts buscan datos en: `../data/congestion-1.csv`
Los resultados se guardan en: `../resultados/`

Si ejecutas desde otra ubicación, ajusta las rutas según sea necesario.
