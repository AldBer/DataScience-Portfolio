# 📊 Semana 01 - Fundamentos SQL com PostgreSQL

Este diretório contém os exercícios práticos da primeira semana do plano de aprendizado SQL + BI.

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

## 📁 Estrutura Recomendada no Repositório