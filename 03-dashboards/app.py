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
            "../01-real-estate-sp/app_housing/main.py"
        ),
        create_card(
            "Crypto Analysis", 
            "Dashboard de criptomoedas", 
            "../02-crypto-monitoring/scripts/technical_analysis.py"
        )
    ], style={"display": "flex", "flexWrap": "wrap", "padding": "20px"}),
    
    # Abas para IA Agents
    dcc.Tabs([
        dcc.Tab(label='Trading Bot', children=[
            html.Div([
                html.Button("Analisar BTC", id='analyze-btn', 
                          style={'margin': '20px', 'padding': '10px 20px'}),
                html.Div(id='bot-output', 
                        style={'padding': '20px', 'fontSize': '18px'})
            ])
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
        return f"💰 Sinal: {bot.analyze('BTC')}"
    return "Clique no botão para analisar BTC"

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)