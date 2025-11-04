# prepare_deploy.py
import os
import shutil
from pathlib import Path

def prepare_streamlit_deploy():
    """Prepara o projeto para deploy no Streamlit Cloud"""
    
    project_root = Path(".")
    
    print("🚀 Preparando deploy no Streamlit Cloud...")
    
    # 1. Verificar se requirements.txt existe
    if not (project_root / "requirements.txt").exists():
        print("❌ requirements.txt não encontrado na raiz")
        return False
    
    # 2. Copiar dados processados se necessário
    data_src = project_root / "data" / "processed" / "precos_por_distrito.json"
    if data_src.exists():
        print("✅ Dados encontrados em data/processed/")
    else:
        print("❌ Dados não encontrados - verifique o caminho")
        return False
    
    # 3. Verificar se streamlit_app.py existe
    if not (project_root / "streamlit_app.py").exists():
        print("❌ streamlit_app.py não encontrado")
        print("💡 Crie o arquivo seguindo as instruções acima")
        return False
    
    # 4. Listar estrutura final
    print("\n📁 Estrutura para deploy:")
    for item in project_root.iterdir():
        if item.is_file() and item.suffix in ['.py', '.txt', '.md']:
            print(f"   📄 {item.name}")
        elif item.is_dir() and item.name in ['data', 'app_housing']:
            print(f"   📁 {item.name}/")
    
    print("\n🎯 CONFIGURAÇÃO NO STREAMLIT CLOUD:")
    print("   Main file path: 01-real-estate-sp/streamlit_app.py")
    
    return True

if __name__ == "__main__":
    if prepare_streamlit_deploy():
        print("\n✅ PRONTO PARA DEPLOY!")
        print("\n🌐 Acesse: https://share.streamlit.io")
        print("📁 Configure o main file path como: 01-real-estate-sp/streamlit_app.py")
    else:
        print("\n❌ Corrija os problemas acima")