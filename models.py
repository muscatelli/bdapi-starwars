from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    email=db.Column(db.String(30), nullable=False)
    isActive= db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<User %r>" % self.id

    def serialize(self):
        return{
    'id': self.id,
    'name': self.name,
    'password': self.password,
    'isActive': self.isActive
}

    def serialize_just_username(self):
        return{
    'id':self.id,
    'name':self.name
}

class Vehicles(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(10), nullable=False)
    vehicle_class=db.Column(db.String(30), nullable=False)
    crews=db.Column(db.String(30), nullable=False)
    manufacturer=db.Column(db.String(30), nullable=False)
    cost_in_credits=db.Column(db.String(30), nullable=False)
    

    def __repr__(self):
        return "<vehicles %r>" % self.id

    def serialize(self):
        return{
    'id': self.id,
    'name': self.name,
    'model': self.model,
    'vechicle_class': self.vechicle_class,
    'crew': self.crew,
    'manufacturer': self.manufacturer,
    'cost_in_credits': self.cost_in_credits
        }

class Character(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    hair_color = db.Column(db.String(30), nullable=False)
    eye_color = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return "<character %r>" % self.id
    
    def serialize(self):
        return{
    'id': self.id,
    'name': self.name,
    'gender': self.gender,
    'hair_color': self.hair_color,
    'eye_color': self.eye_color        
        }

class Planets(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(30), nullable=True)
    population= db.Column(db.String(30), nullable=True)
    terrain= db.Column(db.String(30), nullable=True)
    climate= db.Column(db.String(30), nullable=True)
    rotate_period= db.Column(db.Integer, nullable=True)
    orbital_period= db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return "<planets %r>" % self.id

    def serialize(self):
        return{
        'id': self.id,
        'name': self.name,
        'population': self.population,
        'terrain': self.terrain,
        'climate': self.climate,
        'rotate_period': self.sel.rotate_period,
        'orbital_period': self.orbital_period
        }