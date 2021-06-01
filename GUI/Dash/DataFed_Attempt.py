import Feeder

import dash
import base64
import plotly.graph_objects as go
import dash_daq as daq
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
        dbc.Col(html.Div(id='Av_g', style={'fontSize': 50, 'align-items': 'center', 'marginTop':'100px'}), width="auto"),

        dbc.Col(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
                         style={'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}), width="auto"),

        dbc.Col([
            dbc.Row(html.Div(id='Av_d', style={'fontSize': 50, 'align-items': 'center', 'marginTop': '100px'})),
            dbc.Row(html.Div(id='Arr', style={'fontSize': 50, 'align-items': 'center', 'marginTop': '450px'}))
        ]),

        dbc.Col([daq.GraduatedBar(
                id='throt',
                label={'label':"Throttle", 'style':{'fontSize': 40, 'marginTop':'19px'}},
                max=100,
                size=300,
                vertical=True),
            daq.GraduatedBar(
                id='temp',
                label={'label':"Temperature", 'style':{'fontSize': 40, 'marginTop':'40px'}},
                max=100,
                size=300,
                vertical=True
            )],
            width="auto"
        ),

        dbc.Col([
            dcc.Graph(id='steer'),
            dcc.Graph(id='rpm'),
        ], width="auto"
        )
    ], justify='center'),
    dcc.Interval(id="progress-interval", n_intervals=0, interval=500),
])


@app.callback(
    Output('Av_d', 'children'),
    Output('Av_g', 'children'),
    Output('Arr', 'children'),
    Output('temp', 'value'),
    Output('throt', 'value'),
    Output('steer', 'figure'),
    Output('rpm', 'figure'),
    [Input('progress-interval', 'n_intervals')]
)

def update_output(n):
    progress = Feeder.return_rand_number()
    rpm = Feeder.return_rand_number()
    fig_steer = go.Figure(go.Indicator(
        mode="gauge",
        gauge={'axis': {'range': [None, 100]},
               'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 1, 'value': progress}}
    ))
    fig_rpm = go.Figure(go.Indicator(
        mode="gauge+number",
        value=rpm,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge = {'axis': {'range': [None, 500]}}
    ))
    fig_steer.update_layout(title="Steering", font=dict(size=30))
    fig_rpm.update_layout(title="RPM Moteur", font=dict(size=30))
    return f'{progress:04}'\
        , f'{progress:04}'\
        , f'{progress:04}'\
        , progress\
        , progress\
        , fig_steer\
        , fig_rpm\

if __name__ == '__main__':
    app.run_server(debug=True)