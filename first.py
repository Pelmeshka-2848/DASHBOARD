import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

app = Dash(__name__)

df = pd.read_csv('lr.csv', delimiter=';')

fig = px.bar(df, x="Марка машины", y="Оценка", color="Год выпуска", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Лабораторная работа'),

    html.Div(children='''
        
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)