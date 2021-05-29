import dash
import base64
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

image_filename = 'bajaTOP.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.Div(id='Av_g', style={'fontSize': 50, 'align-items': 'left'}), width="auto"),
        dbc.Col(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
                         style={'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}), width="auto"),
        dbc.Col(html.Div(id='Av_d', style={'fontSize': 50, 'align-items': 'left'}), width="auto"),
    ]),
        #html.P('Example P', className='my-class', id='my-p-element'),
    dcc.Interval(id="progress-interval", n_intervals=0, interval=50),
])


@app.callback(
    Output('Av_d', 'children'),
    Output('Av_g', 'children'),
    [Input('progress-interval', 'n_intervals')]
)

def update_output(n):
    progress = min(n % 110, 100)
    return f'{progress:04}', f'{progress:04}'

if __name__ == '__main__':
    app.run_server(debug=True)