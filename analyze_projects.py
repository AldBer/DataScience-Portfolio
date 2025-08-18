#!/usr/bin/env python3
"""
Análise e Migração de Projetos do Dashboards
Identifica, analisa e migra projetos da pasta dashboards para a nova estrutura

Autor: Claude AI Assistant
Data: 2025-08-18
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime

class ProjectAnalyzer:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path).resolve()
        self.dashboards_path = self.base_path / "dashboards"
        self.analysis_results = {}
        
    def analyze_project_folder(self, project_path):
        """Analisa uma pasta de projeto e determina seu valor e tipo"""
        project_path = Path(project_path)
        analysis = {
            "name": project_path.name,
            "path": str(project_path),
            "type": "unknown",
            "files": [],
            "notebooks": [],
            "apps": [],
            "data_files": [],
            "assets": [],
            "size_mb": 0,
            "complexity_score": 0,
            "recommendation": "",
            "new_location": ""
        }
        
        if not project_path.exists():
            analysis["recommendation"] = "SKIP - Path does not exist"
            return analysis
        
        # Analizar conteúdo
        total_size = 0
        for file_path in project_path.rglob("*"):
            if file_path.is_file():
                try:
                    file_size = file_path.stat().st_size
                    total_size += file_size
                    
                    relative_path = file_path.relative_to(project_path)
                    file_info = {
                        "name": file_path.name,
                        "path": str(relative_path),
                        "size": file_size,
                        "extension": file_path.suffix.lower()
                    }
                    
                    # Categorizar arquivos
                    if file_path.suffix.lower() == '.ipynb':
                        analysis["notebooks"].append(file_info)
                        analysis["complexity_score"] += 3
                    elif file_path.suffix.lower() == '.py':
                        analysis["apps"].append(file_info)
                        analysis["complexity_score"] += 2
                        if 'streamlit' in file_path.read_text(encoding='utf-8', errors='ignore').lower():
                            analysis["type"] = "streamlit_app"
                    elif file_path.suffix.lower() in ['.csv', '.json', '.xlsx', '.parquet']:
                        analysis["data_files"].append(file_info)
                        analysis["complexity_score"] += 1
                    elif file_path.suffix.lower() in ['.png', '.jpg', '.jpeg', '.svg', '.html']:
                        analysis["assets"].append(file_info)
                        analysis["complexity_score"] += 0.5
                    
                    analysis["files"].append(file_info)
                    
                except (OSError, UnicodeDecodeError, PermissionError):
                    continue
        
        analysis["size_mb"] = round(total_size / (1024*1024), 2)
        
        # Determinar tipo de projeto
        if analysis["notebooks"] and analysis["apps"]:
            analysis["type"] = "full_analysis_with_app"
        elif analysis["notebooks"]:
            analysis["type"] = "analysis_project"
        elif analysis["apps"]:
            analysis["type"] = "app_project"
        elif analysis["data_files"]:
            analysis["type"] = "data_project"
        
        # Fazer recomendação
        self._make_recommendation(analysis)
        
        return analysis
    
    def _make_recommendation(self, analysis):
        """Determina recomendação para o projeto"""
        name = analysis["name"].lower()
        complexity = analysis["complexity_score"]
        
        # Projetos específicos conhecidos
        if "housing" in name or "sp_housing" in name or "imob" in name:
            analysis["recommendation"] = "MIGRATE - Real Estate Analysis"
            analysis["new_location"] = "01-real-estate-sp"
            
        elif "crypto" in name or "bitcoin" in name or "trading" in name:
            analysis["recommendation"] = "MIGRATE - Crypto Analysis"
            analysis["new_location"] = "02-crypto-monitoring"
            
        elif "sql" in name or "bi" in name or "power" in name:
            analysis["recommendation"] = "MIGRATE - SQL/BI Project"
            analysis["new_location"] = "03-sql-projects"
            
        elif "ml" in name or "machine" in name or "model" in name:
            analysis["recommendation"] = "MIGRATE - ML Project"
            analysis["new_location"] = "04-machine-learning"
            
        # Por complexidade e conteúdo
        elif complexity >= 5:
            analysis["recommendation"] = "MIGRATE - High Value Project"
            analysis["new_location"] = f"05-{name.replace('_', '-').replace(' ', '-')}"
            
        elif complexity >= 2:
            analysis["recommendation"] = "REVIEW - Medium Value Project"
            analysis["new_location"] = f"experimental/{name}"
            
        elif analysis["size_mb"] > 50:
            analysis["recommendation"] = "REVIEW - Large Project (check content)"
            
        else:
            analysis["recommendation"] = "SKIP - Low complexity or empty"
    
    def scan_dashboards_folder(self):
        """Escaneia todos os projetos na pasta dashboards"""
        print(f"🔍 Analisando projetos em: {self.dashboards_path}")
        
        if not self.dashboards_path.exists():
            print("❌ Pasta dashboards não encontrada!")
            return
        
        for item in self.dashboards_path.iterdir():
            if item.is_dir() and item.name != "__pycache__":
                print(f"\n📊 Analisando: {item.name}")
                analysis = self.analyze_project_folder(item)
                self.analysis_results[item.name] = analysis
                
                # Mostrar resultado imediato
                print(f"   Tipo: {analysis['type']}")
                print(f"   Arquivos: {len(analysis['files'])}")
                print(f"   Notebooks: {len(analysis['notebooks'])}")
                print(f"   Apps: {len(analysis['apps'])}")
                print(f"   Tamanho: {analysis['size_mb']} MB")
                print(f"   Complexidade: {analysis['complexity_score']}")
                print(f"   👉 {analysis['recommendation']}")
    
    def generate_migration_plan(self):
        """Gera plano de migração baseado na análise"""
        print("\n" + "="*60)
        print("📋 PLANO DE MIGRAÇÃO DOS PROJETOS")
        print("="*60)
        
        to_migrate = []
        to_review = []
        to_skip = []
        
        for project_name, analysis in self.analysis_results.items():
            if analysis["recommendation"].startswith("MIGRATE"):
                to_migrate.append((project_name, analysis))
            elif analysis["recommendation"].startswith("REVIEW"):
                to_review.append((project_name, analysis))
            else:
                to_skip.append((project_name, analysis))
        
        # Projetos para migrar
        if to_migrate:
            print("\n🚀 MIGRAR IMEDIATAMENTE (Alto Valor):")
            for project_name, analysis in to_migrate:
                print(f"\n📁 {project_name}")
                print(f"   └─ Para: {analysis['new_location']}")
                print(f"   └─ Tipo: {analysis['type']}")
                print(f"   └─ Arquivos importantes:")
                
                for notebook in analysis["notebooks"][:3]:  # Top 3
                    print(f"      • {notebook['name']}")
                for app in analysis["apps"][:2]:  # Top 2
                    print(f"      • {app['name']}")
        
        # Projetos para revisar
        if to_review:
            print(f"\n🔍 REVISAR MANUALMENTE ({len(to_review)} projetos):")
            for project_name, analysis in to_review:
                print(f"   • {project_name} - {analysis['recommendation']}")
        
        # Projetos para pular
        if to_skip:
            print(f"\n⏭️ PULAR ({len(to_skip)} projetos):")
            for project_name, analysis in to_skip:
                print(f"   • {project_name} - {analysis['recommendation']}")
        
        return to_migrate, to_review, to_skip
    
    def execute_migration(self, projects_to_migrate):
        """Executa a migração dos projetos selecionados"""
        print("\n" + "="*60)
        print("🚀 EXECUTANDO MIGRAÇÃO")
        print("="*60)
        
        for project_name, analysis in projects_to_migrate:
            source_path = Path(analysis["path"])
            target_path = self.base_path / analysis["new_location"]
            
            print(f"\n📦 Migrando: {project_name}")
            print(f"   {source_path} -> {target_path}")
            
            try:
                # Criar diretório destino
                target_path.mkdir(parents=True, exist_ok=True)
                
                # Copiar conteúdo
                for item in source_path.iterdir():
                    dest_item = target_path / item.name
                    if item.is_dir():
                        if dest_item.exists():
                            shutil.rmtree(dest_item)
                        shutil.copytree(item, dest_item)
                    else:
                        shutil.copy2(item, dest_item)
                
                # Criar README se não existir
                readme_path = target_path / "README.md"
                if not readme_path.exists():
                    self._create_project_readme(readme_path, project_name, analysis)
                
                print(f"   ✅ Migrado com sucesso!")
                
            except Exception as e:
                print(f"   ❌ Erro na migração: {e}")
    
    def _create_project_readme(self, readme_path, project_name, analysis):
        """Cria README para projeto migrado"""
        content = f"""# {project_name.replace('_', ' ').title()}

## 📊 Visão Geral
{self._get_project_description(project_name, analysis)}

## 🛠️ Tecnologias Identificadas
{self._get_technologies(analysis)}

## 📁 Estrutura do Projeto
```
{project_name}/
├── README.md              # Este arquivo
{self._get_structure_tree(analysis)}
```

## 🚀 Como Executar
{self._get_execution_instructions(analysis)}

## 📈 Arquivos Principais
{self._get_main_files(analysis)}

---
**Migrado automaticamente em**: {datetime.now().strftime('%Y-%m-%d')}  
**Análise**: {analysis['recommendation']}
"""
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _get_project_description(self, name, analysis):
        """Gera descrição baseada no nome e conteúdo"""
        name_lower = name.lower()
        if "housing" in name_lower or "imob" in name_lower:
            return "Análise de dados imobiliários com visualizações interativas e insights de mercado."
        elif "crypto" in name_lower:
            return "Sistema de monitoramento e análise de criptomoedas."
        elif "sql" in name_lower:
            return "Projeto de análise de dados usando SQL e Business Intelligence."
        else:
            return f"Projeto de ciência de dados com {len(analysis['files'])} arquivos e complexidade {analysis['complexity_score']}."
    
    def _get_technologies(self, analysis):
        """Identifica tecnologias baseado nos arquivos"""
        techs = []
        if analysis["notebooks"]:
            techs.append("- Jupyter Notebooks")
        if analysis["apps"]:
            techs.append("- Python")
            if analysis["type"] == "streamlit_app":
                techs.append("- Streamlit")
        if analysis["data_files"]:
            techs.append("- Pandas (provável)")
        if any(f["extension"] in [".png", ".jpg", ".html"] for f in analysis["assets"]):
            techs.append("- Plotly/Matplotlib")
        
        return "\n".join(techs) if techs else "- Python\n- Pandas"
    
    def _get_structure_tree(self, analysis):
        """Gera árvore de estrutura"""
        lines = []
        if analysis["apps"]:
            lines.extend([f"├── {app['name']:<20} # Aplicação principal" for app in analysis["apps"][:2]])
        if analysis["notebooks"]:
            lines.extend([f"├── {nb['name']:<20} # Análise" for nb in analysis["notebooks"][:3]])
        return "\n".join(lines)
    
    def _get_execution_instructions(self, analysis):
        """Gera instruções de execução"""
        if analysis["type"] == "streamlit_app":
            return """1. Instalar dependências:
```bash
pip install streamlit pandas plotly
```

2. Executar aplicação:
```bash
streamlit run app.py
```"""
        else:
            return """1. Instalar dependências:
```bash
pip install pandas numpy matplotlib jupyter
```

2. Executar notebooks:
```bash
jupyter notebook
```"""
    
    def _get_main_files(self, analysis):
        """Lista arquivos principais"""
        files = []
        for nb in analysis["notebooks"][:3]:
            files.append(f"- **{nb['name']}**: Análise exploratória")
        for app in analysis["apps"][:2]:
            files.append(f"- **{app['name']}**: Aplicação interativa")
        return "\n".join(files) if files else "- Aguardando catalogação manual"
    
    def save_analysis_report(self):
        """Salva relatório completo da análise"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_projects": len(self.analysis_results),
            "base_path": str(self.base_path),
            "projects": self.analysis_results
        }
        
        report_path = self.base_path / "project_analysis_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Relatório salvo em: {report_path}")

def main():
    print("🔍 ANÁLISE DE PROJETOS DO DASHBOARDS")
    print("="*50)
    
    analyzer = ProjectAnalyzer()
    
    # Escanear projetos
    analyzer.scan_dashboards_folder()
    
    if not analyzer.analysis_results:
        print("\n❌ Nenhum projeto encontrado na pasta dashboards.")
        return
    
    # Gerar plano de migração
    to_migrate, to_review, to_skip = analyzer.generate_migration_plan()
    
    # Salvar relatório
    analyzer.save_analysis_report()
    
    # Perguntar se quer executar migração
    if to_migrate:
        print(f"\n📤 Encontrados {len(to_migrate)} projetos de alto valor para migrar.")
        response = input("Deseja executar a migração automaticamente? (s/N): ").lower().strip()
        
        if response == 's':
            analyzer.execute_migration(to_migrate)
            print("\n🎉 Migração concluída!")
        else:
            print("\n📋 Plano de migração salvo. Execute manualmente quando estiver pronto.")
    
    print(f"\n✅ Análise completa! Verifique o relatório para mais detalhes.")

if __name__ == "__main__":
    main()