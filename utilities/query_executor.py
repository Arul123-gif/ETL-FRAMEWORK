from sqlalchemy import text
from utilities.db_connection import get_engine

engine = get_engine()

def execute_scalar(query):

    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.scalar()

def fetch_all(query):

    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()

def fetch_one(query):

    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchone()