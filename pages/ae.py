import dash
import pandas as pd
from dash import html, dcc, callback, Input, Output, State
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
from components.f_sidebar import f_sidebar, SIDEBAR_STYLE, SIDEBAR_HIDEN, CONTENT_STYLE,CONTENT_STYLE1 # sidebar
import pyreadr
import plotly.express as px

dash.register_page(__name__, order=2)

adae = pyreadr.read_r('./assets/adae.rda')['adae']
adsl = pyreadr.read_r('./assets/adsl.rda')['adsl']

defaultColDef = {
    "filter": True,
    # "floatingFilter": True,
    "resizable": True,
    "sortable": True,
    "editable": False,
    # "minWidth": 100,
}

columnDefs = [
    {
    'headerName': 'Basic Info',
        'children': [
            {'field': 'STUDYID','columnGroupShow': 'open'},
            {'field': 'USUBJID'},
            {'field': 'SITEID'},
            {'field': 'SUBJID','columnGroupShow': 'open'},
            {'field': 'SAFFL'},
            {'field': 'TRT01P','columnGroupShow': 'open'},
            {'field': 'TRT01A'},
            {'field': 'TRTSDT'},
            {'field': 'TRTEDT'},
            {'field': 'TRTEMFL'},
            {'field': 'RANDDT','columnGroupShow': 'open'},
            {'field': 'TRTSDTM','columnGroupShow': 'open'},
            {'field': 'TRTSTMF','columnGroupShow': 'open'},
            {'field': 'TRTEDTM','columnGroupShow': 'open'},
            {'field': 'TRTETMF','columnGroupShow': 'open'},
            {'field': 'DTHDTC','columnGroupShow': 'open'},
            {'field': 'DTHCAUS','columnGroupShow': 'open'},
            {'field': 'DTHFL','columnGroupShow': 'open'},
            {'field': 'DTHDTF','columnGroupShow': 'open'},
            {'field': 'LDDTHGR1','columnGroupShow': 'open'},
            {'field': 'DTH30FL','columnGroupShow': 'open'},
            {'field': 'DTHA30FL','columnGroupShow': 'open'},
            {'field': 'DTHB30FL','columnGroupShow': 'open'},
            {'field': 'AGE','columnGroupShow': 'open'},
            {'field': 'AGEU','columnGroupShow': 'open'},
            {'field': 'SEX','columnGroupShow': 'open'},
            {'field': 'RACE','columnGroupShow': 'open'},
            {'field': 'ETHNIC','columnGroupShow': 'open'},
            {'field': 'COUNTRY','columnGroupShow': 'open'},
            {'field': 'RACEGR1','columnGroupShow': 'open'},
            {'field': 'AGEGR1','columnGroupShow': 'open'},
            {'field': 'REGION1','columnGroupShow': 'open'},
        ]
    },
    {
    'headerName': 'AE Info',
        'children':[
            {'field': 'AETERM'},
            {'field': 'AESOC'},
            {'field': 'AESEV'},
            {'field': 'AESER'},
            {'field': 'AEACN'},
            {'field': 'AEREL'},
            {'field': 'AEOUT'},
            {'field': 'AESOCCD','columnGroupShow': 'open'},
            {'field':'AELLT','columnGroupShow': 'open'},
            {'field':'AELLTCD','columnGroupShow': 'open'},
            {'field':'AEDECOD','columnGroupShow': 'open'},
            {'field':'AEPTCD','columnGroupShow': 'open'},
            {'field':'AEHLT','columnGroupShow': 'open'},
            {'field':'AEHLTCD','columnGroupShow': 'open'},
            {'field':'AEHLGT','columnGroupShow': 'open'},
            {'field':'AEHLGTCD','columnGroupShow': 'open'},
            {'field':'AEBODSYS','columnGroupShow': 'open'},
            {'field':'AEBDSYCD','columnGroupShow': 'open'},
            {'field':'AESCAN','columnGroupShow': 'open'},
            {'field':'AESCONG','columnGroupShow': 'open'},
            {'field':'AESDISAB','columnGroupShow': 'open'},
            {'field':'AESDTH','columnGroupShow': 'open'},
            {'field':'AESHOSP','columnGroupShow': 'open'},
            {'field':'AESLIFE','columnGroupShow': 'open'},
        ]
    },
    {
    'headerName': 'Date Info',
        'children': [
            {'field':'AESTDTC'},
            {'field':'AEENDTC'},
            {'field': 'ASTDT'},
            {'field': 'ASTDTF','columnGroupShow': 'open'},
            {'field': 'ASTDY'},
            {'field': 'AENDT'},
            {'field': 'AENDTF','columnGroupShow': 'open'},
            {'field': 'AENDY'},
            {'field':'AESTDY','columnGroupShow': 'open'},
            {'field':'AEENDY','columnGroupShow': 'open'},
            {'field':'ASTDTM','columnGroupShow': 'open'},
            {'field':'ASTTMF','columnGroupShow': 'open'},
            {'field':'AENDTM','columnGroupShow': 'open'},
            {'field':'AENTMF','columnGroupShow': 'open'},
            {'field':'AEDTC','columnGroupShow': 'open'},
        ]
    }
]

# print(adae.columns)
adae_grid = dag.AgGrid(
    id='adae_grid',
    rowData=adae.to_dict("records"),
    columnDefs=columnDefs,
    defaultColDef=defaultColDef,
    dashGridOptions={"animateRows": False,'pagination':True},
    columnSize="autoSize",
    style={"height": "500px", "width": "100%"}
)

content = html.Div([html.H3('AE Raw Data'),
                    dbc.Row([
                        # dbc.Card(
                        #     [
                        #         dbc.CardBody(
                        #             [
                                        adae_grid,
                                        dbc.Row([
                                            dbc.Col([
                                            dbc.Input(
                                                id="save-name",
                                                placeholder="Save as...",
                                                type="text",
                                                value=None,
                                                className='mt-2'
                                            ),
                                            ],width=6),
                                        dbc.Col([
                                            dbc.Button(
                                                id="save-btn",
                                                children="Save Table",
                                                color="primary",
                                                size="md",
                                                className='mt-2'
                                            )
                                        ],width=3)
                                        ]),
                                    ]
                                ),
                    #         ]
                    #     )
                    # ]),
                    dbc.Row([
                        dbc.Alert(children=None,
                        color="success",
                        id='alerting',
                        is_open=False,
                        duration=2000,
                        className='ms-4',
                        style={'width':'18rem'}),
                    ]),
                    dbc.Row([
                        html.Div(id="adae_grd_fig",className='mt-2')
                    ]),
                    ],
                   id="page-ae-content",
                   style=CONTENT_STYLE)

layout = html.Div([dcc.Location(id="url"), f_sidebar(), content])

# save your data
@callback(
    Output("alerting", "is_open"),
    Output("alerting", "children"),
    Output("alerting", "color"),
    Input("save-btn", "n_clicks"),
    State("save-name", "value"),
    State("adae_grid", "virtualRowData"),
    prevent_initial_call=True
)
def update_portfolio_stats(n, name, data):
    print(type(name))
    if name is None or len(name)==0:
        return True, "No name provided", "danger"
    else:
        dff = pd.DataFrame(data)
        dff.to_csv(f'./assets/{name}.csv', index=False)
        return True, "Data Saved! Well done!", "success"

# fig
@callback(
    Output("adae_grd_fig", "children"),
    Input("adae_grid", "virtualRowData"),
)
def update_graphs(data):
    diff = adae if data is None else pd.DataFrame(data)
    graphs = []
    for column in ["SITEID","AESOC"]:
        if column in diff.columns:
            diff_grp = diff.groupby([column])
            diff_pct = pd.DataFrame(diff_grp['USUBJID'].nunique() / diff['USUBJID'].nunique())
            diff_pct.reset_index(inplace=True)
            diff_pct.rename(columns={'USUBJID': 'PERCENT'}, inplace=True)
            diff_pct.sort_values(by='PERCENT', ascending=False, inplace=True)
            fig = px.bar(diff_pct, x=column, y='PERCENT',orientation='v')
            if column == 'AESOC':
                fig.update_layout(
                    margin={"t": 10, "l": 10, "r": 10},
                    xaxis_tickangle=90,
                    xaxis={"automargin": True},
                    yaxis={"automargin": True},
                    yaxis_tickformat=".0%",
                    height=800
                )
            else:
                fig.update_layout(
                    margin={"t": 10, "l": 10, "r": 10},
                    xaxis={"automargin": True},
                    yaxis={"automargin": True},
                    yaxis_tickformat=".0%",
                )

            graphs.append(dcc.Graph(id=column, figure=fig))
    return graphs

# sidebar
@callback(
    [
        Output("sidebar", "style"),
        Output("page-ae-content", "style"),
    ],

    [Input("btn_sidebar", "n_clicks")],
    [State("sidebar", "style"),]
)
def toggle_sidebar(n_clicks, current_style):
    if current_style == SIDEBAR_STYLE:
        return SIDEBAR_HIDEN, CONTENT_STYLE1
    else:
        return SIDEBAR_STYLE, CONTENT_STYLE

