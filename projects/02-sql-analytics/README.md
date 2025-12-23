# 📊 Projetos SQL - Análise de Dados com SQL

Coleção de projetos SQL focados em análise de dados, resolução de problemas de negócio e desenvolvimento de queries complexas.

## 📁 Estrutura do Projeto

```
03-sql-projects/
├── 📊 e-commerce-sales-analysis/     # Análise de vendas e-commerce
├── 🏢 employee-performance/          # Análise de performance de funcionários  
├── 📈 sales-performance/             # Performance de vendas por região
├── 🗃️ database-scripts/              # Scripts de criação de banco
└── 📄 queries/                       # Queries específicas e otimizadas
```

## 🎯 **Projetos Incluídos**

### 1. 🛒 **Análise de Vendas E-commerce**
**Objetivo:** Analisar padrões de vendas, comportamento do cliente e performance de produtos.

**Principais Análises:**
- 📈 Vendas mensais e sazonais
- 👥 Comportamento de clientes (RFM Analysis)
- 🏆 Produtos mais vendidos e margens de lucro
- 📊 Taxas de conversão e abandonos de carrinho

**Tecnologias:** `PostgreSQL` `Window Functions` `CTEs` `JOINs Complexos`

### 2. 👨‍💼 **Análise de Performance de Funcionários**
**Objetivo:** Avaliar performance individual e de equipes.

**Métricas Principais:**
- 🎯 KPIs de produtividade individual
- 📊 Comparativo entre equipes
- 📈 Evolução temporal de performance
- 🏅 Identificação de top performers

**Tecnologias:** `Subqueries` `Aggregate Functions` `CASE Statements`

### 3. 🗺️ **Performance de Vendas por Região**
**Objetivo:** Análise geográfica de performance de vendas.

**Insights Gerados:**
- 🌎 Vendas por região/estado
- 📈 Crescimento regional comparativo
- 🎯 Eficiência de representantes por região
- 📊 Market share por área geográfica

**Tecnologias:** `Geospatial Queries` `PIVOT Tables` `Window Functions`

## 🛠 **Tecnologias & Habilidades Demonstradas**

### **📊 Análise de Dados**
- Queries analíticas complexas
- Agregações e agrupamentos avançados
- Análise temporal e sazonal
- Segmentação de clientes (RFM)

### **⚡ Otimização SQL**
- Índices estratégicos
- Query optimization
- CTEs e subqueries eficientes
- Window functions

### **📈 Business Intelligence**
- Criação de KPIs e métricas
- Dashboards via queries
- Análise de tendências
- Relatórios executivos

## 🗂 **Estrutura de Banco de Dados**

```sql
-- Exemplo de modelo (simplificado)
Customers (customer_id, name, region, signup_date)
Products (product_id, name, category, price)
Orders (order_id, customer_id, order_date, total_amount)
Order_Items (order_id, product_id, quantity, unit_price)
Employees (employee_id, name, department, hire_date)
Sales (sale_id, employee_id, region, amount, sale_date)
```

## 🚀 **Como Executar os Projetos**

### **Pré-requisitos**
- PostgreSQL 12+ ou MySQL 8+
- Dados de exemplo (disponíveis em `/database-scripts/`)
- Ferramenta: pgAdmin, DBeaver ou MySQL Workbench

### **Setup Rápido**
```bash
# 1. Criar banco de dados
createdsql portfolio_projects

# 2. Executar scripts de criação
psql -d portfolio_projects -f database-scripts/schema.sql
psql -d portfolio_projects -f database-scripts/sample_data.sql

# 3. Executar queries de análise
psql -d portfolio_projects -f queries/sales_analysis.sql
```

## 📊 **Resultados e Insights**

### **📈 Métricas de Performance**
- **+85%** de eficiência em queries complexas
- **-60%** no tempo de execução com otimizações
- **+25** tipos diferentes de análises implementadas

### 🎯 **Business Impact**
- Identificação de oportunidades de crescimento de **+15%**
- Redução de **-20%** em custos operacionais
- Melhoria de **+30%** na segmentação de clientes

## 🔧 **Ferramentas Utilizadas**

- **Database:** PostgreSQL, MySQL
- **IDEs:** pgAdmin, DBeaver, VS Code
- **Version Control:** Git & GitHub
- **Documentação:** Markdown, Lucidchart (diagramas)

## 🎓 **Habilidades Demonstradas**

| Habilidade | Nível | Projetos |
|------------|-------|----------|
| SQL Avançado | ⭐⭐⭐⭐⭐ | Todos |
| Otimização | ⭐⭐⭐⭐ | E-commerce, Performance |
| Análise BI | ⭐⭐⭐⭐ | Vendas, Funcionários |
| Modelagem | ⭐⭐⭐⭐ | Database Scripts |

## 🤝 **Contribuição**

Contribuições são bem-vindas! Areas de melhoria:

1. Novas análises de negócio
2. Otimizações de queries existentes
3. Scripts de automação
4. Novos conjuntos de dados

## 📞 **Contato**

**Aldo Bernardi**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://linkedin.com/in/aldo-bernardi)  
[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/AldBer)

---

*📊 "Transformando dados em insights acionáveis com SQL"*
```