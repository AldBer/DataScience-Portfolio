import yfinance as yf
import pandas as pd

CRYPTO_LIST = ['BTC-USD', 'ETH-USD', 'BNB-USD']

def fetch_data():
    for crypto in CRYPTO_LIST:
        data = yf.download(crypto, period='1y', interval='1d')
        data.to_csv(f'02_Crypto_Analysis/data/{crypto}.csv')

if __name__ == '__main__':
    fetch_data()