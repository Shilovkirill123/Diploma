from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


engine = create_engine('sqlite:///films.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tagline = Column(String)
    actors = Column(String)
    rating = Column(String)
    year = Column(String)

    def __repr__(self):
        return (
            f"<Film(name: {self.name}, tagline: {self.tagline}," 
            f"actors: {self.actors}, rating: {self.rating}, year: {self.year})>"
        ) 


Film.metadata.create_all(engine)










