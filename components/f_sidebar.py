import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 72,
    "left": 12,
    "bottom": 0,
    "width": "13rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 0.5rem",
    "background-color": "#f8f9fa",
    "fontSize": 18
}

SIDEBAR_HIDEN = {
    "position": "fixed",
    "top": 72,
    "left": "-13rem",
    "bottom": 0,
    "width": "13rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "14rem",
    "margin-right": "0rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "0rem",
    "margin-right": "0rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

def f_sidebar():
    sidebar = html.Div(
        [
            dbc.Nav(
                [
                    dbc.NavLink("ae", href="/ae", id="page-ae"),
                    dbc.NavLink("ae by site", href="/p-ae-site", id="page-ae-site"),
                    # dbc.NavLink("Page 2", href="/sub-ae/ae-summary", id="page-2-link"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        id="sidebar",
        style=SIDEBAR_HIDEN,
    )
    return sidebar