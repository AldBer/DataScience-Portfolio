# test_streamlit.py - VERSÃO SIMPLES PARA TESTE
import streamlit as st
import pandas as pd

st.title("🏠 Teste Streamlit - Funcionando!")
st.success("✅ App carregado com sucesso!")

# Dados de exemplo
data = {
    'Distrito': ['Centro', 'Pinheiros', 'Moema', 'Vila Madalena'],
    'Preço Médio': [500000, 800000, 1200000, 950000],
    'Qtd Imóveis': [150, 200, 80, 120]
}

df = pd.DataFrame(data)
st.dataframe(df)

st.metric("Total de Distritos", len(df))
st.metric("Preço Médio Total", f"R$ {df['Preço Médio'].mean():,.2f}")