# Festa em Cena 🎃

Projeto de limpeza, tratamento e análise de dados de vendas de uma loja fictícia de fantasias e acessórios de Halloween, desenvolvido utilizando Python e Pandas.

## Objetivo

O objetivo do projeto é analisar uma base de dados de pedidos, identificar inconsistências, realizar a limpeza e padronização das informações e gerar resultados que auxiliem na compreensão dos registros de vendas.

## Tecnologias utilizadas

- Python
- Pandas
- Expressões regulares (`re`)
- Módulo `datetime`
- Visual Studio Code
- Git e GitHub

## Estrutura do projeto

```text
festa-em-cena/
│
├── halloween_vendas.csv
├── main.py
├── funcoes.py
├── report.md
└── README.md
```

**Descrição dos arquivos:**

- `halloween_vendas.csv`: base de dados original utilizada na análise.
- `main.py`: arquivo principal, responsável pela leitura, validação, tratamento e análise dos dados.
- `funcoes.py`: contém funções utilizadas na limpeza de categorias, padronização dos canais e conversão de datas.
- `report.md`: relatório com os resultados e principais conclusões.
- `README.md`: documentação e instruções de execução do projeto.

## Base de dados

O arquivo `halloween_vendas.csv` contém 1.500 registros e 14 colunas, com informações sobre pedidos realizados entre agosto e novembro de 2024 e 2025.

Os dados incluem informações como:

- Identificação do pedido.
- Data da venda.
- Produto e categoria.
- Canal de venda.
- Cidade.
- Quantidade e preço unitário.
- Status do pedido.
- Data de entrega.

## Etapas desenvolvidas

### 1. Leitura e exploração dos dados
Leitura do arquivo CSV com Pandas e verificação da estrutura, dimensões, colunas e valores ausentes.

### 2. Limpeza e padronização de textos
- Preenchimento de categorias vazias com "sem categoria".
- Remoção de pontuações e espaços desnecessários.
- Padronização de letras minúsculas.
- Uniformização dos canais de venda.

### 3. Validação de dados numéricos
Identificação de quantidades inválidas, preços ausentes e preços negativos.

### 4. Verificação das datas de entrega
Análise dos pedidos sem data de entrega e comparação com os respectivos status.

### 5. Tratamento das datas de venda
Conversão das datas, identificação de registros inválidos e extração de ano, mês, dia e hora.

### 6. Análise dos pedidos
Contagem de pedidos por canal de venda e por período, considerando ano e mês separadamente.

## Principais resultados

- 18 categorias vazias preenchidas.
- 1.482 categorias não vazias padronizadas.
- 45 registros de canais de venda padronizados.
- 7 quantidades inválidas identificadas.
- 12 preços unitários ausentes.
- 4 datas de venda inválidas.
- 34 pedidos sem data de entrega com status diferente de cancelado.
- O canal Web apresentou a maior quantidade de pedidos, com 666 registros.
- Outubro apresentou o maior número de pedidos nos dois anos analisados.

Os resultados completos estão disponíveis em `report.md`.

## Como executar o projeto

### Pré-requisitos

É necessário ter Python instalado e acesso ao terminal.

### Instalação da biblioteca

No terminal, execute:

```bash
python -m pip install pandas
```

### Execução

Com os arquivos na mesma pasta, execute:

```bash
python main.py
```

O programa realizará as etapas de leitura, limpeza, validação e análise dos dados, exibindo os resultados no terminal.

## Observações

Os dados problemáticos são identificados e separados para análise, sem substituição de valores desconhecidos ou criação de informações.

As contagens representam pedidos registrados na base, não necessariamente vendas concluídas ou faturamento.

Este projeto foi desenvolvido para fins educacionais e de prática de análise e tratamento de dados.

## Autoria

Projeto acadêmico desenvolvido como atividade prática de programação e análise de dados.