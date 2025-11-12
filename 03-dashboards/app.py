# app.py - VERSÃO SIMPLIFICADA E FUNCIONAL
from dash import Dash, html, dcc, Input, Output, callback  
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ====================
# 1. APLICAÇÃO PRINCIPAL
# ====================
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# ====================
# 2. DADOS
# ====================
def create_premium_data():
    dates = pd.date_range(start='2024-01-01', end=datetime.today(), freq='D')
    products = ['Smartphone', 'Notebook', 'Tablet', 'Smartwatch', 'Fones']
    regions = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
    categories = ['Eletrônicos', 'Acessórios', 'Gadgets']
    
    data = []
    for date in dates:
        for product in products:
            data.append({
                'date': date,
                'product': product,
                'category': np.random.choice(categories),
                'region': np.random.choice(regions),
                'sales': np.random.randint(500, 10000),
                'units': np.random.randint(1, 25),
                'profit': np.random.randint(100, 2000),
                'customer_rating': np.random.uniform(3.0, 5.0)
            })
    
    df = pd.DataFrame(data)
    df['profit_margin'] = (df['profit'] / df['sales'] * 100).round(2)
    return df

df = create_premium_data()

# ====================
# 3. COMPONENTES
# ====================
def create_kpi_card(icon, title, value, change, change_type="positive"):
    color = "success" if change_type == "positive" else "danger"
    arrow = "↗️" if change_type == "positive" else "↘️"
    
    return dbc.Card([
        dbc.CardBody([
            html.Div([
                html.H4(icon, className="me-2"),
                html.H5(title, className="text-muted")
            ], className="d-flex justify-content-between align-items-start"),
            
            html.Div([
                html.H2(value, className="card-value mb-1"),
                html.Small([
                    html.Span(f"{arrow} {change}", className=f"text-{color}"),
                    html.Span(" vs último mês", className="text-muted")
                ])
            ])
        ])
    ], className="h-100")

def create_chart_card(title, chart_id, width=6):
    return dbc.Col([
        dbc.Card([
            dbc.CardHeader(title, className="fw-bold"),
            dbc.CardBody(dcc.Graph(id=chart_id))
        ])
    ], width=width)

# ====================
# 4. LAYOUT
# ====================
app.layout = dbc.Container(fluid=True, id="main-container", children=[
    
    # 🔝 HEADER COM TOGGLE 
    dbc.Row([
        dbc.Col([
            html.H1("📊 Dashboard de Performance de Vendas", 
                   className="text-primary my-4"),
            html.P("Análise em tempo real do desempenho comercial", 
                  className="text-muted lead")
        ], width=10),
        
        dbc.Col([
            html.Div([
                html.Span("🌙", style={'fontSize': '20px', 'marginRight': '10px'}),
                dbc.Switch(id="dark-mode-toggle", value=False, className="me-2"),
                html.Span("☀️", style={'fontSize': '20px', 'marginLeft': '10px'})
            ], style={
                'display': 'flex', 
                'alignItems': 'center',
                'justifyContent': 'flex-end',
                'height': '100%',
                'paddingTop': '2rem'
            })
        ], width=2)
    ], className="align-items-center"),
    
    # 📈 LINHA DE KPIs
    dbc.Row([
        dbc.Col(create_kpi_card("💰", "Receita Total", "R$ 2.5M", "+12.5%"), width=3),
        dbc.Col(create_kpi_card("📦", "Unidades Vendidas", "45.2K", "+8.3%"), width=3),
        dbc.Col(create_kpi_card("👥", "Clientes Ativos", "12.4K", "+15.2%"), width=3),
        dbc.Col(create_kpi_card("🎯", "Ticket Médio", "R$ 215", "+5.7%"), width=3),
    ], className="mb-4"),
    
    # 🎛️ FILTROS
    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.Label("📅 Período", className="fw-bold"),
                    dcc.DatePickerRange(
                        id='date-picker',
                        start_date=df['date'].min(),
                        end_date=df['date'].max(),
                        className="w-100"
                    )
                ], width=3),
                
                dbc.Col([
                    html.Label("📦 Produtos", className="fw-bold"),
                    dcc.Dropdown(
                        id='product-filter',
                        options=[{'label': p, 'value': p} for p in df['product'].unique()],
                        multi=True,
                        placeholder="Selecione os produtos..."
                    )
                ], width=3),
                
                dbc.Col([
                    html.Label("🌍 Região", className="fw-bold"),
                    dcc.Dropdown(
                        id='region-filter',
                        options=[{'label': r, 'value': r} for r in df['region'].unique()],
                        multi=True,
                        placeholder="Selecione as regiões..."
                    )
                ], width=3),
                
                dbc.Col([
                    html.Label("📊 Categoria", className="fw-bold"),
                    dcc.Dropdown(
                        id='category-filter',
                        options=[{'label': c, 'value': c} for c in df['category'].unique()],
                        multi=True,
                        placeholder="Selecione categorias..."
                    )
                ], width=3),
            ])
        ])
    ], className="mb-4"),
    
    # 📊 PRIMEIRA LINHA DE GRÁFICOS
    dbc.Row([
        create_chart_card("📈 Tendência de Vendas Diárias", "sales-trend", 8),
        create_chart_card("🎯 Margem de Lucro por Produto", "profit-chart", 4),
    ], className="mb-4"),
    
    # 📊 SEGUNDA LINHA DE GRÁFICOS
    dbc.Row([
        create_chart_card("🌍 Vendas por Região", "region-chart", 6),
        create_chart_card("📦 Desempenho por Produto", "product-chart", 6),
    ], className="mb-4"),
    
    # 📊 TERCEIRA LINHA
    dbc.Row([
        create_chart_card("⭐ Avaliação dos Clientes", "rating-chart", 12),
    ]),
    
], style={"minHeight": "100vh"})

# ====================
# 5. CALLBACK
# ====================
@app.callback(
    [Output('sales-trend', 'figure'),
     Output('profit-chart', 'figure'),
     Output('region-chart', 'figure'),
     Output('product-chart', 'figure'),
     Output('rating-chart', 'figure'),
     Output('main-container', 'className')],
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date'),
     Input('product-filter', 'value'),
     Input('region-filter', 'value'),
     Input('category-filter', 'value'),
     Input('dark-mode-toggle', 'value')]
)
def update_dashboard_and_theme(start_date, end_date, products, regions, categories, dark_mode):
    """Callback único para gráficos e tema"""
    
    # 🎨 1. Tema dark/light
    theme_class = "dark-mode" if dark_mode else ""
    
    # 📊 2. Filtrar dados
    filtered_df = df.copy()
    
    if start_date and end_date:
        filtered_df = filtered_df[
            (filtered_df['date'] >= start_date) & 
            (filtered_df['date'] <= end_date)
        ]
    
    if products:
        filtered_df = filtered_df[filtered_df['product'].isin(products)]
    
    if regions:
        filtered_df = filtered_df[filtered_df['region'].isin(regions)]
        
    if categories:
        filtered_df = filtered_df[filtered_df['category'].isin(categories)]
    
    # 📈 GRÁFICO 1: Tendência de Vendas
    daily_data = filtered_df.groupby('date').agg({
        'sales': 'sum',
        'profit': 'sum'
    }).reset_index()
    
    trend_fig = go.Figure()
    trend_fig.add_trace(go.Scatter(
        x=daily_data['date'], y=daily_data['sales'],
        name='Vendas', line=dict(color='#1f77b4', width=3)
    ))
    trend_fig.add_trace(go.Scatter(
        x=daily_data['date'], y=daily_data['profit'],
        name='Lucro', line=dict(color='#2ca02c', width=2),
        yaxis='y2'
    ))
    trend_fig.update_layout(
        title='Vendas e Lucro ao Longo do Tempo',
        yaxis=dict(title='Vendas (R$)'),
        yaxis2=dict(title='Lucro (R$)', overlaying='y', side='right'),
        hovermode='x unified'
    )
    
    # 📊 GRÁFICO 2: Margem por Produto
    profit_data = filtered_df.groupby('product').agg({
        'sales': 'sum',
        'profit': 'sum'
    }).reset_index()
    profit_data['margin'] = (profit_data['profit'] / profit_data['sales'] * 100).round(1)
    
    profit_fig = px.bar(
        profit_data, x='product', y='margin',
        title='Margem de Lucro por Produto (%)',
        color='margin', color_continuous_scale='Viridis'
    )
    profit_fig.update_layout(showlegend=False)
    
    # 🌍 GRÁFICO 3: Vendas por Região
    region_data = filtered_df.groupby('region')['sales'].sum().reset_index()
    region_fig = px.pie(
        region_data, values='sales', names='region',
        title='Distribuição de Vendas por Região',
        hole=0.4
    )
    
    # 📦 GRÁFICO 4: Performance por Produto
    product_performance = filtered_df.groupby('product').agg({
        'sales': 'sum',
        'units': 'sum', 
        'profit': 'sum'
    }).reset_index()
    
    product_fig = px.scatter(
        product_performance, x='units', y='sales', size='profit',
        color='product', title='Performance: Unidades vs Vendas vs Lucro',
        size_max=60, hover_data=['profit']
    )
    
    # ⭐ GRÁFICO 5: Avaliação dos Clientes
    rating_data = filtered_df.groupby('product')['customer_rating'].mean().round(2).reset_index()
    rating_fig = px.bar(
        rating_data, x='product', y='customer_rating',
        title='Avaliação Média por Produto (1-5)',
        color='customer_rating', color_continuous_scale='RdYlGn',
        range_color=[3, 5]
    )
    
    return trend_fig, profit_fig, region_fig, product_fig, rating_fig, theme_class

# ====================
# 6. EXECUÇÃO
# ====================
if __name__ == '__main__':
    print("🚀 Dashboard Premium Iniciado!")
    print("📊 Acesse: http://127.0.0.1:8050")
    print("🎨 Dark Mode: Use o toggle no canto superior direito!")
    app.run(debug=True, port=8050, host='127.0.0.1')