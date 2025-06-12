import numpy as np
import pandas as pd
import pandas_ta as ta

print("Versões:")
print("NumPy:", np.__version__)
print("Pandas-ta:", ta.__version__)

# Teste RSI
data = pd.Series([10, 12, 15, 14, 13, 12, 11])
rsi = ta.rsi(data, length=3)
print("\nRSI calculado:", rsi.values)
