# app_housing/main.py - VERSÃO FINAL FUNCIONAL
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import json
import unicodedata
import re
from pathlib import Path

# ========== CONFIGURAÇÃO ==========
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data" / "processed"

st.set_page_config(layout="wide", page_title="Dashboard Imóveis SP", page_icon="🏠")
st.title("🏠 Dashboard de Imóveis em São Paulo")

# ========== FUNÇÕES ==========
def normalize_name(name):
    """Normaliza nomes removendo acentos e caracteres especiais"""
    if pd.isna(name):
        return ""
    name = unicodedata.normalize('NFKD', str(name))
    name = ''.join([c for c in name if not unicodedata.combining(c)])
    name = name.upper().strip()
    name = re.sub(r'[^\w\s]', '', name)  # Remove pontuação
    name = re.sub(r'\s+', ' ', name)     # Espaços múltiplos para um
    return name

@st.cache_data
def load_data():
    """Carrega todos os dados necessários"""
    results = {}
    
    # 1. Dados de preços
    precos_path = DATA_DIR / "precos_por_distrito.json"
    with open(precos_path, 'r', encoding='utf-8') as f:
        results['precos'] = json.load(f)
    
    # 2. GeoJSON
    geojson_path = DATA_DIR / "sp_distritos_fixed.geojson"  # Usar o arquivo encontrado
    with open(geojson_path, 'r', encoding='utf-8') as f:
        results['geojson'] = json.load(f)
    
    return results

# ========== CARREGAR DADOS ==========
data = load_data()

# Processar dados de preços
precos_dict = data['precos']['precos_por_distrito']
precos_df = pd.DataFrame.from_dict(precos_dict, orient='index').reset_index()
precos_df = precos_df.rename(columns={'index': 'distrito'})
precos_df['distrito_normalized'] = precos_df['distrito'].apply(normalize_name)

# Processar GeoJSON
geojson_data = data['geojson']
geojson_features = geojson_data['features']

# Criar DataFrame do GeoJSON
geojson_rows = []
for feature in geojson_features:
    props = feature['properties']
    geojson_rows.append({
        'ds_nome': props.get('ds_nome', ''),
        'ds_nome_normalized': normalize_name(props.get('ds_nome', ''))
    })
geojson_df = pd.DataFrame(geojson_rows)

# ========== ANÁLISE DE MATCHING ==========
matching_distritos = set(precos_df['distrito_normalized']).intersection(
    set(geojson_df['ds_nome_normalized'])
)

# ========== DASHBOARD ==========
st.success(f"""
✅ **Dashboard Carregado com Sucesso!**

**📊 Dados Disponíveis:**
- 🏙️ **{len(precos_df)} distritos** com dados de preços
- 🗺️ **{len(geojson_df)} distritos** no mapa
- 🔗 **{len(matching_distritos)} distritos** com dados no mapa
- 🏠 **{precos_df['quantidade_imoveis'].sum():,} imóveis** analisados
- 💰 **Preço médio: R$ {precos_df['preco_medio'].mean():.2f}**
""")

# ========== SIDEBAR ==========
st.sidebar.header("📊 Métricas Principais")
st.sidebar.metric("Distritos com Dados", len(precos_df))
st.sidebar.metric("Imóveis Analisados", f"{precos_df['quantidade_imoveis'].sum():,}")
st.sidebar.metric("Preço Médio", f"R$ {precos_df['preco_medio'].mean():.2f}")

st.sidebar.header("🎯 Distritos no Mapa")
st.sidebar.info(f"**{len(matching_distritos)}** de **{len(precos_df)}** distritos aparecem no mapa")

# ========== MAPA INTELIGENTE ==========
st.subheader("🗺️ Mapa Interativo de São Paulo")

if matching_distritos:
    # Criar dados para o mapa apenas com distritos que têm match
    map_data = []
    for feature in geojson_features:
        nome = feature['properties'].get('ds_nome', '')
        nome_norm = normalize_name(nome)
        
        if nome_norm in matching_distritos:
            # Encontrar dados do distrito
            distrito_data = precos_df[precos_df['distrito_normalized'] == nome_norm].iloc[0]
            map_data.append({
                'nome': nome,
                'nome_normalized': nome_norm,
                'preco_medio': distrito_data['preco_medio'],
                'quantidade_imoveis': distrito_data['quantidade_imoveis'],
                'preco_minimo': distrito_data['preco_minimo'],
                'preco_maximo': distrito_data['preco_maximo'],
                'geometry': feature['geometry']
            })
    
    # Criar DataFrame para o mapa
    map_df = pd.DataFrame(map_data)
    
    if not map_df.empty:
        # Criar figura do mapa
        fig = go.Figure()
        
        # Adicionar o mapa base
        fig.update_layout(
            mapbox_style="carto-positron",
            mapbox_zoom=9,
            mapbox_center={"lat": -23.5505, "lon": -46.6333},
            margin={"r":0,"t":0,"l":0,"b":0},
            height=500
        )
        
        # Adicionar cada distrito como um trace separado (para ter hover personalizado)
        for _, row in map_df.iterrows():
            fig.add_trace(go.Choroplethmapbox(
                geojson=row['geometry'],
                locations=[0],  # Dummy location
                z=[row['preco_medio']],
                colorscale="Viridis",
                marker_opacity=0.7,
                marker_line_width=1,
                marker_line_color='white',
                showscale=False,
                hoverinfo='text',
                text=f"""
                <b>{row['nome']}</b><br>
                Preço Médio: R$ {row['preco_medio']:.2f}<br>
                Imóveis: {row['quantidade_imoveis']}<br>
                Mínimo: R$ {row['preco_minimo']:.2f}<br>
                Máximo: R$ {row['preco_maximo']:.2f}
                """
            ))
        
        # Adicionar barra de cores
        fig.add_trace(go.Choroplethmapbox(
            geojson={"type": "FeatureCollection", "features": []},
            locations=[],
            z=[],
            colorscale="Viridis",
            showscale=True,
            colorbar=dict(
                title="Preço Médio (R$)",
                tickprefix="R$ "
            )
        ))
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Legenda dos distritos no mapa
        st.info(f"""
        **📍 Distritos visíveis no mapa ({len(map_df)}):**
        {', '.join(map_df['nome'].tolist())}
        
        **ℹ️ Nota:** Apenas distritos com dados disponíveis e correspondência geográfica são mostrados.
        """)
    else:
        st.warning("⚠️ Não foi possível criar o mapa com os dados disponíveis.")
else:
    st.info("""
    **ℹ️ Mapa Temporariamente Indisponível**
    
    Nenhum dos distritos com dados de preços foi encontrado no mapa geográfico.
    
    **Solução sugerida:**
    1. Verificar se os nomes dos distritos coincidem
    2. Atualizar o arquivo GeoJSON com mais distritos
    3. Usar a análise estatística abaixo
    """)

# ========== ANÁLISE ESTATÍSTICA ==========
st.subheader("📈 Análise Estatística dos Preços")

col1, col2 = st.columns(2)

with col1:
    # Top 10 mais caros
    top10 = precos_df.nlargest(10, 'preco_medio')
    fig1 = px.bar(
        top10,
        x='preco_medio',
        y='distrito',
        orientation='h',
        title="Top 10 Distritos Mais Caros",
        color='preco_medio',
        color_continuous_scale='Viridis',
        labels={'preco_medio': 'Preço Médio (R$)', 'distrito': 'Distrito'}
    )
    fig1.update_layout(height=400)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    # Distribuição de preços
    fig2 = px.histogram(
        precos_df,
        x='preco_medio',
        nbins=15,
        title="Distribuição de Preços Médios",
        color_discrete_sequence=['#636EFA'],
        labels={'preco_medio': 'Preço Médio (R$)', 'count': 'Número de Distritos'}
    )
    fig2.update_layout(height=400)
    st.plotly_chart(fig2, use_container_width=True)

# ========== TABELA INTERATIVA ==========
st.subheader("📋 Tabela de Dados Completa")

# Adicionar coluna indicando se está no mapa
precos_df['no_mapa'] = precos_df['distrito_normalized'].apply(
    lambda x: '✅' if x in matching_distritos else '❌'
)

# Formatar valores
display_df = precos_df.copy()
display_df['preco_medio'] = display_df['preco_medio'].apply(lambda x: f"R$ {x:,.2f}")
display_df['preco_minimo'] = display_df['preco_minimo'].apply(lambda x: f"R$ {x:,.2f}")
display_df['preco_maximo'] = display_df['preco_maximo'].apply(lambda x: f"R$ {x:,.2f}")

# Ordenar por preço
display_df = display_df.sort_values('preco_medio', ascending=False)

st.dataframe(
    display_df[['distrito', 'no_mapa', 'preco_medio', 'quantidade_imoveis', 'preco_minimo', 'preco_maximo']]
    .rename(columns={
        'distrito': 'Distrito',
        'no_mapa': 'No Mapa',
        'preco_medio': 'Preço Médio',
        'quantidade_imoveis': 'Qtd. Imóveis',
        'preco_minimo': 'Mínimo',
        'preco_maximo': 'Máximo'
    }),
    use_container_width=True,
    height=400
)

# ========== DISTRITOS FALTANTES ==========
with st.expander("🔍 Analisar Distritos Faltantes no Mapa"):
    distritos_sem_mapa = precos_df[precos_df['no_mapa'] == '❌']['distrito'].tolist()
    
    st.write(f"**{len(distritos_sem_mapa)} distritos com dados mas SEM mapa:**")
    for distrito in distritos_sem_mapa:
        st.write(f"- {distrito}")
    
    st.write("\n**Sugestões para correção:**")
    st.write("""
    1. **Verificar nomes alternativos** no GeoJSON
    2. **Procurar por abreviações** (ex: 'JD.' para 'JARDIM')
    3. **Verificar distritos vizinhos** que possam conter os dados
    4. **Atualizar o GeoJSON** com mais distritos
    """)

# ========== RESUMO EXECUTIVO ==========
st.subheader("📊 Resumo Executivo")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Preço Mais Alto", 
              f"R$ {precos_df['preco_medio'].max():.2f}",
              precos_df.loc[precos_df['preco_medio'].idxmax(), 'distrito'])

with col2:
    st.metric("Preço Mais Baixo", 
              f"R$ {precos_df['preco_medio'].min():.2f}",
              precos_df.loc[precos_df['preco_medio'].idxmin(), 'distrito'])

with col3:
    st.metric("Maior Amostra", 
              f"{precos_df['quantidade_imoveis'].max()} imóveis",
              precos_df.loc[precos_df['quantidade_imoveis'].idxmax(), 'distrito'])

# ========== FOOTER ==========
st.markdown("---")
st.markdown(f"""
**📝 Relatório Técnico:**
- **Distritos analisados:** {len(precos_df)} de 96 distritos de SP
- **Imóveis totais:** {precos_df['quantidade_imoveis'].sum():,}
- **Cobertura geográfica:** {len(matching_distritos)} distritos ({len(matching_distritos)/len(precos_df)*100:.1f}%)
- **Preço médio geral:** R$ {precos_df['preco_medio'].mean():.2f}
- **Variação de preços:** R$ {precos_df['preco_medio'].min():.2f} a R$ {precos_df['preco_medio'].max():.2f}

**🛠️ Stack Tecnológico:** Streamlit • Plotly • Pandas • GeoJSON
**📅 Dados atualizados em:** {data['precos'].get('ultima_atualizacao', 'N/A')}
""")