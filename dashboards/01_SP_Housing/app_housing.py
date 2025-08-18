import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd

# Configuração inicial
st.set_page_config(layout="wide")

# Título
st.title("Dashboard de Imóveis em São Paulo")

# Carregar dados
@st.cache_data
def load_data():
    properties = pd.read_csv("F:/Documents/04. Cursos/17.Python/05.Portfolio/dashboards/01_sp_housing/data/raw/sp_properties_sample.csv")
    geodata = gpd.read_file("F:/Documents/04. Cursos/17.Python/05.Portfolio/dashboards/01_sp_housing/data/processed/sp_distritos_processado.geojson")
    return properties, geodata

df, geo_df = load_data()

# Filtros na sidebar
st.sidebar.header("Filtros")
bairros = sorted(df['bairro'].unique())
selected_bairros = st.sidebar.multiselect("Bairros", bairros, default=bairros[:3])

min_price = st.sidebar.slider("Preço mínimo (R$)", 
                             int(df['preco'].min()), 
                             int(df['preco'].max()),
                             int(df['preco'].min()))

max_price = st.sidebar.slider("Preço máximo (R$)", 
                             int(df['preco'].min()), 
                             int(df['preco'].max()),
                             int(df['preco'].max()))

quartos = sorted(df['quartos'].unique())
selected_quartos = st.sidebar.multiselect("Quartos", quartos, default=quartos)

# Aplicar filtros
filtered_df = df[
    (df['bairro'].isin(selected_bairros)) &
    (df['preco'] >= min_price) &
    (df['preco'] <= max_price) &
    (df['quartos'].isin(selected_quartos))
]

# Métricas resumidas
col1, col2, col3 = st.columns(3)
col1.metric("Total de Imóveis", len(filtered_df))
col2.metric("Preço Médio", f"R${filtered_df['preco'].mean():,.2f}")
col3.metric("Área Média", f"{filtered_df['area_m2'].mean():.1f}m²")

# Visualização 1: Mapa de Calor por Distrito
st.subheader("Distribuição Geográfica de Preços")

# Corrigindo o merge - usando ds_nome em vez de ds_name
# Primeiro precisamos garantir que estamos usando a coluna correta para o merge
# Como os bairros em filtered_df estão em 'bairro' e em geo_df em 'ds_nome',
# precisamos verificar se os nomes são compatíveis

# Opção 1: Se os nomes são compatíveis (mesmo formato)
try:
    geo_merged = geo_df.merge(
        filtered_df.groupby('bairro')['preco'].mean().reset_index(), 
        left_on='ds_nome', 
        right_on='bairro',
        how='left'
    )
    
    fig_map = px.choropleth_mapbox(
        geo_merged,
        geojson=geo_merged.geometry,
        locations=geo_merged.index,
        color='preco',
        hover_name='ds_nome',  # Usando ds_nome para hover
        mapbox_style="carto-positron",
        center={"lat": -23.5505, "lon": -46.6333},
        zoom=10,
        opacity=0.5,
        labels={'preco': 'Preço Médio (R$)'}
    )
    st.plotly_chart(fig_map, use_container_width=True)
    
except Exception as e:
    st.error(f"Erro ao criar mapa: {str(e)}")
    st.write("Dados disponíveis em filtered_df:", filtered_df['bairro'].unique()[:10])
    st.write("Dados disponíveis em geo_df:", geo_df['ds_nome'].unique()[:10])

# Visualização 2: Gráfico de Barras (Preço Médio por Bairro)
st.subheader("Preço Médio por Bairro")
mean_price_by_district = filtered_df.groupby('bairro')['preco'].mean().sort_values(ascending=False)
fig_bar = px.bar(
    mean_price_by_district.reset_index(),
    x='bairro',
    y='preco',
    labels={'preco': 'Preço Médio (R$)', 'bairro': 'Bairro'}
)
st.plotly_chart(fig_bar, use_container_width=True)

# Visualização 3: Volume por Região
st.subheader("Volume de Imóveis por Região")
count_by_district = filtered_df['bairro'].value_counts().reset_index()
count_by_district.columns = ['bairro', 'count']
fig_count = px.pie(
    count_by_district,
    names='bairro',
    values='count',
    title="Distribuição por Bairro"
)
st.plotly_chart(fig_count, use_container_width=True)