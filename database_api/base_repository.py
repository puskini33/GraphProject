from database_api.config_database import ConfigDatabase
import sqlite3


class BaseRepository(object):

    def __init__(self, path):
        if path:
            self.path = path
        else:
            self.path = ConfigDatabase.get_path()
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()

    def execute_query(self, sql_query):
        self.cursor.execute(sql_query)
        self.connection.commit()

    def close_connection(self):
        return self.connection.close()
