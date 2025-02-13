from config.database import db
from peewee import CharField, IntegerField, AutoField

from models.BaseModel import BaseModel


# Base model to use for all Peewee models
class Genre(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()

    class Meta:
        database = db
        db_table = 'genre'
