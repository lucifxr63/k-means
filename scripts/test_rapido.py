"""
Script de prueba rápida con muestra de datos
Para verificar que todo funciona antes de correr el análisis completo
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Backend sin GUI
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings
filterwarnings('ignore')
import os
from pathlib import Path

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Obtener directorio del script y configurar rutas
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_PATH = PROJECT_ROOT / 'data' / 'congestion-1.csv'
RESULTADOS_PATH = PROJECT_ROOT / 'resultados' / 'test_resultados.csv'

print("="*80)
print("PRUEBA RÁPIDA - Análisis K-Means (con muestra de datos)")
print("="*80)

# Cargar solo una muestra de datos
print("\n[1/5] Cargando muestra de datos...")
df = pd.read_csv(DATA_PATH, nrows=10000)  # Solo 10k filas para prueba
print(f"✓ Datos cargados: {df.shape[0]} filas x {df.shape[1]} columnas")

# Preparar datos
print("\n[2/5] Preparando datos...")
variables_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
df_clustering = df[variables_numericas].copy()
df_clustering = df_clustering.dropna()

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_clustering)
print(f"✓ Datos escalados correctamente")

# Método del Codo (solo 3-8 clusters para prueba rápida)
print("\n[3/5] Método del Codo...")
inertias = []
K_range = range(2, 9)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=5)
    kmeans.fit(df_scaled)
    inertias.append(kmeans.inertia_)
    print(f"  K={k}: Inercia={kmeans.inertia_:.2f}")

# Silhouette
print("\n[4/5] Silhouette Score...")
silhouette_scores = []

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=5)
    labels = kmeans.fit_predict(df_scaled)
    score = silhouette_score(df_scaled, labels)
    silhouette_scores.append(score)
    print(f"  K={k}: Silhouette={score:.4f}")

k_optimo = K_range[np.argmax(silhouette_scores)]
print(f"\n✓ K óptimo: {k_optimo}")

# K-Means final
print(f"\n[5/5] K-Means final con K={k_optimo}...")
kmeans_final = KMeans(n_clusters=k_optimo, random_state=42, n_init=10)
clusters = kmeans_final.fit_predict(df_scaled)

df_resultado = df.copy()
df_resultado['Cluster'] = clusters

silhouette_final = silhouette_score(df_scaled, clusters)
print(f"✓ Silhouette Score final: {silhouette_final:.4f}")
print(f"✓ Distribución de clusters:")
print(df_resultado['Cluster'].value_counts().sort_index())

# Guardar resultados de prueba
df_resultado.to_csv(RESULTADOS_PATH, index=False)
print(f"\n✓ Resultados de prueba guardados en: {RESULTADOS_PATH}")

print("\n" + "="*80)
print("✓ PRUEBA COMPLETADA EXITOSAMENTE")
print("="*80)
print("\n💡 Todo funciona correctamente. Puedes ejecutar el análisis completo con:")
print("   python scripts/analisis_kmeans.py")
print("   o usar el notebook: jupyter notebook scripts/analisis_kmeans_congestion.ipynb")
