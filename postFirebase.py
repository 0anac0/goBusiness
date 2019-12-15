import pyrebase
import pdb
class FirebaseObj():
    def __init__(self, data, db):
        self.data = data
        self.db = db
        self.key = self.db.generate_key()

    def uploadFirebase(self):
        nome = self.data["nome"]
        sobrenome = self.data["sobrenome"]
        cargo = self.data["cargo"]
        telefone = self.data["telefone-pessoal"]
        email = self.data["email"]
        site = self.data["blog-site"]
        self.db.child("cartoes").child(self.key).set({"Nome": nome, "Sobrenome": sobrenome, "Cargo": cargo,
                                  "Telefone": telefone, "email":email,"site": site})

    def get_key(self):
        return self.key