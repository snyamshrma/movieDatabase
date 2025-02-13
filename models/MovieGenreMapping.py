from config.database import db
from peewee import IntegerField, ForeignKeyField, AutoField

from models.Movie import Movie
from models.Genre import Genre
from models.BaseModel import BaseModel


class MovieGenreMapping(BaseModel):
    id = AutoField(primary_key=True)
    movie = ForeignKeyField(Movie, backref='movie')
    genre = ForeignKeyField(Genre, backref='genre')

    class Meta:
        database = db
        table_name = 'movie_genre_mapping'
        # constraints = ['FOREIGN KEY(movie_id) REFERENCES movie(id) ON DELETE CASCADE',
        #                'FOREIGN KEY(genre_id) REFERENCES genre(id) ON DELETE CASCADE']


