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
<<<<<<< HEAD
    id_kinopoisk = Column(String, unique = True)
    name = Column(String)
    tagline = Column(String)
    actors = Column(String)
    director = Column(String)
    rating = Column(String)
    rating_imdb = Column(String)
=======
    name = Column(String)
    tagline = Column(String)
    actors = Column(String)
    rating = Column(String)
>>>>>>> 009bac50268e7266c7b3b60acd5f6dee55c07af0
    year = Column(String)

    def __repr__(self):
        return (
<<<<<<< HEAD
            f'https://www.kinopoisk.ru/film/{self.id_kinopoisk}\nНазвание фильма: {self.name}\nСлоган: {self.tagline}\n' 
            f'Актеры: {self.actors}\nРежисер: {self.director}\nРейтинг: {self.rating}\n'
            f'Рейтинг imdb: {self.rating_imdb}\nГод: {self.year}'
=======
            f"<Film(name: {self.name}, tagline: {self.tagline}," 
            f"actors: {self.actors}, rating: {self.rating}, year: {self.year})>"
>>>>>>> 009bac50268e7266c7b3b60acd5f6dee55c07af0
        ) 


Film.metadata.create_all(engine)










