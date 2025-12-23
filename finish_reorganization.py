#!/usr/bin/env python3
"""
Script para finalizar a reorganização - Move pastas antigas para dentro de projects/
"""
import os
import shutil
import sys

def move_old_folders_to_projects():
    """Move as pastas antigas da raiz para dentro de projects/"""
    
    # Pastas antigas que devem ser movidas
    old_folders = [
        "01-real-estate-sp",
        "02-sql-projects", 
        "03-dashboards",
        "04-cyber-finance-guardian",
        "05-aws-security-labs"
    ]
    
    # Nomes novos dentro de projects/
    new_names = {
        "01-real-estate-sp": "01-real-estate-sp",
        "02-sql-projects": "02-sql-analytics",
        "03-dashboards": "03-sales-dashboard",
        "04-cyber-finance-guardian": "04-cyber-finance-guardian",
        "05-aws-security-labs": "05-aws-security-labs"
    }
    
    moved_count = 0
    
    for old_folder in old_folders:
        if os.path.exists(old_folder):
            new_folder_name = new_names[old_folder]
            destination = os.path.join("projects", new_folder_name)
            
            print(f"\n📁 Movendo: {old_folder} -> {destination}")
            
            try:
                # Se já existir algo no destino, mesclar
                if os.path.exists(destination):
                    print(f"  ⚠️  Destino já existe, mesclando conteúdo...")
                    # Mover conteúdo individualmente
                    for item in os.listdir(old_folder):
                        src = os.path.join(old_folder, item)
                        dst = os.path.join(destination, item)
                        
                        if os.path.isdir(src):
                            shutil.copytree(src, dst, dirs_exist_ok=True)
                            print(f"  📂 Pasta: {item}")
                        else:
                            shutil.copy2(src, dst)
                            print(f"  📄 Arquivo: {item}")
                    
                    # Remover pasta antiga após copiar tudo
                    shutil.rmtree(old_folder)
                else:
                    # Mover pasta inteira
                    shutil.move(old_folder, destination)
                
                moved_count += 1
                print(f"  ✅ Movido com sucesso!")
                
            except Exception as e:
                print(f"  ❌ Erro movendo {old_folder}: {e}")
    
    return moved_count

def check_current_structure():
    """Mostra estrutura atual"""
    print("\n📁 ESTRUTURA ATUAL:")
    print("-" * 40)
    
    # Lista pastas na raiz
    items = os.listdir('.')
    folders = [f for f in items if os.path.isdir(f) and not f.startswith('.')]
    
    for folder in sorted(folders):
        if folder == 'projects':
            print(f"📦 {folder}/")
            # Lista subpastas de projects
            if os.path.exists('projects'):
                projects = os.listdir('projects')
                for project in sorted(projects):
                    print(f"   └── 📁 {project}/")
        else:
            print(f"📁 {folder}/")
    
    print("-" * 40)

def main():
    print("=" * 60)
    print("🔄 FINALIZANDO REORGANIZAÇÃO DO PORTFÓLIO")
    print("=" * 60)
    
    # Mostrar estado atual
    check_current_structure()
    
    print("\n⚠️  Este script irá MOVER as pastas antigas para dentro de projects/")
    print("   Onde já existir conteúdo, será feito merge.")
    
    confirm = input("\n❓ Continuar? (s/n): ").strip().lower()
    if confirm != 's':
        print("🚫 Operação cancelada.")
        sys.exit(0)
    
    # Mover pastas
    moved = move_old_folders_to_projects()
    
    print(f"\n{'='*60}")
    print(f"✅ CONCLUÍDO: {moved} pastas movidas")
    print("=" * 60)
    
    # Mostrar estrutura final
    print("\n📁 ESTRUTURA FINAL:")
    print("-" * 40)
    
    if os.path.exists('projects'):
        projects = os.listdir('projects')
        for project in sorted(projects):
            print(f"📁 projects/{project}/")
    
    print("-" * 40)
    
    print("\n📋 PRÓXIMOS PASSOS:")
    print("1. Verificar se todos os projetos estão em projects/")
    print("2. Testar: ls -la projects/")
    print("3. Remover pastas vazias se houver")
    print("4. git add . && git commit -m 'Estrutura finalizada'")
    print("5. git push origin main")

if __name__ == "__main__":
    main()