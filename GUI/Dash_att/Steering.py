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
        mode="gauge",
        title={'text': "Steering"},
        delta={'reference': 380},
        gauge={'axis': {'range': [None, 100]},
               'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 1, 'value': progress}}))
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)