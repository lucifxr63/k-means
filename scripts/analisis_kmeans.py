"""
Análisis K-Means - Congestión Vehicular Santiago
Script Python alternativo al notebook
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings
filterwarnings('ignore')
from pathlib import Path

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples

# Configuración de rutas
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_DIR = PROJECT_ROOT / 'data'
RESULTADOS_DIR = PROJECT_ROOT / 'resultados'

# Configuración de visualización
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette('husl')

print("="*80)
print("ANÁLISIS K-MEANS - CONGESTIÓN VEHICULAR SANTIAGO")
print("="*80)

# ============================================================================
# 1. CARGAR DATOS
# ============================================================================
print("\n[1/7] Cargando datos...")
df = pd.read_csv(DATA_DIR / 'congestion-1.csv')
print(f"✓ Datos cargados: {df.shape[0]} filas x {df.shape[1]} columnas")

# ============================================================================
# 2. PREPARACIÓN DE DATOS
# ============================================================================
print("\n[2/7] Preparando datos...")

# Seleccionar variables numéricas
variables_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
df_clustering = df[variables_numericas].copy()
df_clustering = df_clustering.dropna()

# Escalado
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_clustering)

print(f"✓ Variables seleccionadas: {len(df_clustering.columns)}")
print(f"✓ Registros válidos: {len(df_clustering)}")
print(f"✓ Datos escalados (media={df_scaled.mean():.6f}, std={df_scaled.std():.6f})")

# ============================================================================
# 3. MÉTODO DEL CODO
# ============================================================================
print("\n[3/7] Calculando método del Codo...")
inertias = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(df_scaled)
    inertias.append(kmeans.inertia_)
    print(f"  K={k}: Inercia={kmeans.inertia_:.2f}")

# Visualización
plt.figure(figsize=(10, 6))
plt.plot(K_range, inertias, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Número de Clusters (k)', fontsize=12)
plt.ylabel('Inercia (WCSS)', fontsize=12)
plt.title('Método del Codo para K-Means', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xticks(K_range)
plt.tight_layout()
plt.savefig(RESULTADOS_DIR / 'grafico_elbow.png', dpi=300, bbox_inches='tight')
print(f"✓ Gráfico guardado: {RESULTADOS_DIR / 'grafico_elbow.png'}")
plt.close()

# ============================================================================
# 4. MÉTODO SILHOUETTE
# ============================================================================
print("\n[4/7] Calculando Silhouette Score...")
silhouette_scores = []

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(df_scaled)
    score = silhouette_score(df_scaled, labels)
    silhouette_scores.append(score)
    print(f"  K={k}: Silhouette Score={score:.4f}")

# Visualización
plt.figure(figsize=(10, 6))
plt.plot(K_range, silhouette_scores, 'go-', linewidth=2, markersize=8)
plt.xlabel('Número de Clusters (k)', fontsize=12)
plt.ylabel('Silhouette Score', fontsize=12)
plt.title('Análisis de Silhouette para K-Means', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xticks(K_range)
plt.tight_layout()
plt.savefig(RESULTADOS_DIR / 'grafico_silhouette.png', dpi=300, bbox_inches='tight')
print(f"✓ Gráfico guardado: {RESULTADOS_DIR / 'grafico_silhouette.png'}")
plt.close()

k_optimo = K_range[np.argmax(silhouette_scores)]
print(f"\n✓ K óptimo según Silhouette: {k_optimo} (Score: {max(silhouette_scores):.4f})")

# ============================================================================
# 5. IMPLEMENTAR K-MEANS FINAL
# ============================================================================
print(f"\n[5/7] Implementando K-Means con K={k_optimo}...")

kmeans_final = KMeans(n_clusters=k_optimo, random_state=42, n_init=20)
clusters = kmeans_final.fit_predict(df_scaled)

# Agregar clusters al dataframe
df_resultado = df.copy()
df_resultado['Cluster'] = clusters

# Métricas
silhouette_final = silhouette_score(df_scaled, clusters)
print(f"✓ Silhouette Score final: {silhouette_final:.4f}")
print(f"✓ Inercia final: {kmeans_final.inertia_:.2f}")

print("\nDistribución de clusters:")
print(df_resultado['Cluster'].value_counts().sort_index())

# ============================================================================
# 6. VISUALIZACIONES
# ============================================================================
print("\n[6/7] Generando visualizaciones...")

# Boxplots
variables_analizar = ['Duration_hrs', 'Length_km', 'Speed_km/h', 'Peak_Time']

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
axes = axes.flatten()

for i, var in enumerate(variables_analizar):
    df_resultado.boxplot(column=var, by='Cluster', ax=axes[i])
    axes[i].set_title(f'Distribución de {var} por Cluster', fontsize=12, fontweight='bold')
    axes[i].set_xlabel('Cluster', fontsize=11)
    axes[i].set_ylabel(var, fontsize=11)
    axes[i].get_figure().suptitle('')

plt.tight_layout()
plt.savefig(RESULTADOS_DIR / 'boxplots_clusters.png', dpi=300, bbox_inches='tight')
print(f"✓ Gráfico guardado: {RESULTADOS_DIR / 'boxplots_clusters.png'}")
plt.close()

# Mapa geográfico
plt.figure(figsize=(14, 10))
scatter = plt.scatter(df_resultado['Longitud'], 
                      df_resultado['Latitud'], 
                      c=df_resultado['Cluster'], 
                      cmap='viridis', 
                      alpha=0.6, 
                      s=50,
                      edgecolors='black',
                      linewidth=0.5)

plt.colorbar(scatter, label='Cluster')
plt.xlabel('Longitud', fontsize=12)
plt.ylabel('Latitud', fontsize=12)
plt.title('Distribución Geográfica de Clusters', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(RESULTADOS_DIR / 'mapa_geografico.png', dpi=300, bbox_inches='tight')
print(f"✓ Gráfico guardado: {RESULTADOS_DIR / 'mapa_geografico.png'}")
plt.close()

# Heatmap
caracteristicas_clave = ['Duration_hrs', 'Length_km', 'Speed_km/h', 'Peak_Time', 'Hora Inicio', 'Hora Fin']
cluster_means = df_resultado.groupby('Cluster')[caracteristicas_clave].mean()

plt.figure(figsize=(12, 8))
sns.heatmap(cluster_means.T, annot=True, fmt='.2f', cmap='YlOrRd', 
            cbar_kws={'label': 'Valor promedio'}, linewidths=0.5)
plt.title('Heatmap de Características Promedio por Cluster', fontsize=14, fontweight='bold')
plt.xlabel('Cluster', fontsize=12)
plt.ylabel('Variable', fontsize=12)
plt.tight_layout()
plt.savefig(RESULTADOS_DIR / 'heatmap_clusters.png', dpi=300, bbox_inches='tight')
print(f"✓ Gráfico guardado: {RESULTADOS_DIR / 'heatmap_clusters.png'}")
plt.close()

# ============================================================================
# 7. EXPORTAR RESULTADOS
# ============================================================================
print("\n[7/7] Exportando resultados...")

# Guardar resultados
df_resultado.to_csv(RESULTADOS_DIR / 'resultados_kmeans.csv', index=False)
print(f"✓ Resultados exportados: {RESULTADOS_DIR / 'resultados_kmeans.csv'}")

# Guardar centroides
centroides = pd.DataFrame(scaler.inverse_transform(kmeans_final.cluster_centers_), 
                          columns=df_clustering.columns)
centroides.to_csv(RESULTADOS_DIR / 'centroides_clusters.csv', index=False)
print(f"✓ Centroides exportados: {RESULTADOS_DIR / 'centroides_clusters.csv'}")

# Resumen por cluster
print("\n" + "="*80)
print("PERFIL DE CLUSTERS")
print("="*80)

for cluster in range(k_optimo):
    print(f"\n--- CLUSTER {cluster} ---")
    cluster_data = df_resultado[df_resultado['Cluster'] == cluster]
    
    print(f"Registros: {len(cluster_data)} ({len(cluster_data)/len(df_resultado)*100:.1f}%)")
    print(f"Duración promedio: {cluster_data['Duration_hrs'].mean():.2f} hrs")
    print(f"Longitud promedio: {cluster_data['Length_km'].mean():.2f} km")
    print(f"Velocidad promedio: {cluster_data['Speed_km/h'].mean():.2f} km/h")
    print(f"Peak Time promedio: {cluster_data['Peak_Time'].mean():.2f}")
    
    if 'Commune' in cluster_data.columns:
        comuna_top = cluster_data['Commune'].mode()
        if len(comuna_top) > 0:
            print(f"Comuna más frecuente: {comuna_top.values[0]}")

print("\n" + "="*80)
print("✓ ANÁLISIS COMPLETADO")
print("="*80)
print("\nArchivos generados:")
print("  - resultados_kmeans.csv")
print("  - centroides_clusters.csv")
print("  - grafico_elbow.png")
print("  - grafico_silhouette.png")
print("  - boxplots_clusters.png")
print("  - mapa_geografico.png")
print("  - heatmap_clusters.png")
print("\n¡Listo para presentar!")
