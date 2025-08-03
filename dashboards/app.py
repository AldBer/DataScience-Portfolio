import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout mínimo válido
app.layout = html.Div([
    html.H1("Meu Dashboard Dash Funcionando!"),
    html.P("Agora você pode adicionar seus componentes...")
])

if __name__ == "__main__":
    app.run(debug=True)