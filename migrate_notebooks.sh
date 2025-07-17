#!/bin/bash

# Função para migrar notebooks
migrate_notebook() {
    local src=$1
    local dest=$2
    local title=$3
    local tags=$4
    local convert_md=$5
    
    echo "Migrando: $src para $dest"
    
    # Cria diretório de destino se não existir
    mkdir -p "$(dirname "$dest")"
    
    if [ "$convert_md" = "true" ]; then
        # Converte para markdown (preserva código)
        jupyter nbconvert --to markdown "$src" --output "$(basename "$dest" .ipynb)"
        mv "$(dirname "$src")/$(basename "$dest" .ipynb).md" "$dest.md"
        
        # Adiciona metadados
        echo -e "---\ntitle: $title\ntags: [$tags]\n---\n\n$(cat "$dest.md")" > "$dest.md"
        echo "Convertido para Markdown: $dest.md"
    else
        # Copia o notebook original
        cp "$src" "$dest"
        echo "Arquivo copiado como notebook: $dest"
    fi
}

# Exemplo de uso:
# migrate_notebook \
#    "-s 01_California_Housing/notebooks/california_housing.ipynb" \
#    "-d 01_SP_Housing/notebooks/01_EDA.ipynb" \
#    "-a 'Análise Exploratória'" \
#    "-t 'python, pandas'" \
#    "-m true"