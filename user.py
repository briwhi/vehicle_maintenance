from main import db, relationship


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicles = relationship("Vehicle")
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(128))