import geopandas as gpd
import pandas as pd

def process_districts():
    # Converte SHP para GeoJSON
    distritos = gpd.read_file('01_SP_Housing/data/SIRGAS_SHP_distrito.shp')
    
    # Padroniza colunas
    distritos = distritos.rename(columns={
        'ds_nome': 'bairro',
        'geometry': 'geometry'
    })[['bairro', 'geometry']]
    
    # Salva processado
    distritos.to_file('01_SP_Housing/data/sp_distritos_processado.geojson', driver='GeoJSON')

def merge_data():
    # Carrega os dados
    imoveis = pd.read_csv('01_SP_Housing/data/sp_properties_sample.csv')
    distritos = gpd.read_file('01_SP_Housing/data/sp_distritos_processado.geojson')
    
    # Converte para GeoDataFrame
    gdf = gpd.GeoDataFrame(
        imoveis,
        geometry=gpd.points_from_xy(imoveis.longitude, imoveis.latitude)
    )
    
    # Junta com dados espaciais
    merged = gpd.sjoin(gdf, distritos, how='left', op='within')
    merged.to_csv('01_SP_Housing/data/sp_final_data.csv', index=False)

if __name__ == '__main__':
    process_districts()
    merge_data()