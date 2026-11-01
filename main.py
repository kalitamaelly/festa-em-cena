import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv("halloween_vendas.csv", encoding="utf-8")

# Exibir informações iniciais
print("TOTAL DE REGISTROS:")
print(len(df))

print("\nNOMES DAS COLUNAS:")
print(df.columns.tolist())

print("\nPRIMEIROS 3 REGISTROS:")
print(df.head(3))
