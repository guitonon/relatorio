import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table
import dash_html_components as html
import plotly.express as px
import pandas as pd
from plotly.graph_objs import Layout
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import webbrowser
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

external_stylesheets = [dbc.themes.BOOTSTRAP,
"https://use.fontawesome.com/releases/v5.7.2/css/all.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])

app.layout = dbc.Container([   
dbc.Row ([
    html.H1('Academia de Areia - São Carlos')],
    ),

dbc.Row ([
    html.H6('Relatório Final do Projeto')],
    ),

dbc.Row ([
     html.Div(id='div-link1'),
              
    html.Hr()]),  

dbc.Row (
    [html.H6('Esta seção se refere à gerência do projeto. Qual arquivo você deseja visualizar?'),
         dbc.Col(
            dbc.Select(
                id="select1",
                options=[
                    {"label": "Project Charter", "value": "file:///C:/Users/Viajante/Downloads/ProjectCharter_AcademiaDeAreia-_1_.html"},
                    {"label": "Gantt", "value": "https://docs.google.com/spreadsheets/d/1OLiWupfmU_JCEzy35xrjDay1prh67qqDaypzhx1O1Mo/edit?usp=sharing"},
                    {"label": "Matriz de responsabilidades", "value": "https://docs.google.com/spreadsheets/d/1iGThO8WVadYvN6mRcTs6B5NDru1_qkT2j2jRqATF8wc/edit?usp=sharing"}]
                
            ),
            width=4
        ),
        
    ]),

dbc.Row ([
     html.Div(id='div-link2'),
              
    html.Hr()]),  

dbc.Row (
    [html.H6('Esta seção se refere ao Marketing do projeto. Qual arquivo você deseja visualizar?'),
         dbc.Col(
            dbc.Select(
                id="select2",
                options=[
                    {"label": "Estudo dos Concorrentes", "value": "https://docs.google.com/document/d/161dcTO0tKUPQa77iQu8rdawe9mffoWgBtV7ZcILSz4A/edit?usp=sharing"},
                    {"label": "Abordagem ao público", "value": "https://docs.google.com/document/d/1uLAyAZSDqPR-Y9ckFjrOMYyQLVfsapi7heEFhG2qoew/edit?usp=sharing"},
                    {"label": "Identidade Visual", "value": "https://docs.google.com/document/d/1Ar4CU5EPonq8sdMcYVQpcXucvFh7E_Sd4gbwgIq2oGU/edit?usp=sharing"}]
            ),
            width=4
        ),

dbc.Row ([
     html.Div(id='div-link3'),
              
    html.Hr()]),  

dbc.Row (
    [html.H6('Esta seção se refere à construção da Academia de Areia. Qual arquivo você deseja visualizar?'),
         dbc.Col(
            dbc.Select(
                id="select3",
                options=[
                    {"label": "Localização do terreno", "value": "https://docs.google.com/document/d/1xhJOY6zt29ZKW89LZEKbZPIbLDPrYbcr0X3i05fU9MY/edit?usp=sharing"},
                    {"label": "Medidas oficiais das quadras", "value": "https://docs.google.com/document/d/18hL2DLAxn-71WkXbl3K2I2iS4EIyQsU2KkOJrzgOlQQ/edit?usp=sharing"},
                    {"label": "Planta 2D", "value": "https://drive.google.com/file/d/1pZYsZm2morw6yloiQ88-Kuu9G26cjOyc/view?usp=sharing"}]
                
            ),
            width=4
        ),
        
    ]),
        
    ]),

])
@app.callback(
    Output(component_id='div-link1', component_property='children'),
    Input(component_id='select1', component_property='value')
)

def update_output_div(input_value):
    new = 2 
    url = input_value
    return webbrowser.open(url,new=new) 

@app.callback(
    Output(component_id='div-link2', component_property='children'),
    Input(component_id='select2', component_property='value')
)

def update_output_div(input_value):
    new = 2 
    url = input_value
    return webbrowser.open(url,new=new) 

@app.callback(
    Output(component_id='div-link3', component_property='children'),
    Input(component_id='select3', component_property='value')
)

def update_output_div(input_value):
    new = 2 
    url = input_value
    return webbrowser.open(url,new=new) 

if __name__ == '__main__':
    app.run_server(debug=False)
