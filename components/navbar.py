import dash_bootstrap_components as dbc  # Adicione esta linha
from dash import html  # Adicione esta linha

def create_navbar():
    return dbc.NavbarSimple(
        brand="Portfólio IA",
        brand_href="#",
        color="primary",
        dark=True
    )