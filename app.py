from flask import Flask
from flask import render_template
import qrcode

from io import BytesIO
import base64

from dbutils import MONGO_URI
from dbutils import db_connect_to_collection
from dbutils import db_fetch_data


app = Flask(__name__)
donations = db_connect_to_collection(MONGO_URI, 'viveros', 'donaciones')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/catalogo')
def catalogo():
    cursor = db_fetch_data(donations)
    return render_template('catalogue.html', data=enumerate(cursor))


@app.route('/especie')
def especie():
    return render_template('species.html', name='Suculenta')


@app.route('/especies/<string:name>')
def especies_nombre(name):
    # Build QR code:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=1,
    )
    qr.add_data("http://127.0.0.1:5000/especies/{}".format(name))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Encode QR code:
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('ascii')

    return render_template('species.html', name=name, qrimg=img_str)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
