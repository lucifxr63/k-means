import json

# Leer el notebook
with open('scripts/analisis_kmeans_congestion.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

print(f"Total de celdas: {len(notebook['cells'])}")

# Verificar tipo de las primeras celdas
for i in range(min(5, len(notebook['cells']))):
    cell = notebook['cells'][i]
    source_preview = ''.join(cell['source'][:50]) if cell['source'] else ''
    print(f"Celda {i}: Tipo={cell['cell_type']}, Contenido: {source_preview}...")

# La celda 1 debe ser 'code' (contiene las importaciones)
if len(notebook['cells']) > 1:
    cell_1 = notebook['cells'][1]
    if cell_1['cell_type'] != 'code':
        print(f"\n⚠️ Corrigiendo celda 1: {cell_1['cell_type']} → code")
        cell_1['cell_type'] = 'code'
        
        # Guardar el notebook corregido
        with open('scripts/analisis_kmeans_congestion.ipynb', 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        
        print("✓ Notebook corregido y guardado")
    else:
        print("\n✓ Celda 1 ya es de tipo 'code'")

print("\n📊 Resumen de tipos de celdas:")
cell_types = {}
for cell in notebook['cells']:
    cell_type = cell['cell_type']
    cell_types[cell_type] = cell_types.get(cell_type, 0) + 1

for cell_type, count in cell_types.items():
    print(f"  - {cell_type}: {count} celdas")
