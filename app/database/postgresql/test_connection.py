# test_connection.py
from sqlmodel import text
from postgresql_connection import get_session

session = next(get_session())
result = session.exec(text("SELECT version()"))
print(f"Connected: {result.scalar()}")
session.close()