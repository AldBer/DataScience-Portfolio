# 01-real-estate-sp/streamlit_app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

st.set_page_config(layout="wide", page_title="Dashboard Imóveis SP")

st.title("🏠 Dashboard de Imóveis em São Paulo")

def load_data_streamlit():
    """Carrega dados adaptado para Streamlit Cloud"""
    try:
        json_path = "./01-real-estate-sp/data/processed/precos_por_distrito.json"
        
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            st.success(f"✅ Dados carregados de: {json_path}")
            return dados
        else:
            st.error(f"❌ Arquivo não encontrado: {json_path}")
            return None
        
    except Exception as e:
        st.error(f"❌ Erro ao carregar dados: {e}")
        return None

def load_geojson_simplified():
    """Carrega apenas dados básicos do GeoJSON sem geopandas"""
    try:
        geojson_path = "./01-real-estate-sp/data/processed/sp_distritos_processado.geojson"
        
        if os.path.exists(geojson_path):
            with open(geojson_path, 'r', encoding='utf-8') as f:
                geojson_data = json.load(f)
            
            # Extrair apenas nomes dos distritos sem processamento espacial
            distritos = []
            for feature in geojson_data.get('features', []):
                props = feature.get('properties', {})
                distrito_nome = props.get('ds_nome', '')
                if distrito_nome:
                    distritos.append(distrito_nome)
            
            st.success(f"✅ {len(distritos)} distritos carregados do GeoJSON")
            return distritos
        else:
            st.warning("⚠️ GeoJSON não encontrado, usando dados básicos")
            return []
        
    except Exception as e:
        st.warning(f"⚠️ GeoJSON não carregado: {e}")
        return []

# Carregar dados
st.info("🔄 Carregando dados...")
dados_precos = load_data_streamlit()
distritos_geojson = load_geojson_simplified()

if dados_precos is None:
    st.error("❌ Falha ao carregar dados de preços")
    st.stop()

# Sidebar com verificações seguras
st.sidebar.header("📊 Informações do Dataset")

# ✅ USAR .get() PARA EVITAR KeyError
total_distritos = dados_precos.get('total_distritos', 0)
total_imoveis = dados_precos.get('total_imoveis_processados', 0)
preco_medio_geral = dados_precos.get('preco_medio_geral', 0)

st.sidebar.metric("Total de Distritos", total_distritos)
st.sidebar.metric("Imóveis Processados", total_imoveis)
st.sidebar.metric("Preço Médio Geral", f"R$ {preco_medio_geral:,.2f}")

# Verificar estrutura dos dados
if 'precos_por_distrito' not in dados_precos:
    st.error("❌ Chave 'precos_por_distrito' não encontrada")
    st.stop()

# Converter dados para DataFrame
precos_df = pd.DataFrame.from_dict(dados_precos['precos_por_distrito'], orient='index')
precos_df = precos_df.reset_index().rename(columns={'index': 'distrito'})

# Filtros
st.sidebar.header("🎛️ Filtros")
distritos_disponiveis = precos_df['distrito'].dropna().unique()
distritos_selecionados = st.sidebar.multiselect(
    "📍 Distritos",
    options=distritos_disponiveis,
    default=distritos_disponiveis[:3] if len(distritos_disponiveis) > 3 else distritos_disponiveis
)

# Aplicar filtros
if distritos_selecionados:
    filtered_df = precos_df[precos_df['distrito'].isin(distritos_selecionados)]
else:
    filtered_df = precos_df

# Métricas principais
st.subheader("📊 Métricas Principais")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Distritos com Dados", len(precos_df))

with col2:
    st.metric("Total de Imóveis", total_imoveis)

with col3:
    st.metric("Preço Médio Geral", f"R$ {preco_medio_geral:,.2f}")

with col4:
    ultima_atualizacao = dados_precos.get('ultima_atualizacao', 'N/A')
    st.metric("Última Atualização", str(ultima_atualizacao)[:10])

# Gráfico de barras - Top distritos por preço
st.subheader("📈 Preços Médios por Distrito")

if not filtered_df.empty:
    fig_bar = px.bar(
        filtered_df.sort_values('preco_medio', ascending=False),
        x='preco_medio',
        y='distrito',
        orientation='h',
        title="Distritos por Preço Médio",
        labels={'preco_medio': 'Preço Médio (R$)', 'distrito': 'Distrito'},
        color='preco_medio',
        color_continuous_scale='Viridis'
    )
    
    fig_bar.update_layout(
        height=500,
        yaxis={'categoryorder': 'total ascending'},
        xaxis_tickprefix='R$ '
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)
else:
    st.warning("⚠️ Nenhum dado encontrado com os filtros selecionados")

# Tabela de dados
st.subheader("📋 Dados Detalhados por Distrito")

# Formatar valores monetários
def format_currency(value):
    return f"R$ {value:,.2f}" if pd.notna(value) else "N/A"

precos_df_display = precos_df.copy()
precos_df_display['preco_medio'] = precos_df_display['preco_medio'].apply(format_currency)
precos_df_display['preco_minimo'] = precos_df_display.get('preco_minimo', 0).apply(format_currency)
precos_df_display['preco_maximo'] = precos_df_display.get('preco_maximo', 0).apply(format_currency)

st.dataframe(
    precos_df_display[
        ['distrito', 'preco_medio', 'quantidade_imoveis', 'preco_minimo', 'preco_maximo']
    ].rename(columns={
        'distrito': 'Distrito',
        'preco_medio': 'Preço Médio',
        'quantidade_imoveis': 'Qtd. Imóveis',
        'preco_minimo': 'Preço Mínimo',
        'preco_maximo': 'Preço Máximo'
    }),
    use_container_width=True,
    height=400
)

# Informações sobre cobertura
st.subheader("ℹ️ Informações de Cobertura")

col1, col2 = st.columns(2)

with col1:
    taxa_cobertura = (total_imoveis / 723 * 100) if total_imoveis > 0 else 0
    st.metric(
        "Taxa de Cobertura", 
        f"{taxa_cobertura:.1f}%",
        help="Percentual de imóveis que foram mapeados para distritos"
    )

with col2:
    st.metric(
        "Distritos Mapeados", 
        f"{total_distritos}/96",
        help="Distritos com dados vs total de distritos em SP"
    )

# Footer
st.markdown("---")
st.markdown(f"""
**📊 Sobre os dados:**
- Dados processados automaticamente do pipeline
- Preços calculados com base em imóveis mapeados para distritos
- Atualizado em: {ultima_atualizacao}
""")