import json

# Leer el notebook
with open('scripts/analisis_kmeans_congestion.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

print(f"Total de celdas: {len(notebook['cells'])}\n")

# Palabras clave que indican que una celda debería ser código
code_keywords = [
    'import ', 'from ', 'df =', 'print(', 'plt.', 'sns.', 
    'kmeans =', 'for ', 'def ', 'scaler =', '.fit(', '.transform(',
    '.to_csv(', 'pd.', 'np.', '= StandardScaler', '= KMeans'
]

# Palabras clave que indican que es markdown (títulos)
markdown_keywords = ['##', '###', '####']

correcciones = 0

for i, cell in enumerate(notebook['cells']):
    source = ''.join(cell['source'])
    
    # Si la celda empieza con ## o ###, debe ser markdown
    if any(source.strip().startswith(kw) for kw in markdown_keywords):
        if cell['cell_type'] != 'markdown':
            print(f"Celda {i}: Corrigiendo a markdown")
            cell['cell_type'] = 'markdown'
            correcciones += 1
    # Si contiene código Python, debe ser code
    elif any(kw in source for kw in code_keywords):
        if cell['cell_type'] != 'code':
            preview = source[:80].replace('\n', ' ')
            print(f"Celda {i}: {cell['cell_type']} → code")
            print(f"  Contenido: {preview}...")
            cell['cell_type'] = 'code'
            
            # Asegurar que tiene la estructura correcta de celda de código
            if 'execution_count' not in cell:
                cell['execution_count'] = None
            if 'outputs' not in cell:
                cell['outputs'] = []
            
            correcciones += 1

if correcciones > 0:
    # Guardar el notebook corregido
    with open('scripts/analisis_kmeans_congestion.ipynb', 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print(f"\n✓ {correcciones} celdas corregidas y guardadas")
else:
    print("\n✓ Todas las celdas ya tienen el tipo correcto")

# Resumen final
print("\n📊 Resumen final de tipos de celdas:")
cell_types = {}
for cell in notebook['cells']:
    cell_type = cell['cell_type']
    cell_types[cell_type] = cell_types.get(cell_type, 0) + 1

for cell_type, count in cell_types.items():
    print(f"  - {cell_type}: {count} celdas")
