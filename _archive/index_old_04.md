---
layout: default
dark_mode: true
---

<link rel="icon" href="{{ '/_includes/favicon.ico' | relative_url }}">
<style>
  :root {
    --bg-dark: #121212;
    --card-dark: #1e1e1e;
    --text-primary: #e0e0e0;
    --text-secondary: #a0a0a0;
    --accent: #6c63ff;
    --hover: #7d75ff;
  }
  
  body {
    background-color: var(--bg-dark);
    color: var(--text-primary);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  
  .project-card {
    background-color: var(--card-dark);
    border-radius: 12px;
    padding: 25px;
    margin-bottom: 40px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.3);
    transition: all 0.3s ease;
    border-left: 4px solid var(--accent);
  }
  
  .project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.4);
    border-left: 4px solid var(--hover);
  }
  
  .btn-accent {
    background-color: var(--accent);
    color: white;
    padding: 10px 20px;
    border-radius: 6px;
    text-decoration: none;
    display: inline-block;
    margin: 8px 8px 8px 0;
    transition: all 0.2s ease;
    font-weight: 500;
  }
  
  .btn-accent:hover {
    background-color: var(--hover);
    transform: scale(1.05);
  }
  
  h1, h2, h3 {
    color: var(--text-primary);
  }
  
  .skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin: 30px 0;
  }
  
  .skill-card {
    background-color: var(--card-dark);
    padding: 20px;
    border-radius: 8px;
    border-top: 3px solid var(--accent);
  }
</style>

# Portfólio de Ciência de Dados <br> <span style="color: var(--accent)">Aldo Bernardi</span>

## 🚀 Projetos em Destaque

---

### 1. Dashboard Imobiliário 3D - California (Nova Versão)
[![Preview](01_California_Housing/assets/images/preview_3d.png)](01_California_Housing/assets/3d_imoveis.html)

**Tecnologias:** Python, Plotly, GeoPandas, Dark Theme  
**Novos Recursos:**  
- Visualização noturna otimizada  
- Filtros interativos por região  
- Análise comparativa temporal  

**Destaques:**  
▸ Integração com dados do Zillow  
▸ Modelo preditivo com SHAP values  

[📁 Código Fonte](https://github.com/aldber/DataScience-Portfolio/tree/main/01_California_Housing) | 
[📊 Dashboard Dark](01_California_Housing/assets/3d_imoveis_dark.html){: .btn .btn-accent } | 
[📥 Dataset Atualizado](01_California_Housing/data/california_housing_2024.csv){: .btn .btn-accent }

---

### 2. Análise Técnica de Criptoativos (Dashboard Interativo)
[![Crypto Dashboard](02_Crypto_Analysis/assets/images/technical_analysis.png)](02_Crypto_Analysis/assets/technical_analysis.html)

**Stack Modernizada:**  
- Streamlit com tema dark  
- Pandas TA para indicadores avançados  
- Plotly para visualizações dinâmicas  

**Indicadores Implementados:**  
✓ Bandas de Bollinger com ajuste automático  
✓ RSI com níveis personalizáveis  
✓ MACD com histograma

📁 Código Fonte{: .btn .btn-accent } |
🔄 Pipeline de Dados{: .btn .btn-accent } |
📈 Demo ao Vivo{: .btn .btn-accent }

👨‍💻 Perfil Técnico
<div class="skills-grid"> <div class="skill-card"> <h4><i class="fas fa-database"></i> Engenharia de Dados</h4> <ul> <li>Pipelines com Airflow</li> <li>APIs REST & GraphQL</li> <li>SQL Avançado</li> <li>Spark para Big Data</li> </ul> </div> <div class="skill-card"> <h4><i class="fas fa-chart-network"></i> Análise</h4> <ul> <li>Séries Temporais Financeiras</li> <li>GeoAnálise com Kepler.gl</li> <li>Visualização Interativa</li> </ul> </div> <div class="skill-card"> <h4><i class="fas fa-robot"></i> Machine Learning</h4> <ul> <li>XGBoost/LightGBM</li> <li>Redes Neurais Básicas</li> <li>AutoML com PyCaret</li> </ul> </div> </div>
📬 Contato Profissional
{% include contact_form.html %}

**Conecte-se:** em construção

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/aldo-bernardi/) 
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)](https://github.com/aldber) 
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle)](https://kaggle.com/aldobernardi) 
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium)](https://medium.com/@aldobernardi)