from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# --------------------Task Class---------------------------
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, ForeignKey('vehicle.id'))
    name = db.Column(db.String(50))
    date = db.Column(db.Date)
    mileage = db.Column(db.Integer)


# ---------------------Vehicle Class--------------------------
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    year = db.Column(db.Integer)
    manufacturer = db.Column(db.String(40))
    make = db.Column(db.String(50))
    tasks = relationship("Task")


# db.create_all()


@app.route('/')
@app.route('/home')
def home():
    vehicles = Vehicle.query.all()
    return render_template("index.html", vehicles=vehicles)


@app.route('/add_vehicle', methods=['POST', 'GET'])
def add_vehicle():
    if request.method == 'POST':
        name = request.form['name']
        manufacturer = request.form['manufacturer']
        year = request.form['year']
        model = request.form['model']
        vehicle = Vehicle(name=name, manufacturer=manufacturer, year=year, make=model)
        db.session.add(vehicle)
        db.session.commit()
        return redirect(url_for('vehicle_detail'), id=vehicle.id)
    return render_template("add_vehicle.html")


@app.route('/vehicle_detail/<id>')
def vehicle_detail(id):
    vehicle = Vehicle.query.get(id)
    return render_template("vehicle_detail.html", vehicle=vehicle)


if __name__ == "__main__":
    app.run(debug=True)
