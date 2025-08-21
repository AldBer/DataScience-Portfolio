import geopandas as gpd
from pathlib import Path
import os

def process_districts():
    # Caminho absoluto explícito para debug
    geo_dir = Path(r"f:\Documents\04. Cursos\17.Python\05.Portfolio\dashboards\01_SP_Housing\data\geo")
    shp_file = geo_dir / "SIRGAS_SHP_distrito.shp"
    
    print(f"Verificando arquivo em: {shp_file}")
    print(f"Arquivo existe? {shp_file.exists()}")
    
    if not shp_file.exists():
        print("\nArquivos no diretório geo:")
        for f in geo_dir.glob('*'):
            print(f.name)
        raise FileNotFoundError(f"Shapefile não encontrado em: {shp_file}")
    
    try:
        distritos = gpd.read_file(shp_file)
        print("\nLeitura bem-sucedida!")
        print(f"CRS: {distritos.crs}")
        print(f"Distritos carregados: {len(distritos)}")
        
        # Processamento adicional...
        output_path = geo_dir.parent / "processed/sp_distritos_processado.geojson"
        output_path.parent.mkdir(exist_ok=True)
        distritos.to_file(output_path, driver='GeoJSON')
        print(f"Dados salvos em: {output_path}")
        
    except Exception as e:
        print(f"\nErro durante o processamento:")
        raise

if __name__ == "__main__":
    process_districts()