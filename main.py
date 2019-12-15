from flask import Flask, make_response, request, render_template, url_for, redirect
from io import BytesIO
import pyrebase
import qrcode
from PIL import Image
import pdb
from imageGenerate import CardBusiness, ReturnImage
from postFirebase import FirebaseObj
from qrGenerator import QrImage

APP = Flask(__name__)

config = {
    "apiKey": "AIzaSyC1ZnQgGzG28WjRxNyAqWKfgCyVL53BfqY",
    "authDomain": "gobusiness-24214.firebaseapp.com",
    "databaseURL": "https://gobusiness-24214.firebaseio.com",
    "projectId": "gobusiness-24214",
    "storageBucket": "gobusiness-24214.appspot.com",
    "messagingSenderId": "227161030539",
    "appId": "1:227161030539:web:975d35d67f1cd9a88fb98e",
    "measurementId": "G-ECWZY492FB"
}

firebase = pyrebase.initialize_app(config)

db= firebase.database()


@APP.route('/cards/<key>', methods=['GET', 'POST'])
def con_firebase(key):
    obj= db.child("cartoes").child(key).get()
    data = obj.val()
    response_card = CardBusiness(data).final_card()
    response = ReturnImage(response_card).generate_response()
    return response


@APP.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        data = request.form
        pdb.set_trace()
        fb_obj = FirebaseObj(data, db)
        fb_obj.uploadFirebase()

        key = fb_obj.get_key()
        QrImage(key).save_qr()

        return redirect(url_for('display_qr'))
    else:
        return render_template('index.html')


@APP.route('/qr')
def display_qr():
    qr = Image.open('qr.png').convert('RGBA')
    response = ReturnImage(qr).generate_response()
    return response

if __name__ == '__main__':
    APP.run()