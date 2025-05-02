import dash
from dash import html, dcc, callback, Input, Output, State
from components.f_sidebar import f_sidebar, SIDEBAR_STYLE, SIDEBAR_HIDEN, CONTENT_STYLE,CONTENT_STYLE1

dash.register_page(__name__, order=3)

content = html.Div(html.H3('this is ae-site page'), id="page-ae-content", style=CONTENT_STYLE)

layout = html.Div([dcc.Location(id="url"), f_sidebar(), content])


