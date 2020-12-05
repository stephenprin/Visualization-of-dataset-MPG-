import dash
import dash_core_components as dcc
import dash_html_components  as html
import plotly.graph_objects as go
from dash.dependencies import Input,Output
from numpy import random
import pandas as pd

app=dash.Dash()

df=pd.read_csv(r'C:/Users/PRINCE/Desktop/covid19 colab/mpg.csv')
# ADDING NOISE, JITTER
df['year']=random.randint(-4,5,len(df))*0.1+df['model_year']

app.layout=html.Div([
   html.Div(
       dcc.Graph(id='mpg-scatter',
                 figure={
                     'data': [go.Scatter(
                         x=df['year'] + 1900,
                         y=df['mpg'],
                         text=df['name'],
                         hoverinfo ='text' + 'x' + 'y',
                         mode='markers'
                     )
                     ],
                     'layout': go.Layout(title='PLOT SHOW MPG VS MODEL YEAR OF CAR DISTRIBUTION',
                                         xaxis=dict(title='MPG'),
                                         yaxis=dict(title='MODEL YEAR'),
                                         hovermode='closest')
                 }),
       style={'width':'40%','display':'inline-block'}
   )
])

if __name__=='__main__':
    app.run_server(debug=True)