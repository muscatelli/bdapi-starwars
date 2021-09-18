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
