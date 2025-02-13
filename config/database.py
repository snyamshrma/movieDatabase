from peewee import MySQLDatabase

from config import envLoader

# Access environment variables
db_host = envLoader.db_host
db_user = envLoader.db_user
db_password = envLoader.db_password
db_name = envLoader.db_name
db_port = envLoader.db_port

# Establish the database connection
db = MySQLDatabase(db_name, host=db_host, port=int(db_port), user=db_user, password=db_password)


# Function to connect to the database
def connect_db(db):
    if db.is_closed():
        db.connect()


# Function to close the database connection
def close_db():
    if not db.is_closed():
        db.close()
