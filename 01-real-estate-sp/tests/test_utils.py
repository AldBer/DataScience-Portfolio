"""
Testes para funções utilitárias
"""

import unittest
import sys
import os

# Adiciona o diretório scripts ao path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from utils import format_currency, get_summary_stats
import pandas as pd

class TestUtils(unittest.TestCase):
    
    def test_format_currency(self):
        """Testa formatação de moeda"""
        self.assertEqual(format_currency(1000.50), "R$ 1.000,50")
        self.assertEqual(format_currency(1000000), "R$ 1.000.000,00")
        self.assertTrue("N/A" in format_currency(None))
    
    def test_get_summary_stats(self):
        """Testa estatísticas resumidas"""
        df = pd.DataFrame({
            "price_per_m2": [1000, 2000, 3000, 4000, 5000]
        })
        
        stats = get_summary_stats(df)
        self.assertEqual(stats["mean"], 3000.0)
        self.assertEqual(stats["median"], 3000.0)
        self.assertEqual(stats["min"], 1000)
        self.assertEqual(stats["max"], 5000)

if __name__ == '__main__':
    unittest.main()
