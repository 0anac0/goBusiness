import qrcode
from PIL import Image

class QrImage():
    def __init__(self, key):
        self.key= key

    def get_url(self):
        self.domain= "127.0.0.1:5000/cards/"
        self.url = self.domain+self.key
        return self.url

    def save_qr(self):
        self.qr= qrcode.make(self.get_url())
        self.qr.save("qr.png")

