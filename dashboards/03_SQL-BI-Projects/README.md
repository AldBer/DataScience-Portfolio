# 📊 Semana 01 - Fundamentos SQL com PostgreSQL

Este diretório contém os exercícios práticos do plano de aprendizado SQL + BI.

## ✅ Objetivos da Semana

- Instalar e configurar PostgreSQL e pgAdmin
- Criar banco de dados e tabelas
- Importar dados reais via CSV
- Executar queries básicas de análise

---

## 🏗️ Estrutura da Tabela

A tabela criada foi `imoveis`, com os seguintes campos:

| Coluna      | Tipo     | Descrição                           |
|-------------|----------|-------------------------------------|
| bairro      | TEXT     | Nome do bairro                      |
| area_m2     | NUMERIC  | Área em metros quadrados            |
| quartos     | INTEGER  | Número de quartos                   |
| preco       | NUMERIC  | Preço total do imóvel               |
| latitude    | NUMERIC  | Localização geográfica              |
| longitude   | NUMERIC  | Localização geográfica              |
| zona        | TEXT     | Região da cidade (Leste, Sul, etc.) |
| preco_m2    | NUMERIC  | Preço por metro quadrado            |

---

## 🧾 Arquivo de Dados

O arquivo `sp_properties_sample.csv` contém 500 imóveis com dados reais (região de São Paulo).

---

## 📌 Como Executar

1. Subir o arquivo CSV no seu ambiente local
2. Criar a tabela `imoveis`
3. Executar o script `semana01_queries.sql`

---

## 💻 Comandos SQL Usados

- `SELECT`
- `WHERE`
- `ORDER BY`
- `LIMIT`
- `BETWEEN`
- `DISTINCT`
- `COUNT(*)`

---

# 📊 Semana 02 – Agregações e KPIs com SQL

Nesta etapa, trabalhamos com **funções de agregação** e **agrupamentos** para gerar indicadores relevantes do mercado imobiliário.

---

## ✅ Objetivos da Semana

- Utilizar `GROUP BY` e `HAVING`
- Aplicar funções como `AVG`, `COUNT`, `SUM`, `ROUND`
- Criar **KPIs reais** com SQL para uso em relatórios e BI
- Preparar dados para visualizações no Power BI

---

## 📈 Indicadores Criados (KPIs)

| KPI                                      | Descrição                                       |
|------------------------------------------|-------------------------------------------------|
| Preço médio por bairro                   | Valor médio dos imóveis por bairro              |
| Área média por zona                      | Média em m² dos imóveis agrupados por zona      |
| Top 5 bairros mais caros por m²          | Bairros com maior média de `preço/m²`           |
| Quantidade de imóveis por zona           | Total de imóveis por região                     |
| Valor total de imóveis por bairro        | Soma de preços agrupada por bairro              |
| Bairros com mais de 3 imóveis listados   | Usando `HAVING` após `GROUP BY`                 |
| Bairros com preço médio acima de R$7000  | Identificação de regiões premium                |
| Zonas com menor preço médio              | Acessibilidade por região                       |

---

## 📁 Arquivos da Semana

- `semana02_queries.sql`: Todas as queries de agregação e análise
- `sp_properties_sample.csv`: Base de dados real de imóveis (500 registros)
- `README.md`: Este arquivo com explicações e objetivos

---

## 🧠 Funções SQL Usadas

| Função / Comando     | Descrição                                           |
|----------------------|-----------------------------------------------------|
| `AVG()`              | Calcula média                                       |
| `COUNT()`            | Conta número de linhas                              |
| `SUM()`              | Soma valores                                        |
| `GROUP BY`           | Agrupa linhas com base em uma coluna                |
| `HAVING`             | Filtra grupos (usado após `GROUP BY`)               |
| `ORDER BY`           | Ordena resultado                                    |
| `ROUND(valor, casas)`| Arredonda valores (ex: `ROUND(AVG(preco), 2)`)      |

---

## 🧩 Continuação

Na **Semana 3**, aprenderemos:
- `JOIN` entre tabelas (relacionamento)
- Tabelas normalizadas
- Visualização dos dados com Power BI a partir do PostgreSQL

Feito com 💙 por Aldo Bernardi — dados como base para decisões inteligentes!
