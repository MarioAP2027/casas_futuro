import pandas as pd
import matplotlib.pyplot as plt

# Lee tu CSV
df = pd.read_csv('Viviendas_futuro.csv')
print(df)

# Crea el gráfico del ahorro
plt.figure(figsize=(8, 4))
plt.bar(df['Concepto'], df['Ahorro_Porcentaje'], color='#4A90E2')
plt.xticks(rotation=15, ha='right')
plt.title('Porcentaje de Ahorro - Vivienda del Futuro 2030')
plt.ylabel('Ahorro %')
plt.tight_layout()
plt.savefig('grafico_ahorro.png')
print("¡Listo! Gráfico creado como grafico_ahorro.png")