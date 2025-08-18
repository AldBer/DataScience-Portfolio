#!/usr/bin/env python3
"""
Script de Rollback para Refatoração do Portfólio
Restaura o estado anterior usando o backup criado

Autor: Claude AI Assistant  
Data: 2025-08-18
"""

import os
import shutil
import sys
import json
from pathlib import Path
from datetime import datetime

def find_backup_folders(base_path):
    """Encontra pastas de backup disponíveis"""
    parent_dir = Path(base_path).parent
    backup_folders = []
    
    for item in parent_dir.iterdir():
        if item.is_dir() and item.name.startswith("backup_"):
            backup_folders.append(item)
    
    return sorted(backup_folders, key=lambda x: x.name, reverse=True)

def restore_from_backup(backup_path, target_path):
    """Restaura arquivos do backup"""
    try:
        # Remover conteúdo atual (exceto .git)
        for item in Path(target_path).iterdir():
            if item.name != '.git':
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()
        
        # Restaurar do backup
        for item in backup_path.iterdir():
            target_item = Path(target_path) / item.name
            if item.is_dir():
                shutil.copytree(item, target_item)
            else:
                shutil.copy2(item, target_item)
        
        return True
        
    except Exception as e:
        print(f"❌ Erro durante restauração: {e}")
        return False

def main():
    base_path = Path(".").resolve()
    
    print("🔄 SCRIPT DE ROLLBACK - RESTAURAR BACKUP")
    print("=" * 50)
    
    # Encontrar backups disponíveis
    backups = find_backup_folders(base_path)
    
    if not backups:
        print("❌ Nenhum backup encontrado no diretório pai.")
        return
    
    print(f"📦 Backups disponíveis:")
    for i, backup in enumerate(backups):
        print(f"{i+1}. {backup.name}")
    
    # Seleção do backup
    try:
        choice = int(input(f"\nEscolha o backup (1-{len(backups)}): ")) - 1
        if choice < 0 or choice >= len(backups):
            raise ValueError
            
        selected_backup = backups[choice]
        
    except ValueError:
        print("❌ Seleção inválida.")
        return
    
    # Confirmação
    print(f"\n⚠️ Isso irá restaurar o backup: {selected_backup.name}")
    print("⚠️ TODAS as mudanças atuais serão perdidas!")
    
    confirm = input("Deseja continuar? (digite 'CONFIRMAR'): ")
    if confirm != 'CONFIRMAR':
        print("❌ Operação cancelada.")
        return
    
    # Executar restauração
    print(f"\n🔄 Restaurando backup...")
    success = restore_from_backup(selected_backup, base_path)
    
    if success:
        print("✅ Backup restaurado com sucesso!")
        print(f"🗑️ Você pode deletar o backup em: {selected_backup}")
    else:
        print("❌ Falha na restauração do backup.")

if __name__ == "__main__":
    main()