# TODO: write class for all repositories where they take the path and dispose method that closes the database
# connection_to_database attribute, check if cursor can be made an attribute,
from database_api.connect_to_database import ConnectToDatabase
from database_api.config_database import ConfigDatabase


class BaseRepository(object):

    def __init__(self):
        self.path = ConfigDatabase.get_path()
        self.connection, self.cursor = ConnectToDatabase.db_connect(self.path)
        self.commit = ConnectToDatabase.db_commit(self.connection)
        self.close_database = ConnectToDatabase.db_close(self.connection)
        # I think there will also be here a problem at the commit(), close thing

    def open_database(self):
        return self.connection, self.cursor

    def commit_to_database(self):
        return self.commit

    def close_database(self):
        return self.close_database


