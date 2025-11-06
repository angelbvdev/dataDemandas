import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración estética
sns.set(style="whitegrid", palette="muted", font_scale=1.1)
plt.rcParams['figure.dpi'] = 120

# Crear carpeta output si no existe
output_dir = "proceso/3_analisis/analisis1/graficas"
os.makedirs(output_dir, exist_ok=True)

# Carga del dataset
df = pd.read_csv("proceso/3_analisis/analisis1/dataset/motivodeconflicto.csv")

# Convertir Fecha a datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Columna de conflictos relevantes
conflictos_cols = [
    'Aguinaldo', 'Aportaciones', 'Condiciones_Generales_Trabajo', 'Designacion_Beneficiarios',
    'Despido', 'Medidas_Disciplinarias', 'Pago_Reparto_Utilidades', 'Pension_IVCM_Riesgo_Trabajo',
    'Preferencia_Derechos', 'Prestaciones_Ley_Federal_Trabajo', 'Prestaciones_Seguridad_Social',
    'Rescision_Contrato', 'Rescision_por_Acoso', 'Retencion_Salarial', 'Retiro_Voluntario', 'Otras_Instancias'
]

# ================= 1️⃣ Evolución total de juicios por año =================
plt.figure(figsize=(10,5))
sns.lineplot(data=df, x='Anio', y='Total', marker='o')
plt.title("Evolución total de juicios por año")
plt.ylabel("Número de casos")
plt.xlabel("Año")
plt.xticks(df['Anio'].unique())
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "total_juicios_por_año.png"))
plt.show()

# ================= 2️⃣ Conflictos más frecuentes =================
total_conflictos = df[conflictos_cols].sum().sort_values(ascending=False)

plt.figure(figsize=(12,6))
sns.barplot(x=total_conflictos.values, y=total_conflictos.index, palette="viridis")
plt.title("Conflictos más frecuentes")
plt.xlabel("Número de casos")
plt.ylabel("Tipo de conflicto")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "conflictos_frecuentes.png"))
plt.show()

# ================= 3️⃣ Tendencia mensual por conflicto (ejemplo: Despido) =================
df_month = df.groupby(['Anio','Mes'])['Despido'].sum().reset_index()
meses_orden = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
df_month['Mes'] = pd.Categorical(df_month['Mes'], categories=meses_orden, ordered=True)
df_month = df_month.sort_values(['Anio','Mes'])

plt.figure(figsize=(12,6))
sns.lineplot(data=df_month, x='Mes', y='Despido', hue='Anio', marker='o', palette="tab10")
plt.title("Tendencia mensual de juicios por despido")
plt.ylabel("Número de casos")
plt.xlabel("Mes")
plt.legend(title='Año', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "tendencia_despidos.png"))
plt.show()

# ================= 4️⃣ Mapa de calor de correlación =================
plt.figure(figsize=(12,10))
corr = df[conflictos_cols].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlación entre tipos de conflictos")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "correlacion_conflictos.png"))
plt.show()

# ================= 5️⃣ Distribución de juicios por tipo en caja =================
plt.figure(figsize=(14,6))
sns.boxplot(data=df[conflictos_cols], palette="pastel")
plt.xticks(rotation=45)
plt.title("Distribución de juicios por tipo de conflicto")
plt.ylabel("Número de casos")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "distribucion_caja_conflictos.png"))
plt.show()

# ================= 6️⃣ Heatmap de juicios por año y tipo =================
df_year_conf = df.groupby('Anio')[conflictos_cols].sum()
plt.figure(figsize=(14,8))
sns.heatmap(df_year_conf.T, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Juicios por año y tipo de conflicto")
plt.xlabel("Año")
plt.ylabel("Tipo de conflicto")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "heatmap_juicios_anio_tipo.png"))
plt.show()


print(f"✅ Todos los gráficos se han guardado en la carpeta: {output_dir}")