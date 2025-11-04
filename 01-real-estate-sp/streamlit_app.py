# 01-real-estate-sp/streamlit_app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
import json
import os
from pathlib import Path

st.set_page_config(layout="wide", page_title="Dashboard Imóveis SP")

st.title("🏠 Dashboard de Imóveis em São Paulo")

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

def load_data_streamlit():
    """Carrega dados adaptado para Streamlit Cloud"""
    try:
        json_path = "./01-real-estate-sp/data/processed/precos_por_distrito.json"
        
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            st.success(f"✅ Dados carregados de: {json_path}")
            
            # 🔍 DEBUG: Mostrar estrutura dos dados
            st.write("🔍 Estrutura dos dados carregados:")
            st.json(dados)  # Mostra o JSON completo
            
            return dados
        else:
            st.error(f"❌ Arquivo não encontrado: {json_path}")
            return None
        
    except Exception as e:
        st.error(f"❌ Erro ao carregar dados: {e}")
        return None

def load_geojson_streamlit():
    """Carrega GeoJSON adaptado para Streamlit Cloud"""
    try:
        geojson_path = "./01-real-estate-sp/data/processed/sp_distritos_processado.geojson"
        
        if os.path.exists(geojson_path):
            geodata = gpd.read_file(geojson_path)
            st.success(f"✅ GeoJSON carregado de: {geojson_path}")
            
            # 🔍 DEBUG: Mostrar estrutura do GeoJSON
            st.write("🔍 Primeiras linhas do GeoJSON:")
            st.write(geodata.head())
            
            return geodata
        else:
            st.error(f"❌ Arquivo não encontrado: {geojson_path}")
            return None
        
    except Exception as e:
        st.error(f"❌ Erro ao carregar GeoJSON: {e}")
        return None

# Carregar dados
st.info("🔄 Carregando dados...")
dados_precos = load_data_streamlit()
geo_df = load_geojson_streamlit()

# ⚠️ VERIFICAÇÃO SEGURA DOS DADOS
if dados_precos is None or geo_df is None:
    st.error("❌ Falha ao carregar dados necessários")
    st.stop()

# 🔍 VERIFICAR ESTRUTURA ANTES DE USAR
st.subheader("🔍 Verificação da Estrutura de Dados")

# Verificar se as chaves esperadas existem
chaves_esperadas = ['total_imoveis_processados', 'total_distritos', 'preco_medio_geral', 'precos_por_distrito']
chaves_encontradas = list(dados_precos.keys())

st.write(f"Chaves esperadas: {chaves_esperadas}")
st.write(f"Chaves encontradas: {chaves_encontradas}")

# Verificar cada chave individualmente
for chave in chaves_esperadas:
    if chave in dados_precos:
        st.success(f"✅ '{chave}': {dados_precos[chave]}")
    else:
        st.error(f"❌ Chave '{chave}' não encontrada")

# ⚠️ SÓ CONTINUA SE AS CHAVES PRINCIPAIS EXISTIREM
if 'precos_por_distrito' not in dados_precos:
    st.error("❌ Chave 'precos_por_distrito' não encontrada. Estrutura do JSON diferente do esperado.")
    st.stop()

# Sidebar com verificações seguras
st.sidebar.header("📊 Informações do Dataset")

# ✅ USAR .get() PARA EVITAR KeyError
st.sidebar.metric(
    "Total de Distritos", 
    dados_precos.get('total_distritos', 'N/A')
)
st.sidebar.metric(
    "Imóveis Processados", 
    dados_precos.get('total_imoveis_processados', 'N/A')
)
st.sidebar.metric(
    "Preço Médio Geral", 
    f"R$ {dados_precos.get('preco_medio_geral', 0):.2f}"
)

# Resto do código com verificações seguras...
try:
    # Converter dados do JSON para DataFrame
    precos_df = pd.DataFrame.from_dict(dados_precos['precos_por_distrito'], orient='index')
    precos_df = precos_df.reset_index().rename(columns={'index': 'distrito'})
    
    st.success("✅ Dados convertidos para DataFrame")
    st.dataframe(precos_df)
    
except Exception as e:
    st.error(f"❌ Erro ao converter dados: {e}")
    st.stop()

# Normalizar nomes dos distritos para matching
precos_df['distrito_normalized'] = precos_df['distrito'].apply(normalize_name)
geo_df['ds_nome_normalized'] = geo_df['ds_nome'].apply(normalize_name)

# Debug: Mostrar os distritos disponíveis
with st.expander("🔍 Debug - Distritos Disponíveis"):
    st.write("Distritos nos dados de preço:", precos_df['distrito'].tolist())
    st.write("Distritos no GeoJSON:", geo_df['ds_nome_normalized'].tolist())

# Fazer merge entre GeoJSON e dados de preços
geo_merged = geo_df.merge(
    precos_df,
    left_on='ds_nome_normalized',
    right_on='distrito_normalized',
    how='left'
)

# Sidebar com informações
st.sidebar.header("📊 Informações do Dataset")
st.sidebar.metric("Total de Distritos", dados_precos['total_distritos'])
st.sidebar.metric("Imóveis Processados", dados_precos['total_imoveis_processados'])
st.sidebar.metric("Preço Médio Geral", f"R$ {dados_precos['preco_medio_geral']:.2f}")

# Filtros
st.sidebar.header("🎛️ Filtros")

# Filtro de distritos
distritos_disponiveis = precos_df['distrito'].dropna().unique()
distritos_selecionados = st.sidebar.multiselect(
    "📍 Distritos",
    options=distritos_disponiveis,
    default=distritos_disponiveis[:5] if len(distritos_disponiveis) > 5 else distritos_disponiveis
)

# Filtro de faixa de preço
if not precos_df.empty:
    min_price = precos_df['preco_medio'].min()
    max_price = precos_df['preco_medio'].max()
    
    price_range = st.sidebar.slider(
        "💰 Faixa de Preço Médio (R$)",
        min_value=float(min_price),
        max_value=float(max_price),
        value=(float(min_price), float(max_price))
    )

# Aplicar filtros
if distritos_selecionados:
    filtered_geo = geo_merged[geo_merged['distrito'].isin(distritos_selecionados)]
else:
    filtered_geo = geo_merged

filtered_geo = filtered_geo[
    (filtered_geo['preco_medio'] >= price_range[0]) & 
    (filtered_geo['preco_medio'] <= price_range[1])
]

# Métricas principais
st.subheader("📊 Métricas Principais")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Distritos com Dados", len(precos_df))

with col2:
    st.metric("Total de Imóveis", dados_precos['total_imoveis_processados'])

with col3:
    st.metric("Preço Médio Geral", f"R$ {dados_precos['preco_medio_geral']:.2f}")

with col4:
    st.metric("Última Atualização", pd.to_datetime(dados_precos['ultima_atualizacao']).strftime('%d/%m/%Y'))

# Mapa Coroplético
st.subheader("🗺️ Mapa de Preços por Distrito")

if not filtered_geo.empty and not filtered_geo['preco_medio'].isna().all():
    # Criar mapa coroplético
    fig = px.choropleth_mapbox(
        filtered_geo,
        geojson=filtered_geo.geometry.__geo_interface__,
        locations=filtered_geo.index,
        color='preco_medio',
        hover_name='ds_nome',
        hover_data={
            'preco_medio': ':.2f',
            'quantidade_imoveis': True,
            'preco_minimo': ':.2f',
            'preco_maximo': ':.2f'
        },
        color_continuous_scale='Viridis',
        mapbox_style="carto-positron",
        center={"lat": -23.5505, "lon": -46.6333},
        zoom=9,
        opacity=0.7,
        labels={
            'preco_medio': 'Preço Médio (R$)',
            'quantidade_imoveis': 'Qtd. Imóveis',
            'preco_minimo': 'Preço Mínimo',
            'preco_maximo': 'Preço Máximo'
        }
    )
    
    fig.update_layout(
        height=600,
        margin={"r":0,"t":0,"l":0,"b":0},
        coloraxis_colorbar=dict(
            title="Preço Médio (R$)",
            tickprefix="R$ "
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("⚠️ Nenhum dado encontrado com os filtros selecionados ou dados incompletos.")

# Tabela de dados
st.subheader("📋 Dados Detalhados por Distrito")

# Ordenar por preço médio
precos_df_sorted = precos_df.sort_values('preco_medio', ascending=False)

# Formatar valores monetários
def format_currency(value):
    return f"R$ {value:,.2f}" if pd.notna(value) else "N/A"

precos_df_display = precos_df_sorted.copy()
precos_df_display['preco_medio'] = precos_df_display['preco_medio'].apply(format_currency)
precos_df_display['preco_minimo'] = precos_df_display['preco_minimo'].apply(format_currency)
precos_df_display['preco_maximo'] = precos_df_display['preco_maximo'].apply(format_currency)

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

# Gráfico de barras - Top 10 distritos por preço
st.subheader("📈 Top 10 Distritos por Preço Médio")

top_10 = precos_df_sorted.head(10)

fig_bar = px.bar(
    top_10,
    x='preco_medio',
    y='distrito',
    orientation='h',
    title="Distritos com Maiores Preços Médios",
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

# Informações sobre cobertura
st.subheader("ℹ️ Informações de Cobertura")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Taxa de Cobertura", 
        f"{(dados_precos['total_imoveis_processados'] / 723 * 100):.1f}%",
        help="Percentual de imóveis que foram mapeados para distritos"
    )

with col2:
    st.metric(
        "Distritos Mapeados", 
        f"{dados_precos['total_distritos']}/96",
        help="Distritos com dados vs total de distritos em SP"
    )

# Footer
st.markdown("---")
st.markdown("""
**📊 Sobre os dados:**
- Dados processados automaticamente do pipeline
- Preços calculados com base em imóveis mapeados para distritos
- Atualizado em: {}
""".format(pd.to_datetime(dados_precos['ultima_atualizacao']).strftime('%d/%m/%Y %H:%M')))

# Botão para atualizar dados
if st.button("🔄 Executar Pipeline de Atualização"):
    with st.spinner("Executando pipeline de atualização..."):
        try:
            import subprocess
            # Caminho correto para o script
            script_path = Path(__file__).parent / "scripts" / "atualizar_precos.py"
            result = subprocess.run(
                ["python", str(script_path)], 
                capture_output=True, 
                text=True,
                cwd=Path(__file__).parent
            )
            
            if result.returncode == 0:
                st.success("✅ Pipeline executado com sucesso!")
                st.info("Recarregue a página para ver os dados atualizados.")
            else:
                st.error(f"❌ Erro no pipeline: {result.stderr}")
                
        except Exception as e:
            st.error(f"❌ Erro ao executar pipeline: {e}")