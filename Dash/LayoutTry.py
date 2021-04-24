import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

external_stylesheet = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheet)


app.layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("A single column"))),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ]
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)