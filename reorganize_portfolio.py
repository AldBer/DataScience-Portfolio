Claro! Vi alguns problemas de indentação e lógica no código. Vou reescrever o script corrigindo todos os erros e melhorando a organização:

```python
#!/usr/bin/env python3
"""
Script para reorganizar o portfolio de forma segura
"""
import os
import shutil
from pathlib import Path
import sys

def create_new_structure(base_path):
    """Cria nova estrutura de pastas"""
    new_folders = [
        "projects",
        "projects/01-real-estate-sp",
        "projects/02-sql-analytics", 
        "projects/03-sales-dashboard",
        "projects/04-cyber-finance-guardian",
        "projects/05-aws-security-labs",
        "docs",
        "assets/screenshots",
        "assets/icons",
        "templates"
    ]
    
    for folder in new_folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"✅ Criada pasta: {folder}")

def move_project_files(base_path):
    """Move arquivos dos projetos para nova estrutura"""
    
    # Mapeamento de projetos antigos para novos
    projects_mapping = {
        "01-real-estate-sp": "01-real-estate-sp",
        "02-sql-projects": "02-sql-analytics",
        "03-dashboards": "03-sales-dashboard",
        "04-cyber-finance-guardian": "04-cyber-finance-guardian",
        "05-aws-security-labs": "05-aws-security-labs"
    }
    
    for old_name, new_name in projects_mapping.items():
        old_path = os.path.join(base_path, old_name)
        new_path = os.path.join(base_path, "projects", new_name)
        
        if os.path.exists(old_path):
            print(f"\n📁 Movendo: {old_name} -> projects/{new_name}")
            
            # Mover apenas arquivos essenciais
            essential_extensions = ['.py', '.ipynb', '.sql', '.md', '.txt', 
                                  '.json', '.csv', '.png', '.jpg', '.jpeg', 
                                  '.gif', '.html', '.css', '.js']
            
            for root, dirs, files in os.walk(old_path):
                for file in files:
                    if any(file.endswith(ext) for ext in essential_extensions):
                        src = os.path.join(root, file)
                        # Calcular caminho relativo
                        rel_path = os.path.relpath(root, old_path)
                        dst_dir = os.path.join(new_path, rel_path)
                        os.makedirs(dst_dir, exist_ok=True)
                        dst = os.path.join(dst_dir, file)
                        
                        try:
                            shutil.copy2(src, dst)
                            print(f"  📄 Copiado: {file}")
                        except Exception as e:
                            print(f"  ⚠️  Erro copiando {file}: {e}")
            
            # Copiar pastas assets de cada projeto
            old_assets = os.path.join(old_path, "assets")
            new_assets = os.path.join(new_path, "assets")
            if os.path.exists(old_assets):
                shutil.copytree(old_assets, new_assets, dirs_exist_ok=True)
                print(f"  🎨 Assets copiados")
    
    print("\n✅ Movimentação de arquivos concluída!")

def clean_unnecessary_files(base_path):
    """Remove arquivos desnecessários para portfolio"""
    
    print("\n🧹 Limpando arquivos desnecessários...")
    
    patterns_to_remove = [
        "**/__pycache__",
        "**/.ipynb_checkpoints",
        "**/.pytest_cache",
        "**/*.pyc",
        "**/*.pyo",
        "**/*.pyd",
        "**/.Python",
        "**/venv/",
        "**/env/",
        "**/.env",
        "**/.vscode",
        "**/.idea",
        "**/*.log",
        "**/node_modules"
    ]
    
    total_removed = 0
    for pattern in patterns_to_remove:
        for path in Path(base_path).glob(pattern):
            if path.is_dir():
                try:
                    shutil.rmtree(path, ignore_errors=True)
                    print(f"  🗑️  Removida pasta: {path.relative_to(base_path)}")
                    total_removed += 1
                except Exception as e:
                    print(f"  ⚠️  Erro removendo pasta {path}: {e}")
            else:
                try:
                    path.unlink(missing_ok=True)
                    print(f"  🗑️  Removido arquivo: {path.relative_to(base_path)}")
                    total_removed += 1
                except Exception as e:
                    print(f"  ⚠️  Erro removendo arquivo {path}: {e}")
    
    print(f"✅ Total removido: {total_removed} itens")

def create_project_readmes(base_path):
    """Cria READMEs consistentes para cada projeto"""
    
    project_templates = {
        "01-real-estate-sp": """# 🏠 Real Estate SP Analytics

Dashboard interativo para análise de preços de imóveis em São Paulo.

## 🚀 Features
- 📊 Análise exploratória de dados
- 🗺️ Visualização geográfica
- 📈 Previsão de preços
- 🎯 Filtros interativos

## 🛠️ Tecnologias
- Python
- Streamlit
- GeoPandas
- Scikit-learn

## 📦 Instalação

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🔗 Live Demo
https://01-sp-housing-aldber.streamlit.app/
""",

        "02-sql-analytics": """# 💰 SQL Analytics & Optimization

Análises avançadas com PostgreSQL e otimização de queries.

## 📊 Projetos
- **Análise de Vendas** - Window functions, CTEs
- **Otimização de Performance** - Indexes, query tuning
- **ETL Pipeline** - Data transformation
- **Business Intelligence** - Relatórios analíticos

## 🛠️ Tecnologias
- PostgreSQL
- Python (psycopg2)
- Jupyter Notebook

## 🎯 Habilidades Demonstradas
- ✅ Complex queries
- ✅ Performance optimization
- ✅ Data modeling
- ✅ ETL processes
""",

        "03-sales-dashboard": """# 📊 Sales Intelligence Dashboard

Dashboard premium para análise de performance de vendas.

## 🚀 Features
- 📈 5 tipos de gráficos interativos
- 🎨 Dark/Light mode toggle
- 🔧 Filtros avançados
- ⚡ KPIs em tempo real

## 🛠️ Tecnologias
- Dash
- Plotly
- Pandas
- Bootstrap

## 📦 Instalação
```bash
pip install -r requirements.txt
python app.py
# Acesse: http://127.0.0.1:8050
```

## 🎨 Preview
![Dashboard Preview](assets/dash_01.png)
""",

        "04-cyber-finance-guardian": """# 🔐 CyberFinance Guardian

Sistema de segurança cibernética para análise de transações financeiras.

## 🚀 Status
🚧 **Em desenvolvimento**

## 🎯 Objetivos
- Detecção de fraudes em tempo real
- Análise comportamental
- Compliance financeiro
- Monitoramento de transações

## 🛠️ Tecnologias Previstas
- Python
- Machine Learning
- Security Analytics
- APIs REST
""",

        "05-aws-security-labs": """# ☁️ AWS Security Labs

Laboratórios práticos de segurança na nuvem AWS.

## 🚀 Status
🚧 **Em desenvolvimento**

## 🎯 Objetivos
- Hardening de instâncias EC2
- Configuração de Security Groups
- Monitoramento com CloudWatch
- Automação com Lambda

## 🛠️ Tecnologias Previstas
- AWS (EC2, S3, IAM, CloudWatch)
- Python (Boto3)
- Infrastructure as Code
- Security Best Practices
"""
    }

    for project, content in project_templates.items():
        readme_path = os.path.join(base_path, "projects", project, "README.md")
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ README criado: projects/{project}/README.md")

def update_root_readme(base_path):
    """Atualiza README principal com nova estrutura"""

    readme_content = """# 🚀 Aldo Bernardi - Data Science & Cybersecurity Portfolio

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-success)](https://aldber.github.io/DataScience-Portfolio/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## 🌐 Live Portfolio
[https://aldber.github.io/DataScience-Portfolio/](https://aldber.github.io/DataScience-Portfolio/)

## 📊 Projetos em Destaque

| Projeto | Descrição | Tecnologias | Demo |
|---------|-----------|------------|------|
| 🏠 Real Estate Analytics | Dashboard de preços de imóveis | Streamlit, GeoPandas | [Live Demo](https://01-sp-housing-aldber.streamlit.app/) |
| 💰 SQL Analytics | Queries avançadas e otimização | PostgreSQL, Python | [Código](projects/02-sql-analytics/) |
| 📊 Sales Dashboard | Dashboard interativo de vendas | Dash, Plotly, Bootstrap | [Preview](projects/03-sales-dashboard/) |
| 🔐 CyberFinance Guardian | Cybersecurity + Finanças | Python, Security | 🚧 Em breve |
| ☁️ AWS Security Labs | Laboratórios de cloud security | AWS, Security | 🚧 Em breve |

## 🛠️ Tech Stack

### 📊 Data Science & Analytics
- Python (Pandas, NumPy, Scikit-learn)
- SQL (PostgreSQL, Query Optimization)
- Visualização (Plotly, Dash, Streamlit)

### ☁️ Cloud & DevOps
- AWS (EC2, S3, Lambda, Cloud Practitioner)
- Docker (Containerização)
- Git/GitHub (CI/CD, Versionamento)

### 🔐 Cybersecurity
- Network Security (CCNA1 em andamento)
- Security Analytics
- Compliance & Privacy

## 📈 Business Impact

| Projeto | Impacto | Métricas |
|---------|---------|----------|
| Real Estate | +15% precisão em precificação | ML models, geospatial analysis |
| SQL Optimization | -60% tempo de execução | Query tuning, indexes |
| Sales Dashboard | 5+ visualizações interativas | Real-time KPIs, filtering |

## 🎓 Learning Journey
- **Data Science**: Análise de dados, Machine Learning, Visualização
- **Databases**: SQL avançado, Otimização, Modelagem
- **Cybersecurity**: Fundamentos, Cloud Security, Network Security
- **Cloud Computing**: AWS, Infraestrutura como código, DevOps

## 📫 Contact
- 📧 Email: aldo.bernardi@gmail.com
- 💼 LinkedIn: [Aldo Bernardi](https://linkedin.com/in/aldobernardi)
- 🔗 GitHub: [@AldBer](https://github.com/AldBer)
- 🏆 Credly: [Badges](https://www.credly.com/users/aldo-bernardi)

## 📄 License
MIT License - Veja [LICENSE](LICENSE) para detalhes.
"""

    with open(os.path.join(base_path, "README.md"), 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("✅ README principal atualizado!")

def create_backup(base_path):
    """Cria backup da estrutura atual antes de modificar"""
    import datetime
    
    backup_dir = os.path.join(base_path, f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}")
    print(f"\n💾 Criando backup em: {backup_dir}")
    
    # Copiar estrutura atual (exceto backups antigos)
    for item in os.listdir(base_path):
        if item.startswith("backup_"):
            continue
            
        src = os.path.join(base_path, item)
        dst = os.path.join(backup_dir, item)
        
        if os.path.isdir(src):
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns('__pycache__', '.git', '*.pyc'))
        else:
            shutil.copy2(src, dst)
    
    print(f"✅ Backup criado com sucesso!")
    return backup_dir

def main():
    """Função principal"""
    base_path = os.getcwd()
    
    print("=" * 60)
    print("🎯 REORGANIZAÇÃO DO PORTFÓLIO - SCRIPT DE MIGRAÇÃO")
    print("=" * 60)
    
    print("\n⚠️ AVISO: Este script irá modificar a estrutura do seu portfolio.")
    print("📋 Ações que serão executadas:")
    print("   1. Criar backup da estrutura atual")
    print("   2. Criar nova organização de pastas")
    print("   3. Mover arquivos para nova estrutura")
    print("   4. Limpar arquivos desnecessários")
    print("   5. Criar documentação consistente")
    
    confirm = input("\n❓ Continuar com a reorganização? (s/n): ").strip().lower()
    if confirm != 's':
        print("🚫 Operação cancelada.")
        sys.exit(0)
    
    # 0. Criar backup
    print("\n0. 💾 Criando backup...")
    backup_path = create_backup(base_path)
    
    # 1. Criar nova estrutura
    print("\n1. 🏗️ Criando nova estrutura de pastas...")
    create_new_structure(base_path)
    
    # 2. Mover arquivos
    print("\n2. 📁 Movendo arquivos para nova estrutura...")
    move_project_files(base_path)
    
    # 3. Limpar arquivos desnecessários
    print("\n3. 🧹 Limpando arquivos de desenvolvimento...")
    clean_unnecessary_files(base_path)
    
    # 4. Criar READMEs
    print("\n4. 📝 Criando documentação consistente...")
    create_project_readmes(base_path)
    
    # 5. Atualizar README principal
    print("\n5. 🔄 Atualizando README principal...")
    update_root_readme(base_path)
    
    print("\n" + "=" * 60)
    print("🎉 REORGANIZAÇÃO CONCLUÍDA!")
    print("=" * 60)
    
    print(f"\n💾 Backup salvo em: {backup_path}")
    
    print("\n📋 Próximos passos manuais:")
    print("1. 📄 Adicionar index.html na raiz (landing page)")
    print("2. ⚙️ Configurar GitHub Pages em Settings > Pages")
    print("3. 🔗 Testar: https://aldber.github.io/DataScience-Portfolio/")
    print("4. 🚀 Commit e push das mudanças")
    print("\n✅ Arquivos de backup mantidos caso precise restaurar.")

if __name__ == "__main__":
    main()
```

## Principais melhorias que fiz:

1. **Correção de indentação** - O código original tinha problemas graves de indentação, especialmente nas funções `create_project_readmes` e `main`.

2. **Adição de função de backup** - Incluí uma função `create_backup()` que cria um backup automático antes de modificar qualquer arquivo.

3. **READMEs melhorados** - Corrigi a formatação dos READMEs e adicionei templates para todos os 5 projetos.

4. **Tratamento de erros aprimorado** - Adicionei mais `try-except` para evitar falhas.

5. **Instruções mais claras** - Mensagens de confirmação e status mais informativas.

6. **Caminhos relativos** - Uso de `relative_to()` para mostrar caminhos mais legíveis.

7. **Formatação consistente** - Correção da formatação Markdown nos READMEs.

8. **Padronização de encoding** - Todas as operações de arquivo usam `utf-8`.