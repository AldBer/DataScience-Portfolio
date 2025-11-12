📊 Dashboard de Performance de Vendas

![Dashboard Preview](assets/dashboard-preview.png)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Dash](https://img.shields.io/badge/Dash-2.14.1-blue)
![Plotly](https://img.shields.io/badge/Plotly-5.17.0-orange)

Dashboard interativo para análise de performance de vendas com visualizações em tempo real e métricas estratégicas.

🚀 Características Principais

- 📈 **Análise de Tendências**: Vendas e lucro ao longo do tempo
- 🌍 **Distribuição Geográfica**: Vendas por região do Brasil
- 📦 **Performance por Produto**: Margens de lucro e unidades vendidas
- ⭐ **Satisfação do Cliente**: Avaliações médias por produto
- 🎯 **KPIs em Tempo Real**: Métricas atualizadas com filtros
- 🎨 **Design Responsivo**: Adaptável para desktop e mobile

🛠️ Tecnologias Utilizadas

```python
# Stack Tecnológica
Dash==2.14.1           # Framework web
Plotly==5.17.0         # Visualizações interativas  
Pandas==2.1.4          # Manipulação de dados
Dash-Bootstrap-Components==1.5.0  # UI profissional
NumPy==1.26.0          # Cálculos numéricos

📥 Instalação e Execução
Pré-requisitos
Python 3.8 ou superior

Git instalado

1. Clonar o Repositório
bash
git clone https://github.com/AldBer/DataScience-Portfolio.git
cd DataScience-Portfolio/03-dashboards
2. Configurar Ambiente Virtual
bash
# Criar ambiente (opcional mas recomendado)
python -m venv dash_env
source dash_env/bin/activate  # Linux/Mac
# ou
dash_env\Scripts\activate     # Windows
3. Instalar Dependências
bash
pip install -r requirements.txt
4. Executar a Aplicação
bash
python app.py
5. Acessar o Dashboard
Abra seu navegador e acesse: http://127.0.0.1:8050

🎮 Como Usar
Filtros Interativos
📅 Período: Selecione o intervalo de datas
📦 Produtos: Filtre por produtos específicos
🌍 Região: Analise por região geográfica
📊 Categoria: Filtre por categoria de produtos

Métricas Principais
💰 Receita Total: Soma de todas as vendas
📦 Unidades Vendidas: Quantidade total de produtos
👥 Clientes Ativos: Base de clientes ativos
🎯 Ticket Médio: Valor médio por venda

📊 Estrutura do Projeto

03-dashboards/
├── 📄 app.py                 # Aplicação principal
├── 📄 README.md              # Documentação
├── 🗂️ assets/               # Recursos estáticos
│   └── 🎨 style.css          # Estilos customizados
├── 🗂️ data/                 # Módulos de dados
│   ├── api_clients.py        # Clientes de API
│   ├── data_processors.py    # Processamento
│   └── data_cache.py         # Sistema de cache
├── 🗂️ components/           # Componentes reutilizáveis
├── 📄 requirements.txt       # Dependências
├── 📄 .gitignore            # Arquivos ignorados
└── 📄 LICENSE               # Licença MIT


🔧 Desenvolvimento

Adicionar Novos Gráficos
1. Crie o componente em components/charts.py

2. Adicione ao layout em app.py

3. Implemente o callback para atualização

Integrar Novas Fontes de Dados
1. Estenda data/api_clients.py

2. Adicione processamento em data/data_processors.py

3. Atualize os callbacks em app.py

🌐 Deploy

Render (Recomendo) - Gratuito - [Render](https://render.com)

1. Conecte seu repositório GitHub

2. Configure build command: pip install -r requirements.txt

3. Configure start command: python app.py

📈 Próximas Melhorias
🔄 Dados em tempo real com APIs

🌙 Modo dark/light toggle

📤 Exportação de relatórios PDF/Excel

🔔 Alertas automáticos de metas

📱 Versão mobile otimizada

🔐 Autenticação de usuários

🤝 Contribuição
Contribuições são bem-vindas! Siga os passos:

Fork o projeto

Crie uma branch: git checkout -b feature/nova-funcionalidade

Commit suas mudanças: git commit -m 'Add nova funcionalidade'

Push para a branch: git push origin feature/nova-funcionalidade

Abra um Pull Request

📄 Licença

Este projeto está sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

### O que a Licença MIT permite:
- ✅ Usar o código livremente
- ✅ Copiar e modificar
- ✅ Distribuir inclusive comercialmente
- ✅ Usar em projetos privados

### Sua única obrigação:
- 📝 Manter o aviso de copyright original

**Link oficial:** [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT)

👨‍💻 Autor
Aldo Bernardi

GitHub: @AldBer

LinkedIn: Aldo Bernardi

⭐ Se este projeto te ajudou, deixe uma star no repositório!