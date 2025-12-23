# app_test.py - VERSÃO CORRIGIDA
from dash import Dash, html, dcc, Input, Output, callback  
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ====================
# DADOS SIMULADOS (PARA TESTE)
# ====================

def create_sample_data():
    """Cria dados de exemplo para teste rápido"""
    dates = pd.date_range(start='2024-01-01', end=datetime.today(), freq='D')
    
    data = []
    for date in dates:
        data.append({
            'date': date,
            'product': np.random.choice(['Produto A', 'Produto B', 'Produto C']),
            'category': np.random.choice(['Eletrônicos', 'Roupas', 'Casa']),
            'region': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste']),
            'sales': np.random.randint(100, 5000),
            'units': np.random.randint(1, 50)
        })
    
    return pd.DataFrame(data)

# ====================
# APLICAÇÃO PRINCIPAL
# ====================

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Dados de exemplo
df = create_sample_data()

app.layout = html.Div([
    dbc.NavbarSimple(
        brand="📊 Dashboard de Vendas - TESTE",
        color="primary",
        dark=True,
    ),
    
    # KPIs
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("💰 Vendas Totais"),
                html.H3(f"R$ {df['sales'].sum():,.2f}")
            ])
        ]), width=3),
        
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("📦 Total Produtos"),
                html.H3(f"{df['units'].sum():,}")
            ])
        ]), width=3),
        
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("🏪 Regiões"),
                html.H3(f"{df['region'].nunique()}")
            ])
        ]), width=3),
        
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("📈 Ticket Médio"),
                html.H3(f"R$ {df['sales'].mean():.2f}")
            ])
        ]), width=3),
    ], style={"margin": "20px"}),
    
    # Filtros
    dbc.Row([
        dbc.Col([
            html.Label("Período:"),
            dcc.DatePickerRange(
                id='date-picker',
                start_date=df['date'].min(),
                end_date=df['date'].max()
            )
        ], width=6),
        
        dbc.Col([
            html.Label("Produto:"),
            dcc.Dropdown(
                id='product-filter',
                options=[{'label': p, 'value': p} for p in df['product'].unique()],
                multi=True
            )
        ], width=6),
    ], style={"margin": "20px"}),
    
    # Gráficos
    dbc.Row([
        dbc.Col(dcc.Graph(id='sales-trend'), width=12),
    ]),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='products-chart'), width=6),
        dbc.Col(dcc.Graph(id='regions-chart'), width=6),
    ]),
])

# Callbacks
@app.callback(
    [Output('sales-trend', 'figure'),
     Output('products-chart', 'figure'),
     Output('regions-chart', 'figure')],
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date'),
     Input('product-filter', 'value')]
)
def update_charts(start_date, end_date, products):
    filtered_df = df.copy()
    
    # Aplicar filtros
    if start_date and end_date:
        filtered_df = filtered_df[
            (filtered_df['date'] >= start_date) & 
            (filtered_df['date'] <= end_date)
        ]
    
    if products:
        filtered_df = filtered_df[filtered_df['product'].isin(products)]
    
    # Gráfico 1: Tendência
    daily_sales = filtered_df.groupby('date')['sales'].sum().reset_index()
    trend_fig = px.line(daily_sales, x='date', y='sales', title='Tendência de Vendas')
    
    # Gráfico 2: Produtos
    product_sales = filtered_df.groupby('product')['sales'].sum().reset_index()
    product_fig = px.pie(product_sales, values='sales', names='product', title='Vendas por Produto')
    
    # Gráfico 3: Regiões
    region_sales = filtered_df.groupby('region')['sales'].sum().reset_index()
    region_fig = px.bar(region_sales, x='region', y='sales', title='Vendas por Região')
    
    return trend_fig, product_fig, region_fig

if __name__ == '__main__':
    print("🚀 Iniciando Dashboard...")
    print("📊 Acesse: http://localhost:8050")
    print("🌐 Ou: http://127.0.0.1:8050")
    
    # ✅ CORREÇÃO: app.run() em vez de app.run_server()
    # ✅ CORREÇÃO: host='0.0.0.0' para permitir acesso
    app.run(
        debug=True, 
        port=8050, 
        host='127.0.0.1'  # Ou '0.0.0.0' para rede local
    )