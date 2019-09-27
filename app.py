from flask import Flask
from flask import render_template
from unidecode import unidecode
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
    qr.add_data("http://127.0.0.1:5000/especies/%s" % name)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Encode QR code:
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('ascii')

    especieqr = [
        {
            "nombre": "HIERBABUENA",
            "descripcion": unidecode("Es una especie del género Mentha, una hierba aromática muy empleada en gastronomía y perfumería por su aroma intenso y fresco. Tiene propiedades útiles, antiespasmódicas, es carminativo, antiséptico, analgésico, antiinflamatorio y estimulante."),
            "imagen": "hierbabuena.jpg"
        },
        {
            "nombre": "SUCULENTA",
            "descripcion": unidecode("Se dan típicamente zonas secas y calurosas, donde el agua es escasa. Muchas de las especies de esta familia son populares en jardinería y floricultura; son plantas duras y requieren cuidados mínimos. Otra ventaja para el cultivo de estas plantas es lo habitualmente sencillo de su propagación, necesitándose en algunos casos una simple hoja para lograr un nuevo ejemplar."),
            "imagen": "suculenta.jpg"
        },
        {
            "nombre": "CEMPASUCHIL",
            "descripcion": unidecode("Es una especie de la familia Asteraceae, nativa de México, donde se encuentra en estado silvestre principalmente en los estados de Chiapas, México, Morelos, Puebla, San Luis Potosí, Sinaloa, Tlaxcala, Oaxaca, Jalisco y Veracruz. La principal característica de las flores es que están agrupadas en cabezuelas o en inflorescencias solitarias, sobre pedúnculos de hasta 15 cm de largo, son liguladas de colores amarillo a rojo."),
            "imagen": "cempasuchil.jpg"
        },
        {
            "nombre": "DALIA",
            "descripcion": unidecode("La dalia es una especie originaria de los bosques templados del Sur y Centro de México. Posee raíces en forma de camotes, los cuales son comestibles y medicinales, ahora se está cultivando en zonas rurales para producir té a partir de la misma."),
            "imagen": "dalia.jpg"
        },
        {
            "nombre": "ROMERO",
            "descripcion": unidecode("El romero es un arbusto aromático, leñoso, de hojas perennes, muy ramificado y ocasionalmente achaparrado y que puede llegar a medir 2 metros de altura. Se cría en todo tipo de suelos, preferiblemente los secos y algo arenosos y permeables, adaptándose muy bien a los suelos pobres. Crece en zonas litorales y de montaña baja."),
            "imagen": "romero.jpg"
        }
    ]

    data = 1
    for item in especieqr:
        if item['nombre'] == name:
            data = item

    return render_template('species.html', name=name, data=data, qrimg=img_str)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
