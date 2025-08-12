class TradingAgent:
    def __init__(self):
        self.history = []
    
    def analyze(self, symbol):
        """Simula análise de mercado"""
        import random
        signal = random.choice(['BUY', 'SELL', 'HOLD'])
        self.history.append(f"{symbol}: {signal}")
        return signal