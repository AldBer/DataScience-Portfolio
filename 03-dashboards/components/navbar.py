import dash_bootstrap_components as dbc

def create_navbar():
    navbar = dbc.NavbarSimple(
        brand="Meu Dashboard",
        brand_href="#",
        color="primary",
        dark=True,
    )
    return navbar