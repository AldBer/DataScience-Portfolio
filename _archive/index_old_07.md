---
layout: default
dark_mode: true
---

<!-- Adicionar no head -->
<meta property="og:image" content="/assets/images/portfolio-preview.png">
<meta name="keywords" content="ciência de dados, portfolio, python, sql, aldo bernardi">
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

<div class="profile-header" style="display: flex; align-items: center; gap: 20px; margin-bottom: 40px;">
  <img src="https://avatars.githubusercontent.com/u/85644066" alt="Aldo Bernardi" style="width: 100px; height: 100px; border-radius: 50%; border: 3px solid var(--accent);">
  <div>
    <h1 style="margin: 0;">Portfólio de Ciência de Dados</h1>
    <h2 style="margin: 0; color: var(--accent);">Aldo Bernardi</h2>
    <p>Transformando dados em decisões estratégicas</p>
  </div>
</div>

## 🚀 Projetos em Destaque

Nesta seção, você encontrará os principais projetos desenvolvidos por Aldo Bernardi em ciência de dados, com foco em visualizações interativas, automações e insights aplicáveis a problemas reais.

<div class="project-card">
  <h3>Dashboard Imobiliário - São Paulo</h3>
  <p><strong>Resumo:</strong> Análise geográfica avançada dos distritos de SP</p>
  <p><strong>Tecnologias:</strong> Python, GeoPandas, Folium</p>
  <a href="/01_SP_Housing/notebooks/" class="btn">📁 Código Fonte</a>
  <a href="/01_SP_Housing/assets/interactive/mapa_calor.html" class="btn">📊 Acessar Dashboard</a>
</div>

<div class="project-card">
  <h3>Monitor de Criptoativos</h3>
  <p><strong>Resumo:</strong> Análise automática de oportunidades de trading</p>
  <p><strong>Tecnologias:</strong> Python, Streamlit, GitHub Actions</p>
  <a href="https://aldber-crypto.streamlit.app/" class="btn">📊 Ver Dashboard</a>
  <a href=".github/workflows/crypto_bot.yml" class="btn">🔁 Workflow GitHub</a>
</div>

## 📊 Projetos SQL e Business Intelligence

Esta seção acompanha o desenvolvimento semanal do aprendizado em SQL de Aldo Bernardi, com foco em manipulação de dados, geração de KPIs e integração com ferramentas de visualização como Power BI.

<div class="project-card">
  <h3>Semana 01 – Fundamentos de SQL</h3>
  <p><strong>Atividades:</strong></p>
  <ul>
    <li>Importação de base de imóveis reais (São Paulo)</li>
    <li>Criação da estrutura de banco de dados</li>
    <li>Consultas básicas: SELECT, WHERE, ORDER BY, LIMIT</li>
  </ul>
  <a href="/03_SQL-BI-Projects/Semana_01/" class="btn">📁 Ver Projeto</a>
  <span>📄 Script: <code>queries_basicas_01.sql</code></span>
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
  <a href="/03_SQL-BI-Projects/Semana_02/" class="btn">📁 Ver Projeto</a>
  <span>📊 Dashboard: <code>sp_kpis_dashboard.pbix</code></span>
</div>

## 🛠️ Habilidades Técnicas

Você pode conhecer mais sobre minha experiência profissional acessando meu <a href="https://linkedin.com/in/aldo-bernardi/" target="_blank">perfil no LinkedIn</a>.

<div class="project-card">
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
    <div>
      <h4>Linguagens</h4>
      <ul>
        <li>🐍 Python (Pandas, NumPy)</li>
        <li>🛢️ SQL (PostgreSQL, BigQuery)</li>
      </ul>
    </div>
    <div>
      <h4>Visualização</h4>
      <ul>
        <li>📊 Plotly, Power BI</li>
        <li>🗺️ GeoPandas, Folium</li>
      </ul>
    </div>
    <div>
      <h4>Ferramentas</h4>
      <ul>
        <li>⚙️ Git, Docker</li>
        <li>☁️ Google Cloud</li>
      </ul>
    </div>
  </div>
</div>

## 📬 Contato

<div class="project-card" style="text-align: center;">
  <a href="https://linkedin.com/in/aldo-bernardi/" class="btn" target="_blank">LinkedIn</a>
  <a href="https://github.com/aldber" class="btn" target="_blank">GitHub</a>
</div>
