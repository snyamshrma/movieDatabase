from config.database import db
from models.BaseModel import BaseModel
from peewee import CharField, AutoField


# Base model to use for all Peewee models
class Movie(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    year = CharField()
    imdb_id = CharField()

    class Meta:
        database = db
        db_table = 'movie'
