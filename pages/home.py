import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output, State

dash.register_page(__name__, path='/', order=0)

layout = html.Div([
    dcc.Markdown("This is home page"),
    dcc.Location(id='url')
])

@callback(
    Output("sidebar-button-container", "style"),
    Input("url", "pathname"),
)
def toggle_sidebar_visibility(pathname):
    # print(f"当前路径是: {pathname}")
    if pathname == "/" or pathname == "/home":
        return {"display": "none"}
    return {"display": "block"}