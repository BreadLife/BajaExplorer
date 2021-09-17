import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

progress = html.Div(
    [
        dcc.Interval(id="progress-interval", n_intervals=0, interval=100),
        dbc.Progress(id="progress"),
    ]
)

app.layout = html.Div([progress])
"""
Le input est le "trigger" du callback qui active la fonction. Dans ce cas-ci on le trigger à chaque 100ms grace dcc.interval
De plus, il faut spécifier dans le callback ce qu'on lit ou écrit dans avec les id des éléments dans app.layout
Une fois que la fonction est appellée, elle retourne des valeurs/char dans différentes sous sections de chaque élément dans app.layout
Dans ce cas-ci on change "value" et "children" dans "progress", Ces deux variables vont faire changer respectivement la valeur
de la barre de progrès et le pourcentage affiché sur la barre de progrès.
"""

@app.callback(
    [Output("progress", "value"), Output("progress", "children")],
    [Input("progress-interval", "n_intervals")],
)
def update_progress(n):
    # check progress of some background process, in this example we'll just
    # use n_intervals constrained to be in 0-100
    progress = min(n % 110, 100)
    # only add text after 5% progress to ensure text isn't squashed too much
    return progress, f"{progress} %" if progress >= 5 else ""

if __name__ == '__main__':
    app.run_server(debug=True)