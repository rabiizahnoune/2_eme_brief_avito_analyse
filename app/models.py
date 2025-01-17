from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float,text
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

url_base = 'postgresql://admin:rajarabii1@localhost:5433/immobilier_db'

engine = create_engine(url_base)


with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print(result.fetchone())  

Base = declarative_base()


class Annonce(Base):
    __tablename__ = 'annonces'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(String)
    datetime = Column(DateTime)
    nb_rooms = Column(Integer)
    nb_baths = Column(Integer)
    surface_area = Column(Float)
    link = Column(String)
    city_id = Column(Integer, ForeignKey('villes.id'))

    ville = relationship("Ville", back_populates="annonces")
    equipements = relationship("AnnonceEquipement", back_populates="annonce")


class Ville(Base):
    __tablename__ = 'villes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    annonces = relationship("Annonce", back_populates="ville")


class Equipement(Base):
    __tablename__ = 'equipements'

    id = Column(Integer, primary_key=True)
    name = Column(String)  

    annonces = relationship('AnnonceEquipement', back_populates='equipement')


class AnnonceEquipement(Base):
    __tablename__ = 'annonce_equipement'

    annonce_id = Column(Integer, ForeignKey('annonces.id'), primary_key=True)
    equipement_id = Column(Integer, ForeignKey('equipements.id'), primary_key=True)

    annonce = relationship('Annonce', back_populates='equipements')
    equipement = relationship('Equipement', back_populates='annonces')



Base.metadata.create_all(engine)
