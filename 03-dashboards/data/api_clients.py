# data/api_clients.py - VERSÃO CORRIGIDA
import requests
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time

class FakeStoreClient:
    """Cliente para API FakeStore - Dados de E-commerce"""
    
    def __init__(self):
        self.base_url = "https://fakestoreapi.com"
    
    def get_products(self):
        """Busca todos os produtos"""
        try:
            response = requests.get(f"{self.base_url}/products")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"ERRO: Erro FakeStore API: {e}")  # ✅ REMOVIDO EMOJI
            return []
    
    def get_categories(self):
        """Busca categorias"""
        try:
            response = requests.get(f"{self.base_url}/products/categories")
            return response.json()
        except:
            return []

class YahooFinanceClient:
    """Cliente para Yahoo Finance - Dados Financeiros"""
    
    def __init__(self):
        self.tickers = {
            'varejo_br': ['MGLU3.SA', 'VVAR3.SA', 'BTOW3.SA', 'LREN3.SA'],
            'tech_global': ['AMZN', 'SHOP', 'W', 'ETSY']
        }
    
    def get_stock_data(self, tickers, period='6mo'):
        """Busca dados históricos de ações"""
        try:
            data = yf.download(tickers, period=period, progress=False)
            return data
        except Exception as e:
            print(f"ERRO: Erro Yahoo Finance: {e}")  # ✅ REMOVIDO EMOJI
            return None
    
    def get_current_prices(self, tickers):
        """Busca preços atuais"""
        try:
            data = yf.download(tickers, period='1d', progress=False)
            return data['Close'].iloc[-1] if not data.empty else None
        except:
            return None