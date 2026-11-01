import pandas as pd
from funcoes import limpar_categoria, padronizar_canal, converter_data


# Leitura do arquivo CSV
df = pd.read_csv("halloween_vendas.csv", encoding="utf-8")

# Guardar os valores originais antes da limpeza
categoria_original = df["categoria"].copy()
canal_original = df["canal_venda"].copy()
data_venda_original = df["data_venda"].copy()

# Converter os textos em datas
df["data_venda_convertida"] = pd.to_datetime(
    df["data_venda"].apply(converter_data)
)

# Identificar datas vazias ou inválidas
datas_invalidas = df["data_venda_convertida"].isna()

# Contabilizar os problemas
qtd_datas_invalidas = datas_invalidas.sum()

# Separar os registros com datas problemáticas
datas_problematicas = df.loc[
    datas_invalidas,
    ["pedido_id", "data_venda"]
].copy()

print("\nVERIFICAÇÃO DAS DATAS DE VENDA:")
print("Datas vazias ou inválidas:", qtd_datas_invalidas)
print("\nExemplos de datas problemáticas:")
print(datas_problematicas.head(3))

# Extrair informações das datas válidas
df["ano"] = df["data_venda_convertida"].dt.year
df["mes"] = df["data_venda_convertida"].dt.month
df["dia"] = df["data_venda_convertida"].dt.day
df["hora"] = df["data_venda_convertida"].dt.hour

# Formatar a data no padrão brasileiro
df["data_venda_formatada"] = (
    df["data_venda_convertida"].dt.strftime("%d/%m/%Y")
)

print("\nDATAS FORMATADAS:")
print(
    df[
        ["data_venda", "data_venda_formatada", "ano", "mes", "dia", "hora"]
    ].head(5)
)

# Identificar quantidades inválidas
quantidade_invalida = (
    df["quantidade"].isna()
    | (df["quantidade"] <= 0)
)

# Contabilizar os problemas
qtd_quantidades_invalidas = quantidade_invalida.sum()

# Separar os registros problemáticos
registros_quantidade_invalida = df.loc[
    quantidade_invalida,
    ["pedido_id", "quantidade"]
]

print("\nVALIDAÇÃO DE QUANTIDADES:")
print("Quantidades inválidas:", qtd_quantidades_invalidas)
print(registros_quantidade_invalida.head(3))

# Identificar preços ausentes
preco_ausente = df["preco_unitario"].isna()

# Identificar preços negativos
preco_negativo = df["preco_unitario"] < 0

# Identificar todos os preços problemáticos
preco_invalido = preco_ausente | preco_negativo

# Contabilizar os problemas
qtd_precos_ausentes = preco_ausente.sum()
qtd_precos_negativos = preco_negativo.sum()
qtd_precos_invalidos = preco_invalido.sum()

# Separar os registros problemáticos
registros_preco_invalido = df.loc[
    preco_invalido,
    ["pedido_id", "preco_unitario"]
]

print("\nVALIDAÇÃO DE PREÇOS:")
print("Preços ausentes:", qtd_precos_ausentes)
print("Preços negativos:", qtd_precos_negativos)
print("Total de preços problemáticos:", qtd_precos_invalidos)
print("\nExemplos:")
print(registros_preco_invalido.head(3))

# Reunir os problemas de quantidade e preço
problemas_numericos = quantidade_invalida | preco_invalido

# Separar os pedidos com problemas numéricos
registros_numericos_problematicos = df.loc[
    problemas_numericos
].copy()

# Contar os pedidos distintos afetados
qtd_pedidos_com_problemas = (
    registros_numericos_problematicos["pedido_id"].nunique()
)

print("\nRESUMO DOS PROBLEMAS NUMÉRICOS:")
print("Registros com problemas:", problemas_numericos.sum())
print("Pedidos distintos afetados:", qtd_pedidos_com_problemas)




# Limpar e padronizar as categorias
df["categoria"] = df["categoria"].apply(limpar_categoria)

# Padronizar os canais de venda
df["canal_venda"] = df["canal_venda"].apply(padronizar_canal)

# Identificar os canais reconhecidos
canais_reconhecidos = ["Mercado", "Loja física", "Web"]

# Filtrar os canais válidos
df_canais_validos = df[
    df["canal_venda"].isin(canais_reconhecidos)
].copy()

# Contar pedidos distintos por canal
pedidos_por_canal = (
    df_canais_validos.groupby("canal_venda")["pedido_id"]
    .nunique()
)

# Contar pedidos com canais não reconhecidos
pedidos_nao_reconhecidos = df.loc[
    ~df["canal_venda"].isin(canais_reconhecidos),
    "pedido_id"
].nunique()

print("\nPEDIDOS POR CANAL DE VENDA:")
print(pedidos_por_canal)

print("\nPedidos com canal não reconhecido:", pedidos_nao_reconhecidos)
print("Total de pedidos analisados:", df_canais_validos["pedido_id"].nunique())

# Separar os pedidos com datas válidas
df_datas_validas = df[
    df["data_venda_convertida"].notna()
].copy()

# Criar a identificação do período no formato ano-mês
df_datas_validas["ano_mes"] = (
    df_datas_validas["data_venda_convertida"].dt.strftime("%Y-%m")
)

# Contar pedidos distintos por período
pedidos_por_periodo = (
    df_datas_validas.groupby("ano_mes")["pedido_id"]
    .nunique()
)

print("\nPEDIDOS POR PERÍODO:")
print(pedidos_por_periodo)

print(
    "\nPedidos excluídos da análise por data inválida:",
    datas_invalidas.sum()
)



# Contabilizar categorias vazias antes da limpeza
categoria_original_texto = categoria_original.fillna("").astype(str)

categoria_vazia = (
    categoria_original.isna()
    | categoria_original_texto.str.strip().eq("")
)

qtd_categorias_preenchidas = categoria_vazia.sum()


# Contabilizar categorias não vazias que foram modificadas
categoria_nao_vazia = ~categoria_vazia

qtd_categorias_alteradas = (
    categoria_nao_vazia
    & (categoria_original_texto != df["categoria"])
).sum()

print("\nLIMPEZA DE CATEGORIAS:")
print("Categorias vazias preenchidas:", qtd_categorias_preenchidas)
print("Categorias não vazias alteradas:", qtd_categorias_alteradas)

# Contabilizar canais que foram padronizados
qtd_canais_alterados = (
    canal_original.astype(str).str.strip()
    != df["canal_venda"]
).sum()

print("Canais de venda padronizados:", qtd_canais_alterados)

# Identificar pedidos sem data de entrega
sem_entrega = (
    df["data_entrega"].isna()
    | df["data_entrega"].astype(str).str.strip().eq("")
)

# Identificar pedidos cancelados
cancelado = (
    df["status_pedido"].astype(str).str.strip().str.lower()
    == "cancelado"
)

# Identificar pedidos sem entrega com status diferente de cancelado
sem_entrega_outro_status = sem_entrega & ~cancelado

# Identificar pedidos sem entrega que foram cancelados
sem_entrega_cancelados = sem_entrega & cancelado

qtd_sem_entrega_cancelados = sem_entrega_cancelados.sum()

print(
    "Pedidos sem entrega e cancelados:",
    qtd_sem_entrega_cancelados
)


# Contabilizar os resultados
qtd_sem_entrega = sem_entrega.sum()
qtd_cancelados = cancelado.sum()
qtd_sem_entrega_outro_status = sem_entrega_outro_status.sum()

print("\nVERIFICAÇÃO DE DATAS DE ENTREGA:")
print("Pedidos sem data de entrega:", qtd_sem_entrega)
print("Pedidos cancelados:", qtd_cancelados)
print("Pedidos sem entrega com outro status:", qtd_sem_entrega_outro_status)

# Exibir até 3 exemplos de pedidos que precisam de atenção
print("\nEXEMPLOS DE PEDIDOS SEM ENTREGA E NÃO CANCELADOS:")
print(
    df.loc[
        sem_entrega_outro_status,
        ["pedido_id", "status_pedido", "data_entrega"]
    ].head(3)
)


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

# Verificar os canais de venda existentes
print("\nCANAIS DE VENDA ENCONTRADOS:")
print(df["canal_venda"].unique())


print("\nCANAIS APÓS A PADRONIZAÇÃO:")
print(df["canal_venda"].value_counts(dropna=False))

