#!/usr/bin/env python3
"""
Script de Refatoração do Portfólio de Data Science
Reorganiza a estrutura atual para seguir melhores práticas

Autor: Claude AI Assistant
Data: 2025-08-18
"""

import os
import shutil
import sys
from pathlib import Path
import subprocess
import json
from datetime import datetime

class PortfolioRefactor:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path).resolve()
        self.backup_created = False
        self.changes_log = []
        
    def log_change(self, action, source="", target=""):
        """Registra mudanças para rollback se necessário"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        change = {
            "time": timestamp,
            "action": action,
            "source": source,
            "target": target
        }
        self.changes_log.append(change)
        print(f"[{timestamp}] {action}: {source} -> {target}")
    
    def create_backup(self):
        """Cria backup do estado atual"""
        try:
            backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            backup_path = self.base_path.parent / backup_name
            
            print(f"🔄 Criando backup em: {backup_path}")
            shutil.copytree(self.base_path, backup_path, ignore=shutil.ignore_patterns('.git'))
            
            self.backup_created = True
            self.log_change("BACKUP_CREATED", target=str(backup_path))
            print(f"✅ Backup criado com sucesso!")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao criar backup: {e}")
            return False
    
    def is_git_repo(self):
        """Verifica se é um repositório Git"""
        return (self.base_path / ".git").exists()
    
    def git_add_and_commit(self, message):
        """Adiciona mudanças ao Git"""
        if not self.is_git_repo():
            return True
            
        try:
            subprocess.run(["git", "add", "."], cwd=self.base_path, check=True)
            subprocess.run(["git", "commit", "-m", message], cwd=self.base_path, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Git commit falhou: {e}")
            return False
    
    def remove_unnecessary_files(self):
        """Remove arquivos desnecessários"""
        print("\n🗑️ Removendo arquivos desnecessários...")
        
        files_to_remove = [
            "index.md",
            "script.py", 
            "setup.py",
            "estrutura.txt",
            ".vscode.json"
        ]
        
        dirs_to_remove = [
            "_includes",
            "_sass-cache", 
            ".ipynb_checkpoints",
            ".sass-cache"
        ]
        
        # Remover arquivos
        for file in files_to_remove:
            file_path = self.base_path / file
            if file_path.exists():
                file_path.unlink()
                self.log_change("REMOVED_FILE", source=str(file_path))
        
        # Remover diretórios
        for dir_name in dirs_to_remove:
            dir_path = self.base_path / dir_name
            if dir_path.exists():
                shutil.rmtree(dir_path)
                self.log_change("REMOVED_DIR", source=str(dir_path))
    
    def restructure_projects(self):
        """Reestrutura os projetos"""
        print("\n📁 Reestruturando projetos...")
        
        # Renomear e mover dashboards/01_SP_Housing para 01-real-estate-sp
        old_housing_path = self.base_path / "dashboards" / "01_SP_Housing"
        new_housing_path = self.base_path / "01-real-estate-sp"
        
        if old_housing_path.exists():
            shutil.move(str(old_housing_path), str(new_housing_path))
            self.log_change("MOVED_PROJECT", source=str(old_housing_path), target=str(new_housing_path))
            
            # Criar estrutura interna do projeto
            self.create_project_structure(new_housing_path, "Real Estate Analysis")
        
        # Mover e organizar projetos SQL
        old_sql_path = self.base_path / "streams"
        new_sql_path = self.base_path / "03-sql-projects"
        
        if old_sql_path.exists():
            shutil.move(str(old_sql_path), str(new_sql_path))
            self.log_change("MOVED_PROJECT", source=str(old_sql_path), target=str(new_sql_path))
            self.create_project_structure(new_sql_path, "SQL Projects")
        
        # Mover core para assets globais
        core_path = self.base_path / "core"
        assets_path = self.base_path / "assets"
        
        if core_path.exists():
            assets_path.mkdir(exist_ok=True)
            shutil.move(str(core_path), str(assets_path / "core"))
            self.log_change("MOVED_CORE", source=str(core_path), target=str(assets_path / "core"))
    
    def create_project_structure(self, project_path, project_title):
        """Cria estrutura padrão dentro de cada projeto"""
        project_path = Path(project_path)
        
        # Criar diretórios padrão
        directories = ["src", "notebooks", "assets", "data"]
        for dir_name in directories:
            dir_path = project_path / dir_name
            dir_path.mkdir(exist_ok=True)
            
            # Criar __init__.py em src
            if dir_name == "src":
                (dir_path / "__init__.py").touch()
        
        # Criar README.md do projeto se não existir
        readme_path = project_path / "README.md"
        if not readme_path.exists():
            self.create_project_readme(readme_path, project_title)
    
    def create_project_readme(self, readme_path, project_title):
        """Cria README padrão para projeto"""
        readme_content = f"""# {project_title}

## 📊 Visão Geral
Breve descrição do projeto e problema de negócio que resolve.

## 🎯 Objetivos
- Objetivo principal 1
- Objetivo principal 2
- Objetivo principal 3

## 🛠️ Tecnologias Utilizadas
- Python
- Pandas
- Plotly/Matplotlib
- Streamlit (se aplicável)

## 📁 Estrutura do Projeto
```
{readme_path.parent.name}/
├── README.md              # Este arquivo
├── app.py                 # Aplicação principal (se houver)
├── requirements.txt       # Dependências
├── src/                   # Código fonte modular
├── notebooks/             # Análises Jupyter
├── assets/               # Imagens e recursos
└── data/                 # Dados (se permitido)
```

## 🚀 Como Executar
1. Instalar dependências:
```bash
pip install -r requirements.txt
```

2. Executar a aplicação:
```bash
streamlit run app.py
```

## 📈 Principais Resultados
- Resultado 1
- Resultado 2
- Resultado 3

## 📋 Próximos Passos
- [ ] Melhoria 1
- [ ] Melhoria 2
- [ ] Melhoria 3

---
**Desenvolvido por**: Aldo Bernardi  
**Data**: {datetime.now().strftime('%Y-%m-%d')}
"""
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        self.log_change("CREATED_README", target=str(readme_path))
    
    def update_main_readme(self):
        """Atualiza README principal"""
        print("\n📝 Atualizando README principal...")
        
        readme_content = """# 🚀 Portfólio de Ciência de Dados - Aldo Bernardi

Bem-vindo ao meu portfólio de projetos em Ciência de Dados! Este repositório contém uma coleção de projetos que demonstram minhas habilidades em análise de dados, machine learning e visualização.

## 🎯 Sobre Mim
Profissional apaixonado por transformar dados em insights estratégicos e soluções práticas para problemas reais.

**Conecte-se comigo:**
- 💼 [LinkedIn](https://linkedin.com/in/aldo-bernardi/)
- 🐙 [GitHub](https://github.com/aldber)
- 📧 [Email](mailto:aldo.bernardi@gmail.com)

## 📊 Projetos em Destaque

### 🏠 [Análise Imobiliária de São Paulo](./01-real-estate-sp/)
Dashboard interativo para análise do mercado imobiliário de SP com mapas de calor, visualizações 3D e insights geográficos.

**Tecnologias:** Python, Streamlit, Pandas, Plotly, Folium, GeoPandas

### 📈 [Monitor de Criptoativos](https://aldber-crypto.streamlit.app/)
Sistema automatizado para análise de oportunidades de trading com atualização via GitHub Actions.

**Tecnologias:** Python, Streamlit, CCXT, Telegram API

### 🗄️ [Projetos SQL e BI](./03-sql-projects/)
Série de projetos focados em SQL, agregações e Business Intelligence com Power BI.

**Tecnologias:** SQL, PostgreSQL, Power BI

## 🛠️ Habilidades Técnicas

### Linguagens
- **Python** (Pandas, NumPy, Scikit-learn)
- **SQL** (PostgreSQL, BigQuery)

### Visualização
- **Plotly & Dash**
- **GeoPandas & Folium** 
- **Power BI**
- **Matplotlib & Seaborn**

### Ferramentas
- **Git & GitHub**
- **Docker**
- **Streamlit**
- **Jupyter Notebooks**

## 📁 Estrutura do Repositório

```
📁 DataScience-Portfolio/
├── 🏠 01-real-estate-sp/          # Análise imobiliária SP
├── 📈 02-crypto-monitoring/       # Monitor criptomoedas  
├── 🗄️ 03-sql-projects/            # Projetos SQL e BI
├── 🤖 04-machine-learning/        # Projetos ML (em breve)
├── 📊 dashboards/                 # Landing page do portfólio
├── 🎨 assets/                     # Recursos globais
└── ⚙️ .github/workflows/          # Automações CI/CD
```

## 🚀 Acesso Rápido

- **🌐 [Portfólio Online](https://aldber.github.io/DataScience-Portfolio/)**
- **📊 [Dashboards Interativos](./dashboards/)**
- **📱 [Apps Streamlit](https://aldber-crypto.streamlit.app/)**

## 📈 Estatísticas do Repositório

![GitHub Repo stars](https://img.shields.io/github/stars/aldber/DataScience-Portfolio?style=social)
![GitHub forks](https://img.shields.io/github/forks/aldber/DataScience-Portfolio?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/aldber/DataScience-Portfolio)

## 🤝 Contribuições

Feedbacks e sugestões são sempre bem-vindos! Sinta-se à vontade para:
- Abrir [issues](https://github.com/aldber/DataScience-Portfolio/issues) com sugestões
- Fazer fork do repositório
- Enviar pull requests com melhorias

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

⭐ **Se este portfólio te ajudou de alguma forma, considere dar uma estrela no repositório!**

**Última atualização:** {datetime.now().strftime('%B %Y')}
"""
        
        readme_path = self.base_path / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        self.log_change("UPDATED_MAIN_README", target=str(readme_path))
    
    def create_missing_directories(self):
        """Cria diretórios que podem estar faltando"""
        print("\n📁 Criando estrutura de diretórios...")
        
        directories = [
            "02-crypto-monitoring",
            "04-machine-learning", 
            "assets/images",
            "assets/docs",
            "assets/presentations"
        ]
        
        for dir_path in directories:
            full_path = self.base_path / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            self.log_change("CREATED_DIR", target=str(full_path))
            
            # Criar README para projetos futuros
            if dir_path.startswith(("02-", "04-")):
                project_name = dir_path.split("-", 1)[1].replace("-", " ").title()
                readme_path = full_path / "README.md"
                self.create_project_readme(readme_path, f"{project_name} (Em Desenvolvimento)")
    
    def save_refactor_log(self):
        """Salva log das mudanças"""
        log_path = self.base_path / "refactor_log.json"
        
        log_data = {
            "timestamp": datetime.now().isoformat(),
            "backup_created": self.backup_created,
            "total_changes": len(self.changes_log),
            "changes": self.changes_log
        }
        
        with open(log_path, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n📋 Log salvo em: {log_path}")
    
    def run_refactor(self, create_backup=True):
        """Executa a refatoração completa"""
        print("🚀 Iniciando refatoração do portfólio...")
        print(f"📍 Diretório base: {self.base_path}")
        
        # Criar backup se solicitado
        if create_backup:
            if not self.create_backup():
                print("❌ Não foi possível criar backup. Abortando refatoração.")
                return False
        
        try:
            # Executar etapas da refatoração
            self.remove_unnecessary_files()
            self.restructure_projects()
            self.create_missing_directories()
            self.update_main_readme()
            
            # Salvar log
            self.save_refactor_log()
            
            # Commit das mudanças
            if self.is_git_repo():
                print("\n📤 Fazendo commit das mudanças...")
                self.git_add_and_commit("Refactor: Reorganize portfolio structure following best practices")
            
            print("\n✅ Refatoração concluída com sucesso!")
            print(f"📊 Total de mudanças: {len(self.changes_log)}")
            
            if self.backup_created:
                print(f"🔒 Backup disponível em: {self.base_path.parent}")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Erro durante a refatoração: {e}")
            print("🔄 Considere restaurar do backup se necessário.")
            return False


def main():
    """Função principal"""
    print("=" * 60)
    print("🔄 SCRIPT DE REFATORAÇÃO DO PORTFÓLIO")
    print("=" * 60)
    
    # Confirmar execução
    response = input("\n⚠️ Este script irá reorganizar sua estrutura de arquivos.\nDeseja continuar? (s/N): ").lower().strip()
    
    if response != 's':
        print("❌ Operação cancelada pelo usuário.")
        return
    
    # Executar refatoração
    refactor = PortfolioRefactor()
    success = refactor.run_refactor(create_backup=True)
    
    if success:
        print("\n🎉 Seu portfólio foi reorganizado com sucesso!")
        print("\n📋 Próximos passos recomendados:")
        print("1. Revisar as mudanças com 'git status'")
        print("2. Testar o GitHub Pages")
        print("3. Atualizar requirements.txt nos projetos")
        print("4. Adicionar conteúdo aos novos READMEs")
    else:
        print("\n😟 A refatoração falhou. Verifique os logs e backup.")

if __name__ == "__main__":
    main()