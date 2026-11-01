import pandas as pd
import re
from datetime import datetime


def limpar_categoria(categoria):

    # Verificar se a categoria está vazia.
    if pd.isna(categoria) or str(categoria).strip() == "":
        return "Sem categoria"
    
    # Remover espaços no inicio e no final
    categoria = str(categoria).strip()

    # Transformar todas as letras em minúsculas
    categoria = categoria.lower()

    # Remover pontuações e caracteres indevidos
    categoria = re.sub(r"[^a-z\s]", "", categoria)

    # Remover espaços repetidos
    categoria = re.sub(r"\s+", " ", categoria).strip()

    # Se o resultado ficar vazio, preencher
    if categoria == "":
        return "sem categoria"

    return categoria



def padronizar_canal(canal):

    # Remover espaços e padronizar letras minúsculas
    canal = str(canal).strip().lower()

    # Identificar o canal e retornar o nome oficial
    if canal == "mercado":
        return "Mercado"

    elif canal == "loja física":
        return "Loja física"

    elif canal == "web":
        return "Web"

    else:
        return "canal não reconhecido"


def converter_data(data):

    # Verificar se a data está vazia
    if pd.isna(data) or str(data).strip() == "":
        return None

    # Tentar converter o texto em data
    try:
        return datetime.strptime(
            str(data).strip(),
            "%Y-%m-%d %H:%M:%S"
        )

    # Caso a data seja inválida, retornar None
    except ValueError:
        return None
    

