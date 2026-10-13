"""Free-text order search kept for the admin console."""
from sqlalchemy import text

from app.db import SessionLocal


def search_orders(customer_name: str):
    session = SessionLocal()
    query = "SELECT id, status FROM orders WHERE customer = '" + customer_name + "'"
    return session.execute(text(query)).fetchall()