import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc


dash.register_page(__name__)

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    # sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    html.H3('ae summary'),
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    ),
        # dcc.Store(id="collapse-store", data=False),
])