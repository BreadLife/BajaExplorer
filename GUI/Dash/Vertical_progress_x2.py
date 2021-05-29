import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

app.layout = html.Div([
    daq.GraduatedBar(
        id='throt',
        label='throttle',
        max=100,
        vertical=True
    ),
    daq.GraduatedBar(
        id='temp',
        label='temperature',
        max=100,
        vertical=True
    ),
    dcc.Interval(id="progress-interval",
                 n_intervals=0,
                 interval=100),
])


@app.callback(
    Output('temp', 'value'),
    Output('throt', 'value'),
    [Input('progress-interval', 'n_intervals')]
)

def update_output(n):
    progress = min(n % 110, 100)
    return progress, progress

if __name__ == '__main__':
    app.run_server(debug=True)