from dash import Dash, html, dcc, Input, Output  
import dash_bootstrap_components as dbc  
from components.navbar import create_navbar
from components.project_card import create_card
from agents.trading_agent import TradingAgent

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
bot = TradingAgent()

app.layout = html.Div([
    create_navbar(),
    
    # Seção de Projetos
    html.Div([
        create_card(
            "SP Housing", 
            "Análise de mercado imobiliário", 
            "/sp-housing"
        ),
        create_card(
            "Crypto Analysis", 
            "Dashboard de criptomoedas", 
            "/crypto"
        )
    ], style={"display": "flex"}),
    
    # Abas para IA Agents
    dcc.Tabs([
        dcc.Tab(label='Trading Bot', children=[
            html.Button("Analisar BTC", id='analyze-btn'),
            html.Div(id='bot-output')
        ])
    ])
])

# Callback para o bot
@app.callback(
    Output('bot-output', 'children'),
    Input('analyze-btn', 'n_clicks')
)
def update_output(n):
    if n:
        return f"Sinal: {bot.analyze('BTC')}"