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

@app.route("/user",methods=["POST","GET"])
def user():
    if request.method == "GET":
        user = User.query.get(1)
        if user is not None:
            return jsonify(user.serialize())
    else:
        user = User()
        user.name = request.json.get("name")
        user.password = request.json.get("password")
        user.email = request.json.get("email")
        user.isActive = request.json.get("isActive")
        
        
        db.session.add(user)
        db.session.commit()
    

    return jsonify(user.serialize()), 200

@app.route("/vehicles",methods=["GET", "POST"])

def vehicles():
    if request.method == "GET":
        vehicles = Vehicles.query.get(1)
        if vehicles is not None:
            return jsonify(vehicles.serialize())
    else:
        vehicles = Vehicles()
        vehicles.name = request.json.get('name')
        vehicles.model = request.json.get('model')
        vehicles.vehicle_class = request.json.get('vehicle_class')
        vehicles.crews = request.json.get('crews')
        vehicles.manufacturer = request.json.get('manufacturer')
        vehicles.cost_in_credits = request.json.get('cost_in_credits')     
    
        db.session.add(vehicles)
        db.session.commit()

    return jsonify(vehicles.serialize()), 200

@app.route("/character", methods=["POST", "GET"])
def character():    
    if request.method == "GET":
        character = Character.query.get(1)
        if character is not None:
            return jsonify(character.serialize())   
    else:
    
        character = Character()
        character.name = request.json.get("name")
        character.gender = request.json.get("gender")
        character.hair_color = request.json.get("hair_color")
        character.skin_color = request.json.get("skin_color")
         
        db.session.add(character)
        db.session.commit()
    
    return jsonify(character.serialize()), 200

@app.route("/planets", methods=["POST", "GET"])
def planets(): 
    if request.method == "GET":
        planets = Planets.query.get(1)
        if planets is not None:
            return jsonify(planets.serialize())   
    else:
        planets = Planets()
        planets.name = request.json.get("name")
        planets.rotation_period = request.json.get("rotation_period")
        planets.climate = request.json.get("climate")
        planets.terrain = request.json.get("terrain")
        planets.population = request.json.get("population")
        
            
        db.session.add(planets)
        db.session.commit()
    
    return jsonify(planets.serialize()), 200


if __name__ == "__main__":
    app.run(host='localhost',port=8080)




