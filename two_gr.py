import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output

df = pd.read_csv('lr.csv', delimiter=';')


app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1("Графики с Dash и Plotly"),

    # График 1 (точечный)
    dcc.Graph(id='graph1'),

    # График 2 (столбчатый)
    dcc.Graph(id='graph2'),
])


@app.callback(
    Output('graph1', 'figure'),
    Output('graph2', 'figure'),
    Input('graph1', 'relayoutData'),
)
def update_graphs(relayout_data):
    try:
        # Фигура точечного графика
        fig1 = px.scatter(df, x='Время мойки', y='Цвет', title='Точечный график').update_layout(
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(family="Arial, sans-serif", size=12, color="Black"),
            paper_bgcolor="White",
        )

        # Фигура столбчатого графика
        fig2 = px.bar(df, x='Время мойки', y='Тип мойки', title='Столбчатый график').update_layout(
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(family="Arial, sans-serif", size=12, color="Black"),
            paper_bgcolor="White",
        )

        return fig1, fig2
    except Exception as e:
        print(str(e))
        return dash.no_update, dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)