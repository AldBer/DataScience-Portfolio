import streamlit as st
import pandas as pd
import ccxt

# Configuração inicial
st.set_page_config(layout="wide", page_title="Análise Cripto")
exchange = ccxt.binance()

def fetch_crypto_data(symbol='BTC/USDT', timeframe='1d', limit=100):
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except Exception as e:
        st.error(f"Erro ao buscar dados: {e}")
        return pd.DataFrame()

# Interface
st.title('📊 Análise de Criptoativos')
pair = st.selectbox('Selecione o par:', ['BTC/USDT', 'ETH/USDT', 'SOL/USDT'])

df = fetch_crypto_data(pair)
if not df.empty:
    st.line_chart(df.set_index('timestamp')['close'])
    st.write("Últimos dados:", df.tail())