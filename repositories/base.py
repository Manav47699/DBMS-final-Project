"""
Base repository with raw SQL execution utilities.
All queries use parameterized statements to prevent SQL injection.
"""
from django.db import connection


def execute_query(query, params=None, fetch=True):
    """
    Execute raw SQL query using Django's connection.
    
    Args:
        query: SQL query string (parameterized with %s placeholders)
        params: Tuple or dict of parameters
        fetch: If True and query is SELECT, return fetchall(); else return None
    
    Returns:
        List of tuples for SELECT, or None for INSERT/UPDATE/DELETE
    """
    with connection.cursor() as cursor:
        cursor.execute(query, params or ())
        if fetch and query.strip().lower().startswith('select'):
            columns = [col[0] for col in cursor.description] if cursor.description else []
            rows = cursor.fetchall()
            if columns and rows:
                return [dict(zip(columns, row)) for row in rows]
            return []
        return None


def execute_insert_return_id(query, params=None):
    """Execute INSERT and return the generated ID. Supports PostgreSQL and SQLite."""
    with connection.cursor() as cursor:
        vendor = connection.vendor
        if vendor == 'postgresql':
            cursor.execute(query + " RETURNING id", params or ())
            row = cursor.fetchone()
            return row[0] if row else None
        else:
            cursor.execute(query, params or ())
            return cursor.lastrowid
