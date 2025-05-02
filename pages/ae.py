import dash
from dash import html, dcc, callback, Input, Output, State, dash_table
from components.f_sidebar import f_sidebar, SIDEBAR_STYLE, SIDEBAR_HIDEN, CONTENT_STYLE,CONTENT_STYLE1
import pyreadr

dash.register_page(__name__, order=2)

adae = pyreadr.read_r('./assets/adae.rda')['adae']
adsl = pyreadr.read_r('./assets/adsl.rda')['adsl']


adae_table = dash_table.DataTable(
    adae.to_dict('records'),
    [{"name":i, "id": i} for i in adae.columns],
    style_table={'overflowX': 'auto'},
    page_size=10
)

content = html.Div([html.H3('this is ae page'),
                    adae_table
                    ],
                   id="page-ae-content",
                   style=CONTENT_STYLE)

layout = html.Div([dcc.Location(id="url"), f_sidebar(), content])

@callback(
    [
        Output("sidebar", "style"),
        Output("page-ae-content", "style"),
    ],

    [
        Input("btn_sidebar", "n_clicks")
    ],
    [
        State("sidebar", "style"),
     ]
)
def toggle_sidebar(n_clicks, current_style):
    if current_style == SIDEBAR_STYLE:
        return SIDEBAR_HIDEN, CONTENT_STYLE1
    else:
        return SIDEBAR_STYLE, CONTENT_STYLE

