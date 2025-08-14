import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_db():
    return psycopg2.connect(
        host="127.0.0.1",
        port=os.getenv("POSTGRES_PORT"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )