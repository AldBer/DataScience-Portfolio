#!/usr/bin/env python3
"""
Script de limpeza segura para a branch main
Remove arquivos temporários e desnecessários mantendo a integridade do repositório
"""

import os
import shutil
from pathlib import Path

# Configurações seguras para a branch main
SAFE_DIRECTORIES = {
    'dashboards': [
        '01_SP_Housing/data/processed/*.geojson',  # Mantém arquivos geo processados
        '02_Crypto_Analysis/data/*.csv'           # Mantém dados críticos
    ],
    'core': [
        'assets/*.zip'  # Exemplo: manter arquivos compactados originais
    ]
}

def confirm_branch():
    """Verifica se estamos na branch main com confirmação explícita"""
    import git
    repo = git.Repo(search_parent_directories=True)
    if repo.active_branch.name != 'main':
        raise RuntimeError("ERRO: Script deve ser executado apenas na branch main!")
    
    print(f"\n=== Executando no repositório: {repo.working_dir}")
    print(f"=== Branch atual: {repo.active_branch.name}\n")
    
    # Confirmação adicional
    response = input("Tem certeza que deseja executar o cleanup na branch main? (s/n): ")
    if response.lower() != 's':
        print("Operação cancelada pelo usuário.")
        exit(0)

def safe_remove(path):
    """Remove arquivos/diretórios com verificações de segurança"""
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"Removendo arquivo: {path}")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Removendo diretório: {path}")
    except Exception as e:
        print(f"AVISO: Não foi possível remover {path} - {str(e)}")

def is_protected(file_path):
    """Verifica se o arquivo está na lista de protegidos"""
    for base_dir, patterns in SAFE_DIRECTORIES.items():
        for pattern in patterns:
            if file_path.match(pattern):
                return True
    return False

def clean_directory(directory):
    """Limpa um diretório de forma segura"""
    print(f"\nLimpando: {directory}")
    
    for root, dirs, files in os.walk(directory):
        for name in files + dirs:
            item_path = Path(root) / name
            
            # Pula itens protegidos
            if is_protected(item_path):
                continue
                
            # Remove checkpoints e arquivos temporários
            if '.ipynb_checkpoints' in str(item_path):
                safe_remove(item_path)
            elif item_path.suffix in ('.tmp', '.log', '.cache'):
                safe_remove(item_path)
            elif item_path.name == '__pycache__':
                safe_remove(item_path)

def main():
    try:
        confirm_branch()
        
        # Diretórios para limpar
        directories_to_clean = [
            'dashboards',
            'core',
            'streams'
        ]
        
        for directory in directories_to_clean:
            if os.path.exists(directory):
                clean_directory(directory)
        
        print("\n=== LIMPEZA CONCLUÍDA COM SUCESSO ===")
        print("Verifique as alterações com 'git status' antes de commitar.")
        
    except Exception as e:
        print(f"\nERRO CRÍTICO: {str(e)}")
        print("Operação abortada para evitar danos ao repositório.")
        exit(1)

if __name__ == '__main__':
    main()