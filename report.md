# Relatório de Análise de Dados — Festa em Cena

## 1. Objetivo do projeto

O projeto Festa em Cena tem como objetivo realizar a limpeza, padronização e análise de uma base de dados de vendas de uma loja fictícia de fantasias e acessórios de Halloween.

A análise foi desenvolvida utilizando Python e Pandas, com o propósito de identificar inconsistências, tratar dados textuais, validar informações numéricas e datas, além de gerar informações que auxiliem na compreensão dos pedidos realizados.

## 2. Características da base de dados

A base utilizada foi `halloween_vendas.csv`, composta por:

- 1.500 registros de pedidos.
- 14 colunas.
- Dados referentes aos períodos de agosto a novembro de 2024 e 2025.
- Três canais de venda: Loja física, Mercado e Web.

## 3. Procedimentos realizados

### 3.1. Limpeza e padronização de textos

Foram realizadas as seguintes operações:

- Preenchimento de 18 categorias vazias com o valor "sem categoria".
- Padronização de 1.482 categorias não vazias, com remoção de pontuações, espaços desnecessários e uniformização das letras.
- Padronização de 45 registros de canais de venda.
- Padronização dos canais para os nomes oficiais: Mercado, Loja física e Web.

As alterações foram realizadas por meio de funções próprias, utilizando os recursos `strip()`, `lower()` e `re.sub()`.

### 3.2. Validação numérica

Foram identificados os seguintes problemas:

| Validação | Quantidade |
|---|---:|
| Quantidades inválidas | 7 |
| Preços unitários ausentes | 12 |
| Preços unitários negativos | 0 |
| Total de registros com problemas numéricos | 19 |
| Pedidos distintos afetados | 19 |

Os registros problemáticos foram separados para identificação, sem substituição ou criação de valores.

### 3.3. Verificação das datas de entrega

Foram identificados 143 pedidos sem data de entrega.

A análise demonstrou que:

- 109 pedidos sem data de entrega estavam com status "Cancelado".
- 34 pedidos sem data de entrega apresentavam outros status.

Foram encontrados exemplos de pedidos com status "Concluído", mas sem data de entrega, indicando possíveis inconsistências nos registros.

Nenhuma data ou status foi inventado ou alterado.

### 3.4. Tratamento das datas de venda

As datas foram convertidas utilizando o formato `%Y-%m-%d %H:%M:%S`.

Também foram extraídas informações de ano, mês, dia e hora, além da criação de uma coluna com as datas formatadas no padrão brasileiro.

Foram identificadas 4 datas inválidas, que foram separadas para análise. Os valores originais foram preservados.

## 4. Resultados das análises

### 4.1. Pedidos por canal de venda

Após a padronização, os 1.500 pedidos foram distribuídos da seguinte maneira:

| Canal de venda | Quantidade de pedidos |
|---|---:|
| Loja física | 551 |
| Mercado | 283 |
| Web | 666 |
| **Total** | **1.500** |

Não foram encontrados canais não reconhecidos após a padronização.

### 4.2. Pedidos por período

A análise considerou somente os registros com datas de venda válidas, totalizando 1.496 pedidos.

| Período | Quantidade de pedidos |
|---|---:|
| Agosto/2024 | 77 |
| Setembro/2024 | 104 |
| Outubro/2024 | 393 |
| Novembro/2024 | 174 |
| Agosto/2025 | 62 |
| Setembro/2025 | 94 |
| Outubro/2025 | 410 |
| Novembro/2025 | 182 |
| **Total** | **1.496** |

Os quatro registros com datas inválidas foram excluídos exclusivamente dessa análise temporal.

Todos os status de pedidos foram mantidos nas contagens, incluindo pedidos cancelados e concluídos.

## 5. Principais achados

### Achado 1 — Canal de venda

O canal Web apresentou a maior quantidade de pedidos, com 666 registros, representando 44,4% do total analisado.

A Loja física apresentou 551 pedidos, enquanto o Mercado registrou 283.

Esse resultado demonstra que o canal Web concentrou a maior quantidade de pedidos na base analisada. Entretanto, a quantidade de pedidos não representa necessariamente maior faturamento, pois não foram consideradas receitas ou valores totais de vendas.

### Achado 2 — Período de vendas

Outubro apresentou a maior quantidade de pedidos nos dois anos analisados.

Em outubro de 2024 foram registrados 393 pedidos, enquanto em outubro de 2025 foram registrados 410, representando um aumento de 17 pedidos, aproximadamente 4,3%.

Outro ponto observado foi que os dois anos apresentaram o mesmo total de pedidos com datas válidas: 748 em 2024 e 748 em 2025.

Esse comportamento indica uma concentração de pedidos no mês de outubro, mas não permite afirmar crescimento geral do negócio ou aumento de faturamento.

## 6. Limitações da análise

Os resultados representam a quantidade de pedidos registrados na base, não necessariamente vendas concluídas ou valores de faturamento.

As quatro datas inválidas não foram consideradas na análise por período.

Os registros com problemas numéricos e inconsistências de entrega foram identificados e separados, sem substituição de informações desconhecidas.

A análise está limitada aos dados fornecidos pelo arquivo CSV e ao intervalo de agosto a novembro de 2024 e 2025.

## 7. Conclusão

O projeto permitiu aplicar técnicas de limpeza, padronização e validação de dados utilizando Python e Pandas.

Foram identificadas inconsistências em categorias, canais de venda, quantidades, preços e datas, permitindo melhorar a organização e a confiabilidade das informações disponíveis.

As análises demonstraram que o canal Web concentrou a maior quantidade de pedidos e que outubro foi o mês com maior volume de registros nos dois anos avaliados.

O trabalho também evidenciou a importância da qualidade dos dados para a obtenção de resultados confiáveis e para a tomada de decisões em um contexto empresarial fictício.

---

**Tecnologias utilizadas:** Python, Pandas, expressão regular (`re`), módulo `datetime` e Git/GitHub.