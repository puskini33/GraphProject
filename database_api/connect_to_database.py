import sqlite3


class ConnectToDatabase(object):

    @staticmethod
    def db_connect(db_path):
        connection = sqlite3.connect(db_path)

        return connection

    @staticmethod
    def db_commit(connection):
        cursor = connection.cursor()
        return cursor

    @staticmethod
    def db_close(connection):
        connection.close()
