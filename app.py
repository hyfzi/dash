import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output, State

app = dash.Dash(
    __name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY]
)

for page in dash.page_registry.values():
    print(page['path'])

header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Nav(
                [
                    dbc.NavLink(page["name"], href=page["path"])
                    for page in dash.page_registry.values()
                    if not page["path"].startswith("/p-")
                ],
            ),
            html.Div(
                dbc.Nav(
                    dbc.NavLink("sidebar", id="btn_sidebar", n_clicks=0),
                    navbar=True
                ),
                id="sidebar-button-container",
                className="ms-auto",
                style={"display": "block"}  # 默认隐藏
            ),
        ],
        fluid=True,
    ),
    color="primary",
    dark=True,
)

app.layout = dbc.Container([header,dash.page_container], fluid=True)

if __name__ == '__main__':
    app.run(debug=True)
