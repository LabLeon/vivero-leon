from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/catalogo')
def catalogo():
    return render_template('catalogue.html')

@app.route('/especie')
def especie():
    return render_template('species.html')


@app.route('/especies/<string:name>')
def especies_nombre(name):
    html = '''
    <h1>Specie "%s" section</h1>
    <p>This section will render the base template for each of the species.</p>
    ''' % name
    return html


if __name__ == '__main__':
    app.run(debug=True, port=5000)
