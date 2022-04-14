from pydoc import classname
from turtle import bgcolor, width
from numpy import size
import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import json
import plotly.graph_objects as go

app = Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR])

map_background_color = '#fafaf8'

df = pd.read_csv('./data/tocantins.csv')
df_tocantins = df[~df['municipio'].isna()]
tocantins_regioes = json.load(open('tocantins.json', 'r'))

# Figure Tocantins map
fig = px.choropleth_mapbox(df_tocantins, locations='municipio', 
                    color='casosNovos', geojson=tocantins_regioes,
                    range_color=(0,260),
                    featureidkey='properties.name',
                    zoom=6,
                    center={"lat": -9.370232849190968, "lon": -47.926742249757595},
                          color_continuous_scale='oryel')
                          # os que gostei: ylorrd, turbid, sunsetdark, speed, ++ pinkyl, peach
                          # NOVOS q gostei: oryel (best of all), mint, matter (good)
fig.update_layout(
                paper_bgcolor=map_background_color,
                mapbox_style="carto-positron",
                autosize=True,
                margin=go.layout.Margin(l=0, r=0, t=0, b=0),
                showlegend=False,)

# Figure CasosAcumulado
pmw = df_tocantins[df_tocantins['municipio'] == 'Palmas'][['casosAcumulado', 'data']].sort_values(by='data')
fig2 = px.line(pmw, x='data', y='casosAcumulado')

server = app.server

app.layout = dbc.Container([
    #Row 1
    dbc.Row(
        dbc.Col(
            html.H2('Dashboard covid-19 Tocantins', className='text-center text-white mt-3 mb-0'), width=6,
            
        ), justify='center', className='bg-black text-white'
    ),
    #Row 2
    dbc.Row(
        dbc.Col(children=[
            html.P('Some text powered by @Davi', className='text-center text-white'),
        ]), justify='center', className='bg-black text-white'
    ),
    #Row 3
    dbc.Row([
        dbc.Col(
            html.Div(children=[
                dbc.RadioItems(
                    id="radios",
                    className="btn-group ",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-primary",
                    labelCheckedClassName="active",
                    options=[
                        {'label': 'Casos Novos', 'value':0},
                        {'label': 'Recuperados', 'value':1},
                        {'label': 'Óbitos Confirmados', 'value':2},
                    ],
                    value=1,
                ),
                dcc.Graph(id="choropleth-map", figure=fig, style={'height': '84vh'})],
                className='border border-alert rounded', style={'background-color': map_background_color}
            ), width=6
            
            # dcc.Loading(
            #             id="loading-1",
            #             type="default",
            #             children=[dcc.Graph(id="choropleth-map", figure=fig, 
            #                 style={'height': '82vh', 'width': '100vh', 'margin-right': '10px'})]),   
        ),
        dbc.Col([
            dbc.Row([
                dbc.Col(
                    dbc.Card(
                        dbc.CardHeader(children=[
                            html.H5('Novos Casos'),
                            html.H4('000.000')
                        ], className='bg-warning'),
                    ), 
                    width=4
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardHeader(children=[
                            html.H5('Recuperados'),
                            html.H4('000.000')
                        ], className='bg-success')
                    ), width=4
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardHeader(children=[
                            html.H5('Óbitos Confirmados'),
                            html.H4('000.000')
                        ], className='bg-danger')
                    ), width=4
                )
            ], className='mb-3 mt-2 text-center text-black'),    
            dbc.Row([
                dbc.Col(
                    dbc.Card(
                        dbc.CardHeader(children=[
                            html.H5('Percentual Tocantins'),
                            html.H4('0%'),
                            html.P('mais casos essa semana.')
                        ])
                    ), width=5),
                dbc.Col(
                    dbc.Card(
                        dbc.CardHeader(children=[
                            html.H5('Percentual Brasil'),
                            html.H4('0%'),
                            html.P('mais casos essa semana.')
                        ])
                    ), width=5
                ),
            ], justify='center',className='mb-2 text-center text-dark'),
            dbc.Row(children=[
                dbc.Col(children=[
                    dcc.Dropdown(
                        options=[
                            {'label': 'Casos', 'value':0},
                            {'label': 'Recuperados', 'value':1},
                            {'label': 'Óbitos', 'value':1},
                        ], value='Casos',  clearable=False
                    )
                ], width=6),
                dbc.Col(children=[
                    dcc.Dropdown(
                        options=[
                            {'label': 'Casos', 'value':0},
                            {'label': 'Recuperados', 'value':1},
                            {'label': 'Óbitos', 'value':1},
                        ], value='Casos',  clearable=False
                    )
                ], width=6, className='mb-2')
            ]),
            dbc.Row(
                    dbc.Col(
                        dcc.Graph(id='general-graph', figure=fig2),
                        
                        className='border border-success mr-2'
                    ),
            )
        ], width=6, className='mr-2 ml-2')
    ],
    className='mt-2')
    
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)