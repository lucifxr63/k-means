# 📊 Datos del Proyecto

Esta carpeta contiene el dataset utilizado para el análisis.

## Dataset Principal

### `congestion-1.csv`
Dataset de congestión vehicular en Santiago de Chile.

**Características:**
- **Filas:** 76,140 registros
- **Columnas:** 70 variables
- **Tamaño:** ~17 MB
- **Formato:** CSV

**Variables principales:**
- `Latitud` / `Longitud` - Ubicación geográfica
- `Fecha` - Fecha del registro
- `Duration_hrs` - Duración de la congestión en horas
- `Length_km` - Longitud del tramo congestionado en km
- `Speed_km/h` - Velocidad promedio en km/h
- `Peak_Time` - Indicador de hora pico
- `Commune` - Comuna
- `Street` - Calle
- `Hora Inicio` / `Hora Fin` - Horarios
- Variables one-hot encoded para comunas y días de la semana (Commune_*, Dia_Semana_*)

## Fuente

Dataset proporcionado para la actividad sumativa del curso de Minería de Datos.

## Uso

Los scripts buscan automáticamente el archivo en esta ubicación:
```
../data/congestion-1.csv
```

Si necesitas usar otro dataset, colócalo aquí con el mismo nombre o modifica las rutas en los scripts.
