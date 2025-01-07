import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id_user'))

class User(Base):
    __tablename__ = 'user'   
    id_user = Column(Integer, primary_key=True)
    user_name = Column(String(100), unique=True, nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    caption = Column(String(3000))
    image = Column(String(50))   


class FavoriteVehicles(Base):
    __tablename__ = 'favoritevehicles'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    user_id = Column(Integer, ForeignKey('favorites.id'))
    vehicle = relationship(Vehicles)
    
    
    def __repr__(self):
        return '<FavoriteVehicle %r>' % self.id    


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    caption = Column(String(3000))
    image = Column(String(50))

class FavoriteCharacters(Base):
    __tablename__ = 'favoritecharacters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    user_id = Column(Integer, ForeignKey('favorites.id'))
    character = relationship(Characters)
    

    def __repr__(self):
        return '<FavoriteCharacter %r>' % self.id


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    caption = Column(String(3000))
    image = Column(String(50)) 

class FavoritePlanets(Base):
    __tablename__ = 'favoriteplanets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('favorites.id'))
    planet = relationship(Planets)
    
    
    def __repr__(self):
        return '<FavoritePlanet %r>' % self.id    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
