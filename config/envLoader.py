import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Access environment variables
db_host = os.getenv("DATABASE_HOST")
db_user = os.getenv("DATABASE_USER")
db_password = os.getenv("DATABASE_PASSWORD")
db_name = os.getenv("DATABASE_NAME")
db_port = os.getenv("DATABASE_PORT")
rapid_api_key = os.getenv("RAPID_API_KEY")
rapid_api_host = os.getenv("RAPID_API_HOST")
