---
layout: default
dark_mode: true
title: Portfólio de Ciência de Dados - Aldo Bernardi
description: Portfólio de projetos em Ciência de Dados, SQL, Python e Visualização de Dados
meta:
  - name: keywords
    content: "ciência de dados, portfolio, python, sql, power bi, machine learning, aldo bernardi"
  - property: og:image
    content: "/assets/images/portfolio-preview.png"
---

<link rel="icon" href="{{ '/_includes/favicon.ico' | relative_url }}">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

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
    line-height: 1.6;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
  }
  
  /* Header Profile */
  .profile-header {
    display: flex;
    align-items: center;
    gap: 30px;
    margin: 40px 0;
  }
  
  .profile-header img {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: 3px solid var(--accent);
    object-fit: cover;
  }
  
  /* Cards */
  .project-card {
    background-color: var(--card-dark);
    border-radius: 12px;
    padding: 30px;
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
  
  /* Buttons */
  .btn-accent {
    background-color: var(--accent);
    color: white;
    padding: 10px 20px;
    border-radius: 6px;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin: 8px 8px 8px 0;
    transition: all 0.2s ease;
    font-weight: 500;
  }
  
  .btn-accent:hover {
    background-color: var(--hover);
    transform: scale(1.05);
  }
  
  /* Skills */
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
  
  .skill-item {
    margin-bottom: 15px;
  }
  
  .skill-bar {
    height: 6px;
    background-color: var(--accent);
    border-radius: 3px;
    margin-top: 5px;
  }
  
  /* Featured Project */
  .featured-project {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    margin-bottom: 50px;
  }
  
  .featured-project img {
    width: 100%;
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.3);
  }
  
  /* Responsive */
  @media (max-width: 768px) {
    .profile-header {
      flex-direction: column;
      text-align: center;
    }
    
    .featured-project {
      grid-template-columns: 1fr;
    }
    
    .skills-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

<!-- Header Section -->
<div class="profile-header">
  <img src="https://avatars.githubusercontent.com/u/85644066" alt="Aldo Bernardi">
  <div>
    <h1 style="margin: 0;">Portfólio de Ciência de Dados</h1>
    <h2 style="margin: 0; color: var(--accent);">Aldo Bernardi</h2>
    <p>Transformando dados em decisões estratégicas</p>
    <div style="margin-top: 15px;">
      <a href="https://linkedin.com/in/aldo-bernardi/" class="btn-accent" target="_blank">
        <i class="fab fa-linkedin"></i> LinkedIn
      </a>
      <a href="https://github.com/aldber" class="btn-accent" target="_blank">
        <i class="fab fa-github"></i> GitHub
      </a>
    </div>
  </div>
</div>

<!-- Featured Project -->
<div class="featured-project">
  <img src="/01_SP_Housing/assets/images/distribuicao_precos.png" alt="Dashboard Imobiliário SP">
  <div>
    <h2>Projeto em Destaque</h2>
    <h3>Análise Imobiliária de São Paulo</h3>
    <p>Explore os padrões de preços por distrito com este dashboard interativo que combina análise geográfica avançada com visualizações 3D.</p>
    <a href="/01_SP_Housing/notebooks/" class="btn-accent">
      <i class="fas fa-code"></i> Ver Notebooks de Análise
    </a>
    <a href="/01_SP_Housing/assets/interactive/mapa_calor.html" class="btn-accent">
      <i class="fas fa-map"></i> Acessar Dashboard
    </a>
  </div>
</div>

## 🚀 Projetos em Destaque

<div class="project-card">
  <h3>Monitor de Criptoativos</h3>
  <p><strong>Resumo:</strong> Sistema automatizado para análise de oportunidades de trading em criptomoedas com atualização horária via GitHub Actions.</p>
  <p><strong>Tecnologias:</strong> Python, Streamlit, CCXT, Telegram API</p>
  
  <div style="margin-top: 20px;">
    <a href="https://aldber-crypto.streamlit.app/" class="btn-accent" target="_blank">
      <i class="fas fa-chart-line"></i> Ver Dashboard
    </a>
    <a href=".github/workflows/crypto_bot.yml" class="btn-accent">
      <i class="fas fa-code-branch"></i> Workflow GitHub
    </a>
  </div>
</div>

## 📊 Projetos SQL e Business Intelligence

<div class="project-card">
  <h3>Semana 01 – Fundamentos de SQL</h3>
  <p><strong>Atividades:</strong></p>
  <ul>
    <li>Importação de base de imóveis reais (São Paulo)</li>
    <li>Criação da estrutura de banco de dados</li>
    <li>Consultas básicas: SELECT, WHERE, ORDER BY, LIMIT</li>
  </ul>
  
  <div style="margin-top: 20px;">
    <a href="/03_SQL-BI-Projects/Semana_01/" class="btn-accent">
      <i class="fas fa-database"></i> Ver Projeto
    </a>
    <span style="margin-left: 15px;">
      <i class="fas fa-file-code"></i> Script: <code>queries_basicas_01.sql</code>
    </span>
  </div>
</div>

<div class="project-card">
  <h3>Semana 02 – Agregações e KPIs</h3>
  <p><strong>Atividades:</strong></p>
  <ul>
    <li>Funções agregadas: AVG, SUM, COUNT, MIN, MAX</li>
    <li>Agrupamentos com GROUP BY e filtros com HAVING</li>
    <li>Exportação de dados para Power BI</li>
    <li>Dashboard de KPIs com indicadores e mapa</li>
  </ul>
  
  <div style="margin-top: 20px;">
    <a href="/03_SQL-BI-Projects/Semana_02/" class="btn-accent">
      <i class="fas fa-chart-bar"></i> Ver Projeto
    </a>
    <span style="margin-left: 15px;">
      <i class="fas fa-file-powerpoint"></i> Dashboard: <code>sp_kpis_dashboard.pbix</code>
    </span>
  </div>
</div>

## 🛠️ Habilidades Técnicas

<div class="skills-grid">
  <div class="skill-card">
    <h4><i class="fas fa-code"></i> Linguagens</h4>
    
    <div class="skill-item">
      <span>Python (Pandas, NumPy)</span>
      <div class="skill-bar" style="width: 90%"></div>
    </div>
    
    <div class="skill-item">
      <span>SQL (PostgreSQL, BigQuery)</span>
      <div class="skill-bar" style="width: 85%"></div>
    </div>
  </div>
  
  <div class="skill-card">
    <h4><i class="fas fa-chart-line"></i> Visualização</h4>
    
    <div class="skill-item">
      <span>Plotly & Dash</span>
      <div class="skill-bar" style="width: 80%"></div>
    </div>
    
    <div class="skill-item">
      <span>GeoPandas & Folium</span>
      <div class="skill-bar" style="width: 75%"></div>
    </div>
  </div>
  
  <div class="skill-card">
    <h4><i class="fas fa-tools"></i> Ferramentas</h4>
    
    <div class="skill-item">
      <span>Git & GitHub</span>
      <div class="skill-bar" style="width: 88%"></div>
    </div>
    
    <div class="skill-item">
      <span>Docker</span>
      <div class="skill-bar" style="width: 70%"></div>
    </div>
  </div>
</div>

## 📬 Vamos Conversar

<div class="project-card" style="text-align: center;">
  <h3>Interessado em trabalhar juntos?</h3>
  <p style="margin-bottom: 20px;">Estou aberto a oportunidades e colaborações em projetos de ciência de dados.</p>
  
  <a href="https://linkedin.com/in/aldo-bernardi/" class="btn-accent" target="_blank">
    <i class="fab fa-linkedin"></i> LinkedIn
  </a>
  <a href="https://github.com/aldber" class="btn-accent" target="_blank">
    <i class="fab fa-github"></i> GitHub
  </a>
  <a href="mailto:aldo.bernardi@gmail.com" class="btn-accent">
    <i class="fas fa-envelope"></i> Enviar Email
  </a>
</div>