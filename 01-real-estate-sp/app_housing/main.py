import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import geopandas as gpd
import json
import unicodedata
import re

# Configuração inicial
st.set_page_config(layout="wide", page_title="Dashboard Imóveis SP")

# Título
st.title("🏠 Dashboard de Imóveis em São Paulo")

def normalize_name(name):
    """
    Normaliza nomes removendo acentos, convertendo para maiúsculas e limpando caracteres especiais
    """
    if pd.isna(name):
        return ""
    
    # Remove acentos
    name = unicodedata.normalize('NFKD', str(name))
    name = ''.join([c for c in name if not unicodedata.combining(c)])
    
    # Converte para maiúsculas e remove espaços extras
    name = name.upper().strip()
    
    # Remove caracteres especiais e múltiplos espaços
    name = re.sub(r'[^\w\s]', '', name)
    name = re.sub(r'\s+', ' ', name)
    
    return name

def create_district_mapping():
    """
    Cria mapeamento manual entre bairros do CSV e distritos do GeoJSON
    Baseado no conhecimento de São Paulo
    """
    mapping = {
        # Bairros CSV -> Distritos Oficiais GeoJSON
        'ITAIM BIBI': 'ITAIM BIBI',
        'JARDINS': 'JARDIM PAULISTA',  # Jardins faz parte do distrito Jardim Paulista
        'LAPA': 'LAPA',
        'MOEMA': 'MOEMA', 
        'MORUMBI': 'VILA ANDRADE',  # Morumbi faz parte de Vila Andrade
        'VILA MADALENA': 'PINHEIROS',  # Vila Madalena faz parte do distrito Pinheiros
        'PINHEIROS': 'PINHEIROS',
        'BROOKLIN': 'BROOKLIN PAULISTA',
        'CAMPO BELO': 'CAMPO BELO',
        'VILA OLIMPIA': 'VILA OLIMPIA',
        'CHACARA SANTO ANTONIO': 'CHACARA SANTO ANTONIO',
        'SANTANA': 'SANTANA',
        'TATUAPE': 'TATUAPE',
        'PENHA': 'PENHA',
        'IPIRANGA': 'IPIRANGA',
        'SAUDE': 'SAUDE',
        'LIBERDADE': 'LIBERDADE',
        'BELA VISTA': 'BELA VISTA',
        'CONSOLACAO': 'CONSOLACAO',
        'HIGIENOPOLIS': 'SANTA CECILIA',  # Higienópolis faz parte de Santa Cecília
        'PACAEMBU': 'PERDIZES',  # Pacaembu faz parte de Perdizes
        'VILA NOVA CONCEICAO': 'MOEMA',  # Vila Nova Conceição faz parte de Moema
        'CAMPO GRANDE': 'CAMPO GRANDE',
        'SANTO AMARO': 'SANTO AMARO',
        'JARDIM EUROPA': 'JARDIM PAULISTA',
        'JARDIM AMERICA': 'JARDIM PAULISTA',
        'CIDADE JARDIM': 'PINHEIROS',
        'BUTANTA': 'BUTANTA',
        'VILA LEOPOLDINA': 'VILA LEOPOLDINA',
        'AGUA BRANCA': 'BARRA FUNDA',  # Água Branca faz parte de Barra Funda
        'PERDIZES': 'PERDIZES',
        'SUMARE': 'SUMARE',
        'VILA POMPEIA': 'POMPEIA',
        'POMPEIA': 'POMPEIA'
    }
    
    return mapping

def apply_district_mapping(df, mapping):
    """
    Aplica o mapeamento de bairros para distritos oficiais
    """
    df = df.copy()
    
    # Normaliza os nomes dos bairros
    df['bairro_normalized'] = df['bairro'].apply(normalize_name)
    
    # Aplica o mapeamento
    df['distrito_oficial'] = df['bairro_normalized'].map(mapping)
    
    # Para bairros não mapeados, tenta usar o nome original normalizado
    mask_not_mapped = df['distrito_oficial'].isna()
    df.loc[mask_not_mapped, 'distrito_oficial'] = df.loc[mask_not_mapped, 'bairro_normalized']
    
    return df

# Carregar dados
@st.cache_data
def load_data():
    """Carrega dados de propriedades e geodados"""
    try:
        properties = pd.read_csv (r"../data/raw/sp_properties_sample.csv")
        geodata = gpd.read_file(r"../data/processed/sp_distritos_processado.geojson")
        
        # Normaliza os nomes dos distritos no geodata
        geodata['ds_nome_normalized'] = geodata['ds_nome'].apply(normalize_name)
        
        return properties, geodata
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return None, None

# Carregar dados
df, geo_df = load_data()

if df is None or geo_df is None:
    st.stop()

# Aplicar mapeamento de distritos
district_mapping = create_district_mapping()
df = apply_district_mapping(df, district_mapping)

# Debug das conversões
with st.expander("🔍 Debug: Mapeamento de Distritos"):
    st.subheader("Conversões Aplicadas:")
    
    mapping_df = pd.DataFrame([
        {"Bairro Original": bairro, "Distrito Mapeado": distrito}
        for bairro, distrito in district_mapping.items()
    ])
    st.dataframe(mapping_df, use_container_width=True)
    
    # Estatísticas do mapeamento
    mapped_count = df['distrito_oficial'].isin(geo_df['ds_nome_normalized']).sum()
    total_count = len(df)
    
    st.metric("🎯 Taxa de Mapeamento", f"{mapped_count}/{total_count} ({mapped_count/total_count*100:.1f}%)")
    
    # Distritos não encontrados
    unmapped = df[~df['distrito_oficial'].isin(geo_df['ds_nome_normalized'])]['distrito_oficial'].unique()
    if len(unmapped) > 0:
        st.warning(f"⚠️ Distritos não encontrados no GeoJSON: {', '.join(unmapped[:5])}")

# Filtros na sidebar
st.sidebar.header("🎛️ Filtros")

# Filtro de bairros (usando os nomes originais)
bairros = sorted(df['bairro'].unique())
selected_bairros = st.sidebar.multiselect(
    "📍 Selecionar Bairros", 
    bairros, 
    default=bairros[:5] if len(bairros) > 5 else bairros
)

# Filtros de preço
price_range = st.sidebar.slider(
    "💰 Faixa de Preços (R$)", 
    int(df['preco'].min()), 
    int(df['preco'].max()),
    (int(df['preco'].min()), int(df['preco'].max())),
    step=10000
)

# Filtro de quartos
quartos = sorted(df['quartos'].unique())
selected_quartos = st.sidebar.multiselect(
    "🛏️ Número de Quartos", 
    quartos, 
    default=quartos
)

# Aplicar filtros
filtered_df = df[
    (df['bairro'].isin(selected_bairros)) &
    (df['preco'] >= price_range[0]) &
    (df['preco'] <= price_range[1]) &
    (df['quartos'].isin(selected_quartos))
]

if filtered_df.empty:
    st.warning("⚠️ Nenhum imóvel encontrado com os filtros selecionados!")
    st.stop()

# Métricas resumidas
st.subheader("📊 Métricas Principais")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🏘️ Total de Imóveis", 
        f"{len(filtered_df):,}",
        delta=f"{len(filtered_df) - len(df):,} vs total"
    )

with col2:
    avg_price = filtered_df['preco'].mean()
    st.metric(
        "💰 Preço Médio", 
        f"R$ {avg_price:,.0f}",
        delta=f"{((avg_price / df['preco'].mean()) - 1) * 100:+.1f}%"
    )

with col3:
    avg_area = filtered_df['area_m2'].mean()
    st.metric(
        "📏 Área Média", 
        f"{avg_area:.1f}m²",
        delta=f"{((avg_area / df['area_m2'].mean()) - 1) * 100:+.1f}%"
    )

# Preparar dados para o mapa
st.subheader("🗺️ Distribuição Geográfica de Preços")

try:
    # Calcular preço médio por distrito oficial (mapeado)
    price_by_district = filtered_df.groupby('distrito_oficial').agg({
        'preco': ['mean', 'count'],
        'area_m2': 'mean',
        'bairro': lambda x: ', '.join(x.unique()[:3])  # Mostra até 3 bairros por distrito
    }).round(2)
    
    # Achatar as colunas multi-level
    price_by_district.columns = ['preco_medio', 'qtd_imoveis', 'area_media', 'bairros_inclusos']
    price_by_district = price_by_district.reset_index()
    
    # Fazer merge com geodados usando nomes normalizados
    geo_merged = geo_df.merge(
        price_by_district,
        left_on='ds_nome_normalized',  # coluna normalizada do geodata
        right_on='distrito_oficial',   # coluna mapeada dos dados de preço
        how='left'
    )
    
    # Verificar se o merge funcionou
    merged_count = geo_merged['preco_medio'].notna().sum()
    st.success(f"✅ Merge realizado com sucesso: {merged_count}/{len(geo_df)} distritos com dados")
    
    if merged_count > 0:
        # Criar mapa coroplético
        geo_merged_valid = geo_merged[geo_merged['preco_medio'].notna()].copy()
        
        fig_map = px.choropleth_mapbox(
            geo_merged_valid,
            geojson=json.loads(geo_merged_valid.to_json()),
            locations=geo_merged_valid.index,
            color='preco_medio',
            hover_name='ds_nome',
            hover_data={
                'preco_medio': ':,.0f',
                'qtd_imoveis': ':,',
                'area_media': ':.1f',
                'bairros_inclusos': True
            },
            color_continuous_scale='Viridis',
            mapbox_style="carto-positron",
            center={"lat": -23.5505, "lon": -46.6333},
            zoom=9.5,
            opacity=0.8,
            labels={
                'preco_medio': 'Preço Médio (R$)',
                'qtd_imoveis': 'Qtd Imóveis',
                'area_media': 'Área Média (m²)',
                'bairros_inclusos': 'Bairros'
            }
        )
        
        fig_map.update_layout(
            height=650,
            margin={"r":0,"t":30,"l":0,"b":0},
            coloraxis_colorbar=dict(
                title="Preço Médio (R$)",
                tickformat=".0f"
            )
        )
        
        st.plotly_chart(fig_map, use_container_width=True)
    else:
        st.error("❌ Não foi possível criar o mapa. Verifique o mapeamento dos distritos.")

except Exception as e:
    st.error(f"❌ Erro ao criar mapa: {str(e)}")

# Visualização 2: Gráfico de Barras (Top 10 Bairros)
st.subheader("📈 Top 10 Bairros - Preço Médio")

top_districts = filtered_df.groupby('bairro')['preco'].mean().sort_values(ascending=False).head(10)

fig_bar = px.bar(
    x=top_districts.values,
    y=top_districts.index,
    orientation='h',
    labels={'x': 'Preço Médio (R$)', 'y': 'Bairro'},
    color=top_districts.values,
    color_continuous_scale='Reds',
    title="Bairros com Maiores Preços Médios"
)

fig_bar.update_layout(
    height=450,
    yaxis={'categoryorder': 'total ascending'},
    showlegend=False,
    xaxis_tickformat='.0f'
)

st.plotly_chart(fig_bar, use_container_width=True)

# Visualização 3: Análise por Número de Quartos
st.subheader("🛏️ Distribuição de Preços por Quartos")

col1, col2 = st.columns(2)

with col1:
    # Box plot por quartos
    fig_box = px.box(
        filtered_df, 
        x='quartos', 
        y='preco',
        title="Distribuição de Preços por Número de Quartos",
        labels={'preco': 'Preço (R$)', 'quartos': 'Número de Quartos'}
    )
    fig_box.update_layout(height=400)
    st.plotly_chart(fig_box, use_container_width=True)

with col2:
    # Scatter plot área vs preço
    fig_scatter = px.scatter(
        filtered_df, 
        x='area_m2', 
        y='preco',
        color='quartos',
        size='area_m2',
        hover_data=['bairro'],
        title="Relação Área vs Preço",
        labels={'area_m2': 'Área (m²)', 'preco': 'Preço (R$)'}
    )
    fig_scatter.update_layout(height=400)
    st.plotly_chart(fig_scatter, use_container_width=True)

# Tabela resumo por distrito
st.subheader("📋 Resumo por Distrito Oficial")

if merged_count > 0:
    summary_table = filtered_df.groupby(['distrito_oficial', 'bairro']).agg({
        'preco': ['mean', 'min', 'max', 'count'],
        'area_m2': 'mean',
        'quartos': 'mean'
    }).round(2)
    
    # Renomear colunas
    summary_table.columns = [
        'Preço Médio', 'Preço Min', 'Preço Max', 
        'Qtd Imóveis', 'Área Média', 'Quartos Médio'
    ]
    
    summary_table = summary_table.sort_values('Preço Médio', ascending=False).head(20)
    
    # Formatar valores monetários
    for col in ['Preço Médio', 'Preço Min', 'Preço Max']:
        summary_table[col] = summary_table[col].apply(lambda x: f"R$ {x:,.0f}")
    
    st.dataframe(summary_table, use_container_width=True)

# Footer com informações
st.markdown("---")
st.markdown("📊 **Dashboard desenvolvido com Streamlit & Plotly** | 🏠 Dados do mercado imobiliário de São Paulo | 🗺️ Mapeamento automático de distritos")