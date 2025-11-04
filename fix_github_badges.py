# fix_github_badges.py
import os
from pathlib import Path

def check_and_fix_badges():
    workflows_dir = Path(".github/workflows")
    readme_path = Path("README.md")
    
    print("🔍 Analisando workflows...")
    
    # Listar workflows existentes
    workflows = list(workflows_dir.glob("*.yml")) + list(workflows_dir.glob("*.yaml"))
    
    print("📋 Workflows encontrados:")
    existing_workflows = []
    for wf in workflows:
        print(f"   ✅ {wf.name}")
        existing_workflows.append(wf.name)
    
    # Verificar README
    if readme_path.exists():
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
        
        print("\n🔍 Procurando badges no README...")
        
        # Buscar badges no README
        import re
        badge_pattern = r'!\[.*?\]\(https://github\.com/.*?/workflows/(.*?)/badge\.svg\)'
        badges_found = re.findall(badge_pattern, readme_content)
        
        if badges_found:
            print("📛 Badges encontradas no README:")
            for badge in badges_found:
                status = "✅ EXISTE" if badge in existing_workflows else "❌ NÃO EXISTE"
                print(f"   {status} {badge}")
        else:
            print("❌ Nenhuma badge encontrada no README")
    
    # Sugerir correções
    print(f"\n🎯 SUGESTÕES:")
    
    if "deploy.yml" not in existing_workflows and "streamlit.yml" in existing_workflows:
        print("1. Renomear streamlit.yml para deploy.yml:")
        print("   git mv .github/workflows/streamlit.yml .github/workflows/deploy.yml")
    
    if "tests.yml" not in existing_workflows:
        print("2. Criar arquivo tests.yml (veja exemplo acima)")
    
    print(f"\3. Badges que funcionarão:")
    for wf in existing_workflows:
        badge_url = f"https://github.com/AldBer/DataScience-Portfolio/actions/workflows/{wf}/badge.svg"
        print(f"   ![Badge]({badge_url})")

if __name__ == "__main__":
    check_and_fix_badges()