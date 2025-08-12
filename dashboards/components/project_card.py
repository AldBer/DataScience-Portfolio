from dash import html, dcc
import dash_bootstrap_components as dbc

def create_card(title, description, btn_link):
    return dbc.Card([
        dbc.CardBody([
            html.H4(title, className="card-title"),
            html.P(description),
            dcc.Link("Acessar", href=btn_link, className="btn btn-primary")
        ])
    ], style={"margin": "10px"})