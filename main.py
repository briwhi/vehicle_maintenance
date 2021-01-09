from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column
from user import User
from vehicle import Vehicle



app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)








class Task(db.Model):
    id = Column(db.Integer, primary_key=True)
    vehicle_id = Column(db.Integer, ForeignKey('vehicle.id'))
    name = Column(db.String(50))
    date = Column(db.Date)
    mileage = Column(db.Integer)


# create db
db.create_all()


# routes
@app.route('/')
def home():
    #vehicles = Vehicle.query.all()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
