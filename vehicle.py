from main import db, relationship, ForeignKey


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    manufacturer = db.Column(db.String(40))
    make = db.Column(db.String(50))
    vin = db.Column(db.String(17))
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    tasks = relationship("Task")