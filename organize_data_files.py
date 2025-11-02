# organize_data_files.py
import os
import shutil
from pathlib import Path

def organize_data_files():
    """Move arquivos de dados brutos para pasta organizada"""
    
    # Extensões de dados brutos
    raw_extensions = {'.xlsx', '.xls', '.csv', '.parquet'}
    
    # Pastas para organizar
    project_folders = [
        '03-sql-projects/Semana_03',
        '01-real-estate-sp/data/raw',
        # adicione outras pastas conforme necessário
    ]
    
    for project_folder in project_folders:
        project_path = Path(project_folder)
        
        if not project_path.exists():
            continue
            
        # Criar pasta dados_brutos se não existir
        raw_data_dir = project_path / 'dados_brutos'
        raw_data_dir.mkdir(exist_ok=True)
        
        # Mover arquivos brutos
        for file_path in project_path.iterdir():
            if file_path.is_file() and file_path.suffix.lower() in raw_extensions:
                if 'dados_brutos' not in str(file_path):
                    new_path = raw_data_dir / file_path.name
                    shutil.move(str(file_path), str(new_path))
                    print(f"📁 Movido: {file_path} → {new_path}")

if __name__ == "__main__":
    organize_data_files()