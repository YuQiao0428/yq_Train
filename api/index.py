'''
    import train_2
    import dash
    import dash_html_components as html

    app = dash.Dash(__name__)

    app.layout = html.Div(
        html.H1('Hello python page...')
    )

    if __name__ == '__main__':
        app.run_server(debug=False)
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'