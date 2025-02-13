from config.database import db
from peewee import IntegerField, ForeignKeyField, CharField, AutoField

from models.Movie import Movie
from models.StreamingPlatform import StreamingPlatform
from models.BaseModel import BaseModel


class MoviePlatformMapping(BaseModel):
    id = AutoField(primary_key=True)
    movie = ForeignKeyField(Movie, backref='movie')
    platform = ForeignKeyField(StreamingPlatform, backref='platform')
    url = CharField(max_length=2000)

    class Meta:
        database = db
        table_name = 'movie_platform_mapping'
        # constraints = ['FOREIGN KEY(movie_id) REFERENCES movie(id) ON DELETE CASCADE',
        #                'FOREIGN KEY(platform_id) REFERENCES platform(id) ON DELETE CASCADE']

