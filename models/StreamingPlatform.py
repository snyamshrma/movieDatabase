from config.database import db

from peewee import CharField, IntegerField, AutoField

from models.BaseModel import BaseModel


class StreamingPlatform(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)

    class Meta:
        database = db
        db_table = 'streaming_platform'
