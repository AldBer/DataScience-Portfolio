from dash import html
import dash_bootstrap_components as dbc

def create_card(title, description, link):
    card = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(title, className="card-title"),
                    html.P(description, className="card-text"),
                    dbc.Button("Acessar", href=link, color="primary"),
                ]
            )
        ],
        style={"width": "18rem", "margin": "10px"},
    )
    return card