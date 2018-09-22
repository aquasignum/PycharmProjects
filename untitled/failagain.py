import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from collections import deque
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', passwd='', database='co2data')
c = conn.cursor()


name_title = 'Microbial Activity'
app = dash.Dash(__name__)

app.layout = html.Div(children=[

    html.H1(children='Realtime Microbial Activity'),
    dcc.Graph(
        id='example-graph', animate=True), dcc.Interval(id='graph-update', interval=5 * 1000), ])



@app.callback(Output('example-graph', 'figure'),
              events=[Event('graph-update', 'interval')])
def update_graph_scatter():
    datasql = []  # set an empty list
    X = deque(maxlen=10)
    Y = deque(maxlen=10)

    conn = mysql.connector.connect(host='localhost', user='root', passwd='', database='co2data')
    c = conn.cursor()
    c.execute("SELECT co2ppm,timeofread FROM co2")
    rows = c.fetchall()
    for row in rows:
        datasql.append(list(row))
        labels = ['co2ppm', 'timeofread']
        df = pd.DataFrame.from_records(datasql, columns=labels)
        X = df['timeofread']
        Y = df['co2ppm']

    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )


    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                                yaxis=dict(range=[min(Y), max(Y)]), )}


if __name__ == "__main__":
    app.run_server(debug=True)