from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash

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
    year = db.Column(db.Integer)
    manufacturer = db.Column(db.String(40))
    make = db.Column(db.String(50))
    vin = db.Column(db.String(17))
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    tasks = relationship("Task")


# ------------------User Class---------------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicles = relationship("Vehicle")
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(128))

# db.create_all()


@app.route('/')
def home():

    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        data = request.form
        email = data['email']
        clear_password = data['password']
        hash_password = generate_password_hash(clear_password)
        user = User(email=email, password=hash_password)
        db.session.add(user)
        db.session.commit()

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
