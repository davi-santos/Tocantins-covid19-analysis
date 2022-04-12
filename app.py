from turtle import width
import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import json
import plotly.graph_objects as go

app = Dash(__name__)

color_og = "#242424"
color_op = '#000000'

df = pd.read_csv('./data/tocantins.csv')
df_tocantins = df[~df['municipio'].isna()]
tocantins_regioes = json.load(open('tocantins.json', 'r'))

fig = px.choropleth_mapbox(df_tocantins, locations='municipio', 
                    color='casosNovos', geojson=tocantins_regioes,
                    featureidkey='properties.name',
                    zoom=6,
                    center={"lat": -9.370232849190968, "lon": -47.926742249757595},
                          color_continuous_scale='Viridis')
fig.update_layout(
                paper_bgcolor=color_og,
                mapbox_style="carto-positron",
                autosize=True,
                margin=go.layout.Margin(l=0, r=0, t=0, b=0),
                showlegend=False,)

server = app.server

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.P('Oi')
        ),
        dbc.Col(
            dcc.Loading(
                        id="loading-1",
                        type="default",
                        children=[dcc.Graph(id="choropleth-map", figure=fig, 
                            style={'height': '105vh', 'margin-right': '10px'})],
                    ),
            #dcc.Graph(id='tocantins_graph', figure=fig)
        )
    ])
    
])

if __name__ == '__main__':
    app.run_server(debug=True)