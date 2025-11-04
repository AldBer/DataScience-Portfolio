# 01-real-estate-sp/streamlit_app.py - VERSÃO SIMPLIFICADA
import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

# Configuração inicial
st.set_page_config(layout="wide", page_title="Dashboard Imóveis SP")

st.title("🏠 Dashboard de Imóveis em São Paulo - CARREGANDO...")

# Função de normalização
def normalize_name(name):
    if pd.isna(name):
        return ""
    return (
        str(name)
        .lower()
        .strip()
        .replace('á', 'a').replace('à', 'a').replace('â', 'a').replace('ã', 'a')
        .replace('é', 'e').replace('ê', 'e')
        .replace('í', 'i')
        .replace('ó', 'o').replace('ô', 'o').replace('õ', 'o')
        .replace('ú', 'u')
        .replace('ç', 'c')
        .replace('-', ' ')
        .replace('  ', ' ')
    )

# Carregar dados básicos
try:
    # Tenta carregar apenas o JSON primeiro
    json_path = "data/processed/precos_por_distrito.json"
    
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        st.success("✅ Dados carregados com sucesso!")
        
        # Mostrar dados básicos
        st.subheader("📊 Dados Carregados")
        st.write(f"Total de distritos: {dados['total_distritos']}")
        st.write(f"Total de imóveis: {dados['total_imoveis_processados']}")
        st.write(f"Preço médio geral: R$ {dados['preco_medio_geral']:.2f}")
        
        # Tabela simples
        precos_df = pd.DataFrame.from_dict(dados['precos_por_distrito'], orient='index')
        precos_df = precos_df.reset_index().rename(columns={'index': 'distrito'})
        
        st.dataframe(precos_df)
        
    else:
        st.error(f"❌ Arquivo não encontrado: {json_path}")
        st.info("📁 Estrutura de arquivos atual:")
        for root, dirs, files in os.walk("."):
            st.write(f"Pasta: {root}")
            for file in files:
                st.write(f"  - {file}")

except Exception as e:
    st.error(f"❌ Erro ao carregar dados: {e}")
    import traceback
    st.code(traceback.format_exc())