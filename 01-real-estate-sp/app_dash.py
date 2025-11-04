# app_dash.py - VERSÃO FINAL PARA DEPLOY
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import json
import os

app = dash.Dash(__name__)

def load_data():
    """Carrega dados - adaptado para Streamlit Cloud"""
    try:
        possible_paths = [
            "data/processed/precos_por_distrito.json",
            "../data/processed/precos_por_distrito.json",
            "precos_por_distrito.json"
        ]
        
        for json_path in possible_paths:
            if os.path.exists(json_path):
                with open(json_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        
        # Fallback para dados de exemplo
        return {
            'precos_por_distrito': {
                'Centro': {'preco_medio': 500000, 'quantidade_imoveis': 150},
                'Pinheiros': {'preco_medio': 800000, 'quantidade_imoveis': 200},
                'Moema': {'preco_medio': 1200000, 'quantidade_imoveis': 80},
            },
            'total_distritos': 3,
            'total_imoveis_processados': 430,
            'preco_medio_geral': 833333
        }
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None

# Carregar dados
dados = load_data()

if dados:
    # Layout do app
    df = pd.DataFrame.from_dict(dados['precos_por_distrito'], orient='index')
    df = df.reset_index().rename(columns={'index': 'distrito'})
    
    app.layout = html.Div([
        html.H1("🏠 Dashboard de Imóveis SP - DASH", 
                style={'textAlign': 'center', 'color': '#2E86AB'}),
        
        # Métricas
        html.Div([
            html.Div([
                html.H3(dados['total_distritos'], style={'color': '#A23B72'}),
                html.P("Distritos")
            ], style={'textAlign': 'center', 'margin': '10px'}),
            html.Div([
                html.H3(dados['total_imoveis_processados'], style={'color': '#F18F01'}),
                html.P("Imóveis")
            ], style={'textAlign': 'center', 'margin': '10px'}),
            html.Div([
                html.H3(f"R$ {dados['preco_medio_geral']:,.0f}", style={'color': '#C73E1D'}),
                html.P("Preço Médio")
            ], style={'textAlign': 'center', 'margin': '10px'}),
        ], style={'display': 'flex', 'justifyContent': 'space-around', 'margin': '20px'}),
        
        # Gráfico
        dcc.Graph(
            figure=px.bar(
                df,
                x='distrito',
                y='preco_medio',
                title="Preços Médios por Distrito",
                labels={'distrito': 'Distrito', 'preco_medio': 'Preço Médio (R$)'},
                color='preco_medio',
                color_continuous_scale='Viridis'
            ).update_layout(height=500)
        ),
        
        # Tabela
        html.Div([
            html.H3("📊 Dados Detalhados", style={'textAlign': 'center'}),
            html.Table([
                html.Tr([
                    html.Th("Distrito", style={'padding': '10px'}),
                    html.Th("Preço Médio", style={'padding': '10px'}),
                    html.Th("Qtd Imóveis", style={'padding': '10px'})
                ])
            ] + [
                html.Tr([
                    html.Td(distrito, style={'padding': '8px', 'border': '1px solid #ddd'}),
                    html.Td(f"R$ {data['preco_medio']:,.0f}", style={'padding': '8px', 'border': '1px solid #ddd'}),
                    html.Td(data['quantidade_imoveis'], style={'padding': '8px', 'border': '1px solid #ddd'})
                ]) for distrito, data in dados['precos_por_distrito'].items()
            ], style={'margin': '20px auto', 'borderCollapse': 'collapse'})
        ], style={'textAlign': 'center', 'margin': '30px'})
    ])

else:
    app.layout = html.Div([
        html.H1("❌ Erro ao carregar dados"),
        html.P("Verifique se os arquivos de dados estão no lugar correto.")
    ])

if __name__ == '__main__':
    # ⚠️ SEM DEBUG - funciona no Streamlit Cloud
    app.run(host='0.0.0.0', port=8050, debug=False)