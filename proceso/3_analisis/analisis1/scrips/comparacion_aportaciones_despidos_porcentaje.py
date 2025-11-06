import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración estética
sns.set(style="whitegrid", font_scale=1.3)
plt.rcParams['figure.dpi'] = 120

# Crear carpeta output si no existe
output_dir = "proceso/3_analisis/analisis1/graficas"
os.makedirs(output_dir, exist_ok=True)

# Carga del dataset
df = pd.read_csv("proceso/3_analisis/analisis1/dataset/motivodeconflicto.csv")

# Calcular totales
total_aportaciones = df['Aportaciones'].sum()
total_despidos = df['Despido'].sum()

# Calcular porcentaje
total_general = total_aportaciones + total_despidos
pct_aportaciones = (total_aportaciones / total_general) * 100
pct_despidos = (total_despidos / total_general) * 100

# Crear DataFrame comparativo
df_comparacion = pd.DataFrame({
    'Tipo de conflicto': ['Aportaciones', 'Despidos'],
    'Porcentaje': [pct_aportaciones, pct_despidos]
})

# Gráfico de barras comparativo
plt.figure(figsize=(8,6))
barplot = sns.barplot(
    data=df_comparacion, 
    x='Tipo de conflicto', 
    y='Porcentaje', 
    palette=['#FF4C4C','#4C79FF']
)

# Agregar etiquetas con porcentaje
for p in barplot.patches:
    height = p.get_height()
    barplot.annotate(f'{height:.1f}%', 
                     (p.get_x() + p.get_width() / 2., height), 
                     ha='center', va='bottom', 
                     fontsize=14, fontweight='bold')

plt.title("Comparativa de peligrosidad de conflictos (en %)", fontsize=18, fontweight='bold')
plt.ylabel("Porcentaje del total")
plt.xlabel("")
plt.ylim(0, 100)
plt.tight_layout()

# Guardar y mostrar
plt.savefig(os.path.join(output_dir, "comparacion_aportaciones_despidos_porcentaje.png"), dpi=300)
plt.show()

print(f" Gráfico guardado en {output_dir}")
