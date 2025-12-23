# data/data_cache.py - VERSÃO CORRIGIDA
import pandas as pd
import pickle
import os
from datetime import datetime, timedelta

class DataCache:
    """Cache local para evitar muitas chamadas de API"""
    
    def __init__(self, cache_dir='data/cache'):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
    
    def get_cache_key(self, source, params):
        """Gera chave única para cache"""
        return f"{source}_{hash(str(params))}.pkl"
    
    def get_data(self, source, params, max_age_hours=24):
        """Busca dados do cache se ainda forem recentes"""
        cache_file = os.path.join(self.cache_dir, self.get_cache_key(source, params))
        
        if os.path.exists(cache_file):
            file_age = datetime.now() - datetime.fromtimestamp(os.path.getmtime(cache_file))
            if file_age < timedelta(hours=max_age_hours):
                with open(cache_file, 'rb') as f:
                    return pickle.load(f)
        
        return None
    
    def save_data(self, source, params, data):
        """Salva dados no cache"""
        cache_file = os.path.join(self.cache_dir, self.get_cache_key(source, params))
        with open(cache_file, 'wb') as f:
            pickle.dump(data, f)