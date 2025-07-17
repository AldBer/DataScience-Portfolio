import ccxt  # Biblioteca para exchanges
from 02_Crypto_Analysis.notifiers.telegram_bot import TelegramBot
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega do .env

exchange = ccxt.binance({
    'apiKey': os.getenv('BINANCE_API_KEY'),
    'secret': os.getenv('BINANCE_SECRET_KEY'),
    'enableRateLimit': True,
    'options': {
        'defaultType': 'spot',
        'test': os.getenv('TEST_MODE') == 'True'
    }
})

def estrategia_compra(pair='BTC/USDT'):
    ticker = exchange.fetch_ticker(pair)
    preco = ticker['last']
    
    # Estratégia simples: Média Móvel
    candles = exchange.fetch_ohlcv(pair, '1d', limit=30)
    close_prices = [c[4] for c in candles]
    media_30d = sum(close_prices) / len(close_prices)
    
    if preco < media_30d * 0.98:  # 2% abaixo da média
        exchange.create_market_buy_order(pair, 0.00001)  # Compra 0.00001 BTC
        return "ORDEM EXECUTADA: COMPRA"
    return "AGUARDANDO OPORTUNIDADE"

class TradingBot:
    def __init__(self):
        self.notifier = TelegramBot()
        
    def execute_trade(self):
        try:
            # ... lógica de trading ...
            self.notifier.send_alert(f"✅ Ordem executada: *Compra 0.00001 BTC* a ${preco}")
            
        except Exception as e:
            self.notifier.send_error(e, "Tentativa de execução de ordem")
            raise  # Re-lança o erro após notificar

import schedule
import time

def heartbeat():
    TelegramBot().send_alert("❤️ *Heartbeat*\\nBot em execução contínua", silent=True)

# Agendamento (opcional)
schedule.every(6).hours.do(heartbeat)

while True:
    schedule.run_pending()
    time.sleep(1)