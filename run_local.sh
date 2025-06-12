#!/bin/bash

# 1. Navegar até a pasta do portfólio
cd /f/Documents/04.\ Cursos/17.Python/05.Portfolio

# 2. Ativar ambiente Conda (se aplicável)
conda activate ds_env  # Substitua pelo nome do seu ambiente

# 3. Instalar dependências do Jekyll (se necessário)
if ! command -v bundle &> /dev/null; then
    gem install bundler jekyll
fi

# 4. Instalar dependências do projeto
bundle install
pip install -r requirements.txt  # Crie este arquivo se necessário

# 5. Iniciar servidor local
bundle exec jekyll serve --livereload

