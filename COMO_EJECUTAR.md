# 🚀 Cómo Ejecutar el Análisis - Guía Paso a Paso

## ✅ Correcciones Aplicadas

He corregido el notebook para que:
1. ✅ Use la ruta correcta del dataset: `../data/congestion-1.csv`
2. ✅ Incluya la celda de entrenamiento del modelo K-Means
3. ✅ Guarde los resultados en `../resultados/` en lugar de la carpeta actual

---

## 📓 Opción 1: Jupyter Notebook (Recomendado para Presentación)

### Paso 1: Abrir el notebook
```bash
cd z:\DEV\Respos\Universidad\mineria\Actividad\k-means
jupyter notebook scripts/analisis_kmeans_congestion.ipynb
```

### Paso 2: Ejecutar todas las celdas
En Jupyter, en el menú superior:
- **Cell → Run All** (Ejecutar todas las celdas)

O presiona **Shift + Enter** en cada celda para ejecutarlas una por una.

### Paso 3: Verificar resultados
Los archivos se guardarán automáticamente en:
- `resultados/resultados_kmeans.csv` - Dataset con clusters asignados
- `resultados/centroides_clusters.csv` - Centroides de cada cluster

### ⏱️ Tiempo estimado:
- **Con 76,140 filas completas:** ~5-10 minutos
- **Gap Statistic:** ~3-5 minutos (la parte más lenta)

---

## 💻 Opción 2: Script Python (Más Rápido, Sin Interacción)

### Ejecución directa:
```bash
cd z:\DEV\Respos\Universidad\mineria\Actividad\k-means
python scripts/analisis_kmeans.py
```

### Ventajas:
- ✅ Genera automáticamente todos los gráficos PNG
- ✅ Muestra progreso en consola [1/7], [2/7], etc.
- ✅ Más rápido que el notebook
- ✅ No necesita interacción

### Archivos generados:
```
resultados/
├── resultados_kmeans.csv
├── centroides_clusters.csv
├── grafico_elbow.png
├── grafico_silhouette.png
├── boxplots_clusters.png
├── mapa_geografico.png
└── heatmap_clusters.png
```

---

## 🧪 Opción 3: Prueba Rápida (30 segundos)

Para verificar que todo funciona antes del análisis completo:

```bash
cd z:\DEV\Respos\Universidad\mineria\Actividad\k-means
python scripts/test_rapido.py
```

**Qué hace:**
- Usa solo 10,000 filas (muestra)
- Ejecuta todo el análisis
- Verifica que no hay errores
- Genera: `resultados/test_resultados.csv`

---

## 📊 ¿Qué Opción Elegir?

| Situación | Opción Recomendada |
|-----------|-------------------|
| **Presentación en clase** | Notebook (Opción 1) - Más visual |
| **Generar todos los gráficos** | Script Python (Opción 2) - Más rápido |
| **Primera vez / Verificar** | Prueba Rápida (Opción 3) - 30 seg |
| **Explorar/Experimentar** | Notebook (Opción 1) - Interactivo |

---

## ⚠️ Problemas Comunes y Soluciones

### Problema 1: "FileNotFoundError: congestion-1.csv"
**Causa:** Ejecutando desde directorio incorrecto

**Solución:**
```bash
# Asegúrate de estar en la raíz del proyecto
cd z:\DEV\Respos\Universidad\mineria\Actividad\k-means

# Luego ejecuta
python scripts/test_rapido.py
```

### Problema 2: "Notebook is not trusted"
**Causa:** Jupyter no confía en el notebook

**Solución:** En Jupyter, click en "Not Trusted" en la parte superior derecha, luego "Trust"

### Problema 3: Archivos se guardan en carpeta incorrecta
**Causa:** Notebook desactualizado

**Solución:** El notebook ya está corregido. Si persiste:
1. Cerrar el notebook
2. Refrescar la página (F5)
3. Volver a abrir el notebook
4. Ejecutar "Cell → Run All"

### Problema 4: Demora mucho en Gap Statistic
**Esto es normal.** Gap Statistic es computacionalmente costoso:
- Con 10,000 filas: ~1 minuto
- Con 76,140 filas: ~3-5 minutos

**Alternativas:**
- Usa el script Python (más optimizado)
- Reduce `n_refs` de 10 a 5 en la celda de Gap Statistic

---

## 📋 Checklist de Ejecución

Antes de ejecutar, verifica:

- [ ] Estás en la carpeta raíz del proyecto
- [ ] Las dependencias están instaladas (`pip install -r requirements.txt`)
- [ ] El archivo `data/congestion-1.csv` existe
- [ ] La carpeta `resultados/` existe

Durante la ejecución:

- [ ] Las celdas se ejecutan sin errores
- [ ] Los gráficos se muestran correctamente
- [ ] Los mensajes de progreso aparecen

Después de ejecutar:

- [ ] Verificar que existen archivos en `resultados/`
- [ ] Abrir los CSVs para confirmar que tienen datos
- [ ] Ver los gráficos PNG generados

---

## 🎯 Para la Presentación (Miércoles 27/11)

### Recomendación: **Jupyter Notebook**

**Por qué:**
- ✅ Visual e interactivo
- ✅ Puedes explicar cada paso
- ✅ Los gráficos se ven en línea
- ✅ Más profesional para presentar

**Preparación:**
1. **Día antes:** Ejecuta todo el notebook una vez y guarda
2. **Día de presentación:** Abre el notebook ya ejecutado
3. **Durante presentación:** Muestra los resultados, re-ejecuta celdas específicas si preguntan

**Alternativa - Pre-generar gráficos:**
```bash
# Un día antes, ejecuta el script para tener todos los PNG listos
python scripts/analisis_kmeans.py

# Luego usa los PNG en una presentación PowerPoint si prefieres
```

---

## 📈 Orden de Ejecución del Análisis

1. **Carga y exploración** (~10 seg)
2. **Preparación y escalado** (~5 seg)
3. **Método del Codo** (~30 seg)
4. **Silhouette Score** (~1 min)
5. **Gap Statistic** (~3-5 min) ⏳ La parte más lenta
6. **K-Means final** (~10 seg)
7. **Visualizaciones** (~30 seg)
8. **Exportar resultados** (~5 seg)

**Total: ~7-10 minutos** para el dataset completo

---

## 💡 Tips Finales

1. **Primera ejecución:** Usa el test rápido para verificar
2. **Análisis completo:** Déjalo correr completo, no lo interrumpas
3. **Presentación:** Ejecuta el notebook el día antes y guárdalo
4. **Gráficos extras:** El script Python genera PNG adicionales

---

**Última actualización:** 26 de noviembre de 2025  
**Estado:** ✅ Notebook corregido y listo para usar
