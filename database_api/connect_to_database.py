import sqlite3


class ConnectToDatabase(object):

    @staticmethod
    def db_connect(db_path):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        return connection, cursor

    @staticmethod
    def db_commit(connection):
        connection.commit()

    @staticmethod
    def db_close(connection):
        connection.close()
