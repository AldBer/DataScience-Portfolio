"""
Componentes reutilizáveis para o dashboard Streamlit
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_metric_cards(stats_dict):
    """
    Cria cards de métricas principais
    
    Args:
        stats_dict (dict): Dicionário com estatísticas
    """
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="💰 Preço Médio/m²",
            value=f"R$ {stats_dict.get('mean', 0):,.0f}",
            delta=None
        )
    
    with col2:
        st.metric(
            label="📊 Mediana/m²", 
            value=f"R$ {stats_dict.get('median', 0):,.0f}",
            delta=None
        )
    
    with col3:
        st.metric(
            label="📈 Valor Máximo/m²",
            value=f"R$ {stats_dict.get('max', 0):,.0f}",
            delta=None
        )
    
    with col4:
        st.metric(
            label="📉 Valor Mínimo/m²",
            value=f"R$ {stats_dict.get('min', 0):,.0f}",
            delta=None
        )

def create_district_map(gdf, price_column="price_per_m2"):
    """
    Cria mapa coroplético dos distritos
    
    Args:
        gdf (GeoDataFrame): Dados geoespaciais
        price_column (str): Coluna com preços
    
    Returns:
        plotly.graph_objects.Figure: Figura do mapa
    """
    fig = px.choropleth_mapbox(
        gdf,
        geojson=gdf.geometry,
        locations=gdf.index,
        color=price_column,
        hover_name="district" if "district" in gdf.columns else gdf.index,
        hover_data={price_column: ":,.0f"},
        color_continuous_scale="Viridis",
        mapbox_style="carto-positron",
        zoom=9,
        center={"lat": -23.5505, "lon": -46.6333},  # São Paulo coordinates
        opacity=0.7,
        title="📍 Preços por Distrito - São Paulo"
    )
    
    fig.update_layout(
        height=600,
        margin={"r":0,"t":30,"l":0,"b":0}
    )
    
    return fig

def create_price_distribution(df, price_column="price_per_m2"):
    """
    Cria gráfico de distribuição de preços
    
    Args:
        df (DataFrame): Dados com preços
        price_column (str): Coluna com preços
    
    Returns:
        plotly.graph_objects.Figure: Figura do histograma
    """
    fig = px.histogram(
        df,
        x=price_column,
        nbins=30,
        title="📊 Distribuição de Preços por m²",
        labels={price_column: "Preço por m² (R$)", "count": "Frequência"},
        color_discrete_sequence=["#1f77b4"]
    )
    
    fig.update_layout(
        height=400,
        showlegend=False
    )
    
    return fig

def create_top_districts_chart(df, top_n=10):
    """
    Cria gráfico dos top distritos por preço
    
    Args:
        df (DataFrame): Dados com distritos e preços
        top_n (int): Número de top distritos
    
    Returns:
        plotly.graph_objects.Figure: Figura do gráfico de barras
    """
    if "district" not in df.columns or "price_per_m2" not in df.columns:
        return go.Figure()
    
    top_districts = df.nlargest(top_n, "price_per_m2")
    
    fig = px.bar(
        top_districts,
        x="price_per_m2", 
        y="district",
        orientation="h",
        title=f"🏆 Top {top_n} Distritos Mais Caros",
        labels={"price_per_m2": "Preço por m² (R$)", "district": "Distrito"},
        color="price_per_m2",
        color_continuous_scale="Reds"
    )
    
    fig.update_layout(
        height=400,
        yaxis={"categoryorder": "total ascending"}
    )
    
    return fig

def sidebar_filters(df):
    """
    Cria filtros na sidebar
    
    Args:
        df (DataFrame): DataFrame para criar filtros
    
    Returns:
        dict: Dicionário com filtros selecionados
    """
    st.sidebar.header("🎛️ Filtros")
    
    filters = {}
    
    # Filtro de preço
    if "price_per_m2" in df.columns:
        price_min = float(df["price_per_m2"].min())
        price_max = float(df["price_per_m2"].max())
        
        filters["price_range"] = st.sidebar.slider(
            "💰 Faixa de Preço (R$/m²)",
            min_value=price_min,
            max_value=price_max,
            value=(price_min, price_max),
            step=100.0
        )
    
    # Filtro de distrito (se disponível)
    if "district" in df.columns:
        districts = ["Todos"] + sorted(df["district"].unique().tolist())
        filters["selected_district"] = st.sidebar.selectbox(
            "📍 Selecionar Distrito",
            districts
        )
    
    return filters
