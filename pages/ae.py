import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=2)

layout = html.Div([
    dcc.Markdown("This is AE page"),
])
