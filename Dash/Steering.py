import dash
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='steer'),
    dcc.Interval(id="progress-interval",
                 n_intervals=0,
                 interval=50),
])


@app.callback(
    Output('steer', 'figure'),
    [Input('progress-interval', 'n_intervals')]
)

def update_output(n):
    progress = min(n % 110, 100)
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        title={'text': "Speed"},
        delta={'reference': 380},
        gauge={'axis': {'range': [None, 500]},
               'steps': [
                   {'range': [0, 250], 'color': "lightgray"},
                   {'range': [250, 400], 'color': "gray"}],
               'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)