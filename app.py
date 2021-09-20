import os 
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Vehicles, Character, Planets #Favorites
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

    return jsonify(vehicles.serialize()), 200

@app.route("/character",methods=["GET"])

def Character():
    character = Character()
    Character.name = request.json.get('name')
    Character.gender = request.json.get('gender')
    Character.hair_color = request.json.get('hair_color')
    Character.eye_color = request.json.get('eye_color')

    db.session.add(character)
    db.session.commit()

    return jsonify(Character.serialize()), 200

@app.route("/planets",methods=["GET"])

def Planets():
    planets = Planets()
    planets.name = request.json.get('name')
    planets.population = request.json.get('population')
    planets.terrain = request.json.get('terrain')
    planets.climate = request.json.get('climate')
    planets.rotate_period = request.json.get('rotate_period')
    planets.orbital_period = request.json.get('orbital_period')

    db.session.add(Planets)
    db.session.commit()

    return jsonify(Plantes,serialize()), 200

#def Favorites():
 #   favorites = Favorites




if __name__ == "__main__":
    app.run(host='localhost',port=8080)




