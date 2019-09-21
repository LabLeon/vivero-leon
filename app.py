from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    html = '''
    <h1>Main section</h1>
    <p>This section will render the index section template.</p>
    '''
    return html


@app.route('/especies')
def especies():
    html = '''
    <h1>Species section</h1>
    <p>This section will render the species section template.</p>
    '''
    return html


@app.route('/especies/<string:name>')
def especies_nombre(name):
    html = '''
    <h1>Specie "%s" section</h1>
    <p>This section will render the base template for each of the species.</p>
    ''' % name
    return html


if __name__ == '__main__':
    app.run(debug=True, port=5000)
