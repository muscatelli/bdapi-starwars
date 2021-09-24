from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    email=db.Column(db.String(30), nullable=False)
    isActive= db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<User %r>" % self.id

    def serialize(self):
        return{
     'name': self.name,
     'password': self.password,
     'email': self.email,
     'isActive': self.isActive
    
}

    def serialize_just_username(self):
        return{
    'id':self.id,
    'name':self.name
}

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable= False)
    model = db.Column(db.String(10))
    vehicle_class=db.Column(db.String(30))
    crews =db.Column(db.String(30))
    manufacturer=db.Column(db.String(30))
    cost_in_credits=db.Column(db.String(30))
    favorite = db.relationship("Favorite",lazy=True)
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))

    

    def __repr__(self):
        return "<vehicles %r>" % self.id

    def serialize(self):
        return{
    'id': self.id,
    'name': self.name,
    'model': self.model,
    'vehicle_class': self.vehicle_class,
    'crews': self.crews,
    'manufacturer': self.manufacturer,
    'cost_in_credits': self.cost_in_credits
        }

class Character(db.Model):
    __tablename__ = 'character'
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    gender = db.Column(db.String(30))
    hair_color = db.Column(db.String(30))
    skin_color = db.Column(db.String(30))
    favorite = db.relationship("Favorite",lazy=True)
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))

    def __repr__(self):
        return "<character %r>" % self.id
    
    def serialize(self):
        return{
    'id': self.id,
    'name': self.name,
    'gender': self.gender,
    'hair_color': self.hair_color,
    'skin_color': self.skin_color        
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    rotation_period = db.Column(db.String(10))
    climate = db.Column(db.String(30), nullable=False)
    terrain = db.Column(db.String(30), default=False)
    population = db.Column(db.String(30), default=False)
    favorite = db.relationship("Favorite",lazy=True)
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))
    
    

    def __repr__(self):
        return "<Planets %r>" % self.id
    
    def serialize(self):
        return {
            'id': self.id,
            'name':self.name,
            'rotation_period':self.rotation_period,
            'climate':self.climate,
            'terrain':self.terrain,
            'population':self.population,
        }


class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(30))
    favorite_name = db.Column(db.String(50))
    user = db.relationship("User",backref=db.backref('user',lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Favorites %r>" % self.id
    
    def serialize(self):
        return {
            'id':self.id,
            'category':self.category,
            'favorite_name':self.favorite_name,
            'user_id':self.user_id
        }

    def serialize_just_user_fav(self):
        return{
        'id': self.id,
        'category': self.category,
        'favorite_name':self.favorite_name
        }

#class Favorite(db.Model):
#    __tablename__ = 'favorites'
#    id= db.Column(db.Integer, primary_key=True)
#    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
#    fav_planet = db.Column(db.Integer, db.ForeignKey('planets.planet.id'))
#.   fav_character = db.Column(db.Integer, db.ForeignKey('character.character.character.id'))
#.   fav_vehicles= db.Column(db.Integer, db.ForeignKey('vehicles.vehicles.id'))


#   def __repr__(self):
#       return "<Favorite %r>" % self.id

#    def serialize(self):
#         return{
     #       'id_user': self.id_user,
      #      'id_fav': self.id_fav,
       #     'fav_planet': self.fav_name,
        #    'fav_character': self.fav_Section,
        #    'fav_vehicles': self.fav_vehicles
        #}

