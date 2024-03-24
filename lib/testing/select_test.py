import sqlite3
import os
import pytest

from lib import sql_queries

# Set up connection to in-memory SQLite database
@pytest.fixture
def connection():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Run SQL scripts to create and populate tables
    with open(os.path.join(os.path.dirname(__file__), "../lib/create.sql"), "r") as create_file:
        create_as_string = create_file.read()
        cursor.executescript(create_as_string)

    with open(os.path.join(os.path.dirname(__file__), "../lib/seed.sql"), "r") as seed_file:
        seed_as_string = seed_file.read()
        cursor.executescript(seed_as_string)

    return conn

# Test cases for SQL queries
def test_select_all_female_bears_return_name_and_age(connection):
    cursor = connection.cursor()
    cursor.execute(sql_queries.select_all_female_bears_return_name_and_age)
    result = cursor.fetchall()
    assert len(result) == 2
    assert ("Tabitha", 7) in result
    assert ("Melissa", 2) in result

def test_select_alive_brown_bears_return_name_and_age(connection):
    cursor = connection.cursor()
    cursor.execute(sql_queries.select_alive_brown_bears_return_name_and_age)
    result = cursor.fetchall()
    assert len(result) == 1
    assert ("Mr. Chocolate", 5) in result