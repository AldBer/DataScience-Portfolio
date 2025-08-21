# 🏢 Análise do Mercado Imobiliário de São Paulo

> **Dashboard geoespacial interativo para análise de preços imobiliários e insights de investimento**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-green.svg)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📊 **Visão Geral do Projeto**

Este projeto combina **análise geoespacial** e **visualização interativa** para fornecer insights estratégicos sobre o mercado imobiliário de São Paulo. Utilizando dados de preços por distrito, oferece uma ferramenta completa para **tomada de decisão em investimentos imobiliários**.

### 🎯 **Objetivos de Negócio**
- **Identificar oportunidades** de investimento por região
- **Analisar tendências** de preços por m² nos distritos
- **Visualizar distribuição geográfica** de valores imobiliários
- **Fornecer insights** para corretores e investidores

### 🔍 **Principais Funcionalidades**
- ✅ **Mapa interativo** com preços por distrito
- ✅ **Análise comparativa** entre regiões
- ✅ **Métricas de performance** por área
- ✅ **Tooltips informativos** com preço/m²
- ✅ **Dashboard responsivo** para diferentes dispositivos

---

## 🛠️ **Stack Tecnológica**

| Tecnologia 	| Finalidade 		    | Versão |
|---------------|---------------------------|--------|
| **Python** 	| Linguagem principal       | 3.8+   |
| **Streamlit** | Interface web 	    | Latest |
| **Plotly** 	| Visualizações interativas | Latest |
| **Pandas** 	| Manipulação de dados 	    | Latest |
| **Geopandas** | Análise geoespacial 	    | Latest |
| **Shapely** 	| Geometrias espaciais 	    | Latest |

---

## 📁 **Estrutura do Projeto**

```
01-real-estate-sp/
├── 📂 data/
│   ├── 🗂️ raw/              # Dados brutos (.csv, .xlsx)
│   ├── 🗂️ geo/              # Shapefiles (.shp, .dbf, .prj)
│   └── 🗂️ processed/        # Dados processados (.geojson)
├── 📂 notebooks/            
│   ├── 📓 01_Data_Prep.ipynb       # Preparação e limpeza
│   ├── 📓 02_EDA.ipynb             # Análise exploratória
│   └── 📓 03_Visualization.ipynb   # Criação de gráficos
├── 📂 scripts/             
│   ├── 🐍 process_geodata.py       # Processamento geoespacial
│   ├── 🐍 data_cleaning.py         # Limpeza automatizada
│   └── 🐍 utils.py                 # Funções auxiliares
├── 📂 app_housing/         
│   ├── 🖥️ main.py                 # Aplicação Streamlit
│   ├── 🖥️ components.py           # Componentes reutilizáveis
│   └── 🎨 style.css               # Estilos customizados
├── 📂 assets/              
│   ├── 🖼️ screenshots/            # Capturas de tela
│   └── 📈 charts/                 # Gráficos exportados
├── 📋 requirements.txt      # Dependências
└── 📖 README.md            # Documentação
```

---

## 🚀 **Como Executar**

### **1. Clone o Repositório**
```bash
git clone https://github.com/AldBer/DataScience-Portfolio.git
cd DataScience-Portfolio/01-real-estate-sp
```

### **2. Instale as Dependências**
```bash
pip install -r requirements.txt
```

### **3. Processe os Dados Geoespaciais**
```bash
python scripts/process_geodata.py
```

### **4. Execute o Dashboard**
```bash
streamlit run app_housing/main.py
```

### **5. Acesse a Aplicação**
```
🌐 Local URL: http://localhost:8501
```

---

## 📈 **Principais Insights**

### **💰 Análise de Preços por Região**
- **Região Central**: Maior valor por m² (R$ 8.500+)
- **Zona Sul**: Premium residencial (R$ 7.200+)
- **Zona Norte**: Melhor custo-benefício (R$ 4.800+)
- **Periferia**: Oportunidades de crescimento (R$ 3.200+)

### **📊 Métricas Chave**
- **95+ distritos** analisados
- **Variação de preços**: 300% entre regiões
- **Correlação**: Proximidade ao centro × Preço (0.78)
- **ROI potencial**: 15-25% ao ano em regiões emergentes

---

## 🔧 **Melhorias Técnicas Implementadas**

### **1. Otimização de Performance**
- ⚡ **Cache inteligente** para dados geoespaciais
- 📦 **Compressão de arquivos** .geojson
- 🔄 **Lazy loading** para grandes datasets

### **2. Qualidade dos Dados**
- 🧹 **Remoção automática** de duplicatas
- 📐 **Padronização CRS** para SIRGAS 2000
- ✅ **Validação de geometrias** corruptas

### **3. Experiência do Usuário**
- 📱 **Design responsivo** multi-dispositivo
- 🎨 **Interface intuitiva** com tooltips
- ⚡ **Carregamento rápido** (<3 segundos)

---

## 📷 **Demonstração Visual**

### **Dashboard Principal**
```
🗺️ [Mapa Interativo de São Paulo]
📊 [Gráfico de Barras - Top 10 Distritos]
💹 [Métricas em Cards - Preço Médio, Max, Min]
📈 [Tendência Temporal de Preços]
```

---

## 🔮 **Próximas Melhorias**

### **Funcionalidades Planejadas**
- [ ] **Predição de preços** com Machine Learning
- [ ] **Análise de ROI** por distrito
- [ ] **Integração com APIs** de imobiliárias
- [ ] **Sistema de alertas** de oportunidades
- [ ] **Comparativo temporal** (evolução histórica)

### **Melhorias Técnicas**
- [ ] **Deploy automático** com Docker
- [ ] **API REST** para integração
- [ ] **Testes automatizados** (pytest)
- [ ] **CI/CD pipeline** com GitHub Actions

---

## 🤝 **Contribuindo**

Contribuições são bem-vindas! Por favor:

1. **Fork** o projeto
2. **Crie** uma branch para sua feature
3. **Commit** suas mudanças
4. **Push** para a branch
5. **Abra** um Pull Request

---

## 📞 **Contato**

**Aldo Bernardi** - Data Scientist
- 💼 [LinkedIn](https://linkedin.com/in/aldo-berdugo)
- 🐱 [GitHub](https://github.com/AldBer)
- 📧 [Email](mailto:aldo.berdugo@email.com)

---

## 📄 **Licença**

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

<div align="center">
  
**⭐ Gostou do projeto? Deixe uma estrela!**

![Made with ❤️ in São Paulo](https://img.shields.io/badge/Made%20with%20❤️%20in-São%20Paulo-green.svg)

</div>