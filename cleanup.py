#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

# Configurações
TARGET_DIRS = [
    "dashboards",
    "core",
    "streams"
]
EXCLUDE_DIRS = {"assets", "data", "scripts"}  # Pastas para não deletar
FILE_EXTENSIONS_TO_DELETE = {
    # Temporários/desnecessários
    ".ipynb_checkpoints", ".pyc", ".pyo", ".pyd", ".tmp", 
    ".log", ".cache", ".swp", ".swo", ".DS_Store", "Thumbs.db",
    # Dados redundantes
    ".shp", ".shx", ".dbf", ".zip"  
}
MAX_SIZE_MB = 50  # Arquivos acima disso serão alertados

def clean_directory(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Remove subdiretórios indesejados
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            if dirname in EXCLUDE_DIRS:
                continue
            if any(x in dirname.lower() for x in ("temp", "cache", "checkpoint")):
                print(f"Removendo diretório: {full_path}")
                shutil.rmtree(full_path, ignore_errors=True)

        # Remove arquivos indesejados
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            full_path = os.path.join(dirpath, filename)
            
            if ext in FILE_EXTENSIONS_TO_DELETE:
                print(f"Removendo arquivo: {full_path}")
                os.unlink(full_path)
            elif os.path.getsize(full_path) > MAX_SIZE_MB * 1024 * 1024:
                print(f"ALERTA: Arquivo grande ({os.path.getsize(full_path)/1024/1024:.2f} MB): {full_path}")

def main():
    print("=== INICIANDO LIMPEZA ===")
    for target_dir in TARGET_DIRS:
        if os.path.exists(target_dir):
            print(f"\nLimpando: {target_dir}")
            clean_directory(target_dir)
    print("\n=== LIMPEZA CONCLUÍDA ===")

if __name__ == "__main__":
    main()

input()