#!/usr/bin/env python3
"""
LIMPEZA FINAL - Remove pastas antigas da raiz
"""
import os
import shutil

def remove_old_folders():
    """Remove pastas antigas da raiz se estiverem vazias ou duplicadas"""
    
    old_folders = [
        "01-real-estate-sp",
        "02-sql-projects", 
        "03-dashboards",
        "04-cyber-finance-guardian",
        "05-aws-security-labs"
    ]
    
    print("🧹 LIMPEZA FINAL DE PASTAS ANTIGAS")
    print("=" * 40)
    
    for folder in old_folders:
        if os.path.exists(folder):
            # Verificar se está vazia
            items = os.listdir(folder)
            if len(items) == 0:
                os.rmdir(folder)
                print(f"✅ Removida (vazia): {folder}/")
            else:
                print(f"⚠️  Ainda tem conteúdo: {folder}/")
                print(f"   Conteúdo: {items[:3]}...")  # Mostra primeiros 3 itens
                
                # Perguntar se quer remover mesmo com conteúdo
                response = input(f"   Remover {folder}/ mesmo com conteúdo? (s/n): ").strip().lower()
                if response == 's':
                    shutil.rmtree(folder)
                    print(f"   ✅ Removida: {folder}/")
                else:
                    print(f"   ⏭️  Mantida: {folder}/")

def verify_structure():
    """Verifica estrutura final"""
    print("\n📁 VERIFICAÇÃO FINAL DA ESTRUTURA")
    print("=" * 40)
    
    # Verificar projetos em projects/
    projects = os.listdir("projects")
    print(f"📦 Projetos em projects/: {len(projects)}")
    for p in sorted(projects):
        count = len(os.listdir(f"projects/{p}"))
        print(f"   ├── {p}/ ({count} itens)")
    
    # Verificar pastas antigas
    print(f"\n📁 Pastas antigas na raiz:")
    old_folders = ["01-real-estate-sp", "02-sql-projects", "03-dashboards", 
                   "04-cyber-finance-guardian", "05-aws-security-labs"]
    
    for folder in old_folders:
        if os.path.exists(folder):
            print(f"   ❌ {folder}/ (PRECISA REMOVER)")
        else:
            print(f"   ✅ {folder}/ (JÁ REMOVIDA)")

if __name__ == "__main__":
    print("🎯 ETAPA FINAL: Limpeza de pastas antigas")
    verify_structure()
    
    confirm = input("\n❓ Executar limpeza? (s/n): ").strip().lower()
    if confirm == 's':
        remove_old_folders()
        print("\n✅ LIMPEZA CONCLUÍDA!")
    else:
        print("🚫 Limpeza cancelada.")
    
    # Verificação final
    verify_structure()
    
    print("\n📋 PRÓXIMOS PASSOS:")
    print("1. git status (verificar mudanças)")
    print("2. git add . && git commit -m 'Estrutura finalizada'")
    print("3. git push origin main")
    print("4. Configurar GitHub Pages")