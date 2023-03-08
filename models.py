from index import app, db

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(300))
    genero = db.Column(db.String(200))
    console = db.Column(db.String(2000))

with app.app_context():
    db.create_all()