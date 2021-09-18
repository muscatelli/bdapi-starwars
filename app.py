import os 
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Vehicles
from flask_migrate import Migrate
#from flask_script import Manager
BASEDIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(BASEDIR, "test.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
#manager = Manager(app)

migrate = Migrate(app, db)
db.init_app(app)

@app.route("/")
def test(): 
    return jsonify('hola mundo')
@app.route("/test",methods=["POST"])


def probando():
    user = User()
    user.name = request.json.get('name') 
    user.password = request.json.get('password')
    user.email = request.json.get('email')
    user.isActive = request.json.get('isActive')  
    
    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize()), 200

@app.route("/vehicles",methods=["GET"])

def vehicles():
    vehicles = Vehicles()
    vehicles.name = request.json.get('name')
    vehicles.model = request.json.get('model')
    vehicles_class = request.json.get('vehicles_class')
    vehicles.crew = request.json.get('crew')
    vehicles.manufacturer = request.json.get('manufacturer')
    vehicles.cost_in_credits = request.json.get('cost_in_credits')     
    
    db.session.add(vehicles)
    db.session.commit()

    return jsonify(user.serialize()), 200


if __name__ == "__main__":
    app.run(host='localhost',port=8080)




