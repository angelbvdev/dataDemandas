import pandas as pd
import matplotlib.pyplot as plt
import os

# Crear carpeta output si no existe
output_dir = "proceso/3_analisis/analisis1/graficas"
os.makedirs(output_dir, exist_ok=True)

# Carga del dataset
df = pd.read_csv("proceso/3_analisis/analisis1/dataset/motivodeconflicto.csv")

# Totales
total_aportaciones = df['Aportaciones'].sum()
total_despidos = df['Despido'].sum()

# Datos para el pastel
labels = ['Aportaciones', 'Despidos']
sizes = [total_aportaciones, total_despidos]
colors = ['#FF4C4C', '#4C79FF']  # rojo para más "peligroso", azul para menos
explode = (0.1, 0)  # resalta Aportaciones

# Crear gráfico de pastel
plt.figure(figsize=(8,8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=explode, shadow=True, textprops={'fontsize':14, 'fontweight':'bold'})

plt.title("Proporción de conflictos: Aportaciones vs Despidos", fontsize=18, fontweight='bold')
plt.tight_layout()

# Guardar y mostrar
plt.savefig(os.path.join(output_dir, "pastel_aportaciones_despidos.png"), dpi=300)
plt.show()

print(f"✅ Gráfico de pastel guardado en {output_dir}")