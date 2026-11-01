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


# Exibir informações sobre a estrutura da base
print("\nESTRUTURA DOS DADOS:")
df.info()

# Exibir quantidade de linhas e colunas
print("\nDIMENSÕES DA BASE:")
print(df.shape)

# Contar valores ausentes em cada coluna
print("\nVALORES AUSENTES POR COLUNA:")
print(df.isnull().sum())
