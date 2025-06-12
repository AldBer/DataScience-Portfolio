import os
import pandas as pd
import pandas_ta as ta
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

# Configuração da página DEVE SER A PRIMEIRA CHAMADA
st.set_page_config(
    page_title="Dashboard Cripto",
    layout="wide",
    page_icon="📈"
)

# Configura caminhos
current_dir = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(current_dir, "..", "data"))

# Debug do caminho (agora depois da configuração da página)
st.sidebar.title("Debug Information")
st.sidebar.write(f"Script directory: {current_dir}")
st.sidebar.write(f"Data directory: {DATA_DIR}")

if os.path.exists(DATA_DIR):
    st.sidebar.write(f"Files in data directory: {os.listdir(DATA_DIR)}")
else:
    st.sidebar.error("Data directory does not exist!")

def analyze_crypto(symbol='BTC-USD', days=180):
    file_path = os.path.join(DATA_DIR, f'{symbol}.csv')
    
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo {file_path} não encontrado")
        
        temp_df = pd.read_csv(file_path)
        st.sidebar.write(f"Colunas em {symbol}.csv:", temp_df.columns.tolist())
        
        date_col = 'Date' if 'Date' in temp_df.columns else 'datetime'
        
        df = pd.read_csv(file_path, parse_dates=[date_col], index_col=date_col)
        df = df.last(f'{days}d')
        
        required_cols = ['Open', 'High', 'Low', 'Close']
        if not all(col in df.columns for col in required_cols):
            missing = [col for col in required_cols if col not in df.columns]
            raise ValueError(f"Colunas faltando: {missing}")
            
    except Exception as e:
        st.error(f"Erro ao carregar {symbol}: {str(e)}")
        return None

    # Calcula indicadores
    df['RSI'] = ta.rsi(df['Close'], length=14)
    macd = ta.macd(df['Close'])
    bbands = ta.bbands(df['Close'])

    # Cria figura
    fig = make_subplots(
        rows=3, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.05,
        row_heights=[0.6, 0.2, 0.2],
        subplot_titles=("Preço com Bollinger Bands", "RSI (14)", "MACD")
    )
    
    # Gráfico de preços
    fig.add_trace(go.Candlestick(
        x=df.index, open=df['Open'], high=df['High'],
        low=df['Low'], close=df['Close'], name=symbol
    ), row=1, col=1)
    
    # Bollinger Bands
    fig.add_trace(go.Scatter(
        x=df.index, y=bbands['BBU_5_2.0'], line=dict(color='royalblue', width=1),
        name='BB Upper', hoverinfo='skip'
    ), row=1, col=1)
    
    fig.add_trace(go.Scatter(
        x=df.index, y=bbands['BBL_5_2.0'], line=dict(color='firebrick', width=1),
        name='BB Lower', fill='tonexty', hoverinfo='skip'
    ), row=1, col=1)
    
    # RSI
    fig.add_trace(go.Scatter(
        x=df.index, y=df['RSI'], line=dict(color='purple'),
        name='RSI (14)'
    ), row=2, col=1)
    
    # MACD
    fig.add_trace(go.Scatter(
        x=df.index, y=macd['MACD_12_26_9'], line=dict(color='blue'),
        name='MACD'
    ), row=3, col=1)
    
    fig.add_trace(go.Scatter(
        x=df.index, y=macd['MACDs_12_26_9'], line=dict(color='orange'),
        name='Signal'
    ), row=3, col=1)
    
    # Layout
    fig.update_layout(
        title=f'Análise Técnica - {symbol}',
        hovermode="x unified",
        height=800,
        showlegend=False,
        xaxis_rangeslider_visible=False
    )
    
    # Linhas de referência
    fig.add_hline(y=30, row=2, col=1, line_dash="dot", line_color="red")
    fig.add_hline(y=70, row=2, col=1, line_dash="dot", line_color="green")
    fig.add_hline(y=0, row=3, col=1, line_dash="dot", line_color="gray")
    
    return fig

# Interface principal
st.title("Análise Técnica de Criptomoedas")

# Widgets
col1, col2 = st.columns([1, 3])
with col1:
    selected = st.selectbox(
        'Selecione o Ativo:',
        ['BTC-USD', 'ETH-USD', 'BNB-USD'],
        index=0
    )
    days = st.slider(
        'Período (dias):',
        min_value=30, max_value=365, value=180
    )

# Geração do gráfico
fig = analyze_crypto(selected, days)
if fig:
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Dados não disponíveis para o ativo selecionado")