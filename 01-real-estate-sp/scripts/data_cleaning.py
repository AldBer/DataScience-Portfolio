"""
Funções de limpeza e processamento de dados
"""

import pandas as pd
import geopandas as gpd
import numpy as np
from shapely.geometry import Point, Polygon

def clean_property_data(df):
    """
    Limpa e padroniza dados de propriedades
    
    Args:
        df (DataFrame): DataFrame com dados de propriedades
    
    Returns:
        DataFrame: DataFrame limpo
    """
    df_clean = df.copy()
    
    # Remove duplicatas
    initial_count = len(df_clean)
    df_clean = df_clean.drop_duplicates()
    duplicates_removed = initial_count - len(df_clean)
    
    if duplicates_removed > 0:
        print(f"   🧹 Removidas {duplicates_removed} duplicatas")
    
    # Remove valores nulos críticos
    critical_columns = ['price', 'district', 'area_m2']
    for col in critical_columns:
        if col in df_clean.columns:
            before_count = len(df_clean)
            df_clean = df_clean.dropna(subset=[col])
            removed = before_count - len(df_clean)
            if removed > 0:
                print(f"   🧹 Removidas {removed} linhas com {col} nulo")
    
    # Calcula preço por m² se não existir
    if 'price_per_m2' not in df_clean.columns and 'price' in df_clean.columns and 'area_m2' in df_clean.columns:
        df_clean['price_per_m2'] = df_clean['price'] / df_clean['area_m2']
        print("   ✅ Coluna 'price_per_m2' criada")
    
    return df_clean

def clean_geodata(gdf):
    """
    Limpa dados geoespaciais
    
    Args:
        gdf (GeoDataFrame): GeoDataFrame com dados geoespaciais
    
    Returns:
        GeoDataFrame: GeoDataFrame limpo
    """
    gdf_clean = gdf.copy()
    
    # Remove geometrias inválidas
    valid_mask = gdf_clean.geometry.is_valid
    invalid_count = (~valid_mask).sum()
    
    if invalid_count > 0:
        print(f"   🧹 Removidas {invalid_count} geometrias inválidas")
        gdf_clean = gdf_clean[valid_mask]
    
    # Remove geometrias vazias
    empty_mask = gdf_clean.geometry.is_empty
    empty_count = empty_mask.sum()
    
    if empty_count > 0:
        print(f"   🧹 Removidas {empty_count} geometrias vazias")
        gdf_clean = gdf_clean[~empty_mask]
    
    return gdf_clean

def standardize_crs(gdf, target_crs="EPSG:4326"):
    """
    Padroniza sistema de coordenadas
    
    Args:
        gdf (GeoDataFrame): GeoDataFrame
        target_crs (str): CRS alvo
    
    Returns:
        GeoDataFrame: GeoDataFrame com CRS padronizado
    """
    if gdf.crs != target_crs:
        gdf_transformed = gdf.to_crs(target_crs)
        print(f"   🗺️  CRS convertido para {target_crs}")
        return gdf_transformed
    
    return gdf
