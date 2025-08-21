"""
Funções auxiliares para o projeto Real Estate SP
"""

import pandas as pd
import geopandas as gpd
from pathlib import Path

def get_project_root():
    """Retorna o diretório raiz do projeto"""
    return Path(__file__).parent.parent

def load_processed_geodata():
    """Carrega dados geoespaciais processados"""
    data_path = get_project_root() / "data" / "processed"
    
    # Busca pelo arquivo geojson mais recente
    geojson_files = list(data_path.glob("*.geojson"))
    if geojson_files:
        latest_file = max(geojson_files, key=lambda x: x.stat().st_mtime)
        return gpd.read_file(latest_file)
    return None

def format_currency(value, currency="R$"):
    """Formata valores monetários"""
    if pd.isna(value):
        return "N/A"
    return f"{currency} {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def validate_coordinates(gdf):
    """Valida coordenadas geográficas"""
    if gdf is None or gdf.empty:
        return False
    
    # Verifica se há geometrias válidas
    valid_geoms = gdf.geometry.is_valid
    return valid_geoms.all()

def get_summary_stats(df, price_column="price_per_m2"):
    """Retorna estatísticas resumidas dos preços"""
    if price_column not in df.columns:
        return {}
    
    return {
        "mean": df[price_column].mean(),
        "median": df[price_column].median(),
        "std": df[price_column].std(),
        "min": df[price_column].min(),
        "max": df[price_column].max(),
        "count": df[price_column].count()
    }
