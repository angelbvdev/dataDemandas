import pandas as pd

# Carga del dataset
df = pd.read_csv("proceso/1_data/dataoriginal/juiciosiniciadosprofedet-motivodeconflicto.csv") 

print("===== INFORMACIÓN GENERAL =====")
print(f"Número de filas: {df.shape[0]}")
print(f"Número de columnas: {df.shape[1]}\n")

print("===== COLUMNAS Y TIPOS DE DATOS =====")
print(df.dtypes)
print("\n")

print("===== PRIMEROS 5 REGISTROS =====")
print(df.head())
print("\n")

print("===== VALORES NULOS POR COLUMNA =====")
print(df.isnull().sum())
print("\n")

print("===== ESTADÍSTICAS DESCRIPTIVAS =====")
print(df.describe(include='all'))  # include='all' para columnas numéricas y categóricas
print("\n")

print("===== NÚMERO DE VALORES ÚNICOS POR COLUMNA =====")
print(df.nunique())
print("\n")

print("===== FRECUENCIAS DE CATEGÓRICAS =====")
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"Columna: {col}")
    print(df[col].value_counts().head(10))  # Muestra los 10 valores más comunes
    print("-"*40)
