## Fluxo de Trabalho de Análise Cripto

1. `notebooks/binance_data_pipeline.ipynb`  
   - Extração e limpeza de dados da Binance API  
   - Protótipo inicial dos indicadores técnicos  
   - Análise estatística exploratória

2. `scripts/technical_analysis.py`  
   - Dashboard interativo com Streamlit  
   - Visualizações otimizadas para tomada de decisão  
   - Parâmetros customizáveis pelo usuário

▶ Execute o dashboard final com:  
```bash
streamlit run scripts/technical_analysis.py