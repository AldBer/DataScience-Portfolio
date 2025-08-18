# 🏠 Análise do Mercado Imobiliário de São Paulo

Dashboard interativo para visualização de preços de imóveis por distrito.

## 🛠️ Implementação

### 📂 Estrutura de Arquivos
01_SP_Housing/
├── data/
│ ├── raw/ # Dados brutos (ex: .csv de imóveis)
│ ├── geo/ # Arquivos shapefile (.shp, .dbf)
│ └── processed/ # Dados processados (.geojson)
├── notebooks/ # Jupyter notebooks de análise
│ ├── 01_Data_Prep.ipynb
│ └── visual_script.ipynb
├── script/ # Scripts Python
│ └── process_geodata.py
└── assets/ # Imagens/arquivos estáticos


### 🔧 Melhorias Implementadas
1. **Limpeza de Dados**
   - Remoção de duplicatas nos arquivos geoespaciais
   - Padronização de CRS (SIRGAS 2000)

2. **Otimizações**
   - Script `process_geodata.py` atualizado para:
     - Caminhos absolutos dinâmicos
     - Tratamento de erros robusto
     - Logging detalhado

3. **Visualização**
   - Gráficos Plotly otimizados
   - Tooltips com informações de preço/m²

## 🚀 Como Executar
```bash
# Instale as dependências
pip install -r requirements.txt

# Processe os dados geoespaciais
python script/process_geodata.py

# Execute o dashboard (Streamlit)
streamlit run app/main.py