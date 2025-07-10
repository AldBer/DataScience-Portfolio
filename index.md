---
layout: default
dark_mode: true
---

<!-- META SEO -->
<title>Portfólio de Dados | Aldo Bernardi</title>
<meta name="description" content="Portfólio de Ciência de Dados de Aldo Bernardi, com projetos em Python, SQL, BI e Machine Learning.">
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- FAVICON & ICONS -->
<link rel="icon" href="{{ '/_includes/favicon.ico' | relative_url }}">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<!-- STYLES -->
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
    margin: 0;
    padding: 0 20px;
  }

  header {
    position: sticky;
    top: 0;
    background-color: var(--bg-dark);
    z-index: 999;
    padding: 10px 0;
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

  .profile-header {
    display: flex;
    align-items: center;
    gap: 20px;
    margin-top: 30px;
    flex-wrap: wrap;
  }

  .profile-header img {
    border-radius: 100px;
    width: 120px;
    height: 120px;
    object-fit: cover;
    border: 3px solid var(--accent);
  }

  @media(max-width: 600px) {
    .profile-header {
      flex-direction: column;
      text-align: center;
    }
  }
</style>

<header>
  <h1>Portfólio de Ciência de Dados - <span style="color: var(--accent)">Aldo Bernardi</span></h1>
</header>

<div class="profile-header">
  <img src="https://avatars.githubusercontent.com/u/85644066" alt="Foto de Aldo Bernardi">
  <div>
    <h2>🎯 Transformando dados em decisões inteligentes</h2>
    <p>Especialista em Análise de Dados, SQL, Python, Dashboards e Machine Learning</p>
  </div>
</div>

---

## 🚀 Projetos em Destaque

### 1. Dashboard Imobiliário 3D - Califórnia  
📍 **Resumo**: Análise geográfica com filtros dinâmicos e visualização noturna.  
🔧 **Tecnologias:** Python, Plotly, GeoPandas  

[📁 Código Fonte](https://github.com/aldber/DataScience-Portfolio/tree/main/01_California_Housing){: .btn .btn-accent }  
[📊 Acessar Dashboard](01_California_Housing/assets/3d_imoveis_dark.html){: .btn .btn-accent }

---

### 2. Análise Automatizada de Criptoativos  
📍 **Resumo**: Dashboard com atualização diária automática via GitHub Actions.  
🔧 **Tecnologias:** Streamlit, Python, GitHub Actions  

[📊 Ver Dashboard](https://yourusername-streamlit-app.streamlit.app/){: .btn .btn-accent }  
[🔁 Workflow GitHub](.github/workflows/update_crypto.yaml){: .btn .btn-accent }

---

## 📊 Projetos com SQL & BI (em breve)

> Esta seção trará relatórios desenvolvidos com SQL, Power BI e Python para análises corporativas, como:  
- Vendas por região  
- Análise de churn  
- Rentabilidade de produtos

🔧 *Estamos desenvolvendo!*

---

## 👨‍💻 Perfil Técnico

<div class="skills-grid">
  <div class="skill-card">
    <h4><i class="fas fa-database"></i> Engenharia de Dados</h4>
    <ul>
      <li>Pipelines com Airflow</li>
      <li>APIs REST/GraphQL</li>
      <li>Spark para Big Data</li>
    </ul>
  </div>
  <div class="skill-card">
    <h4><i class="fas fa-chart-line"></i> Análise de Dados</h4>
    <ul>
      <li>Séries Temporais</li>
      <li>Geoanálise (Kepler.gl)</li>
      <li>Visualização Interativa</li>
    </ul>
  </div>
  <div class="skill-card">
    <h4><i class="fas fa-robot"></i> Machine Learning</h4>
    <ul>
      <li>XGBoost / LightGBM</li>
      <li>Redes Neurais</li>
      <li>AutoML (PyCaret)</li>
    </ul>
  </div>
</div>

---

## 📬 Contato Profissional

{% include contact_form.html %}

<div style="margin-top:30px">
  <a href="https://linkedin.com/in/aldo-bernardi/" target="_blank" class="btn-accent">
    <i class="fab fa-linkedin"></i> LinkedIn
  </a>
  <a href="https://github.com/aldber" target="_blank" class="btn-accent">
    <i class="fab fa-github"></i> GitHub
  </a>
  <a href="https://kaggle.com/aldobernardi" target="_blank" class="btn-accent">
    <i class="fab fa-kaggle"></i> Kaggle
  </a>
</div>