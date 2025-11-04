# Estrutura de GitHub Workflows

Esta pasta contém todos os workflows de automação do projeto, organizados por categoria.

## 📂 Estrutura de Pastas

workflows/
├── _common_steps.yml # Passos compartilhados por todos os workflows
├── crypto/ # Workflows relacionados a análise de criptomoedas
│ ├── bot.yml # Trading bot automático
│ ├── data_update.yml # Atualização de datasets de cripto
│ └── actions.yml # Outras ações relacionadas
├── deploy/ # Workflows de deployment
│ └── streamlit.yml # Deploy de aplicações Streamlit
└── schedules/ # Workflows agendados
└── nightly_build.yml # Tarefas noturnas de build/test


## 🛠️ Workflows Existentes

### _common_steps.yml
- **Propósito**: Contém a configuração básica compartilhada por todos os workflows
- **Inclui**:
  - Setup do Python
  - Instalação de dependências básicas
  - Configuração do ambiente

### crypto/bot.yml
- **Propósito**: Executa o trading bot automático
- **Trigger**: Agendado a cada 6 horas + manual (workflow_dispatch)
- **Dependências**: ccxt, python-telegram-bot

### crypto/data_update.yml
- **Propósito**: Atualiza datasets de criptomoedas
- **Trigger**: Diário às 3AM UTC
- **Outputs**: Novos dados no diretório `02_Crypto_Analysis/data/`

### schedules/nightly_build.yml
- **Propósito**: Executa testes e validações noturnas
- **Trigger**: Diário à 1AM UTC
- **Ações**:
  - Rodar testes unitários
  - Validar qualidade de código
  - Gerar relatórios