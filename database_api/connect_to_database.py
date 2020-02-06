import os
import sqlite3


DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'graph.db')


def db_connect(db_path=DEFAULT_PATH):
    connection = sqlite3.connect(db_path)
    return connection


def create_cursor(connection):
    cursor = connection.cursor()
    return cursor
