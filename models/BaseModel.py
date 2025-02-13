from peewee import Model
from config.database import db


# Base model to use for all Peewee models
class BaseModel(Model):
    class Meta:
        database = db

    @classmethod
    def create_all_tables(cls):
        """Automatically create tables for all subclasses of BaseModel."""
        subclasses = cls.__subclasses__()  # Get all models extending BaseModel
        db.create_tables(subclasses, safe=True)

    @classmethod
    def getById(self, record_id):
        """Get a record by ID or return None if not found."""
        return self.get_or_none(self.id == record_id)

    @classmethod
    def getOne(self, **query):
        """Get a single record based on filters or return None."""
        if query:
            return self.select().where(*[getattr(self, key) == value for key, value in query.items()]).first()
        return self.select().first().execute()

    @classmethod
    def getAll(self, **query):
        """Get all records that match the filters."""
        if query:
            return self.select().where(*[getattr(self, key) == value for key, value in query.items()]).execute()
        return self.select().execute()

    @classmethod
    def countRecords(self, **query):
        """Count total records with optional filters."""
        if query:
            return self.select().where(*[getattr(self, key) == value for key, value in query.items()]).count()
        return self.select().count()
