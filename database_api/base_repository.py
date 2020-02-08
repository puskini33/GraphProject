# TODO: write class for all repositories where they take the path and dispose method that closes the database
# connection_to_database attribute, check if cursor can be made an attribute,
from database_api.connect_to_database import ConnectToDatabase
from database_api.config_database import ConfigDatabase


class BaseRepository(object):

    def __init__(self):
        self.path = ConfigDatabase.get_path()
        self.connection = ConnectToDatabase.db_connect(self.path)
        self.cursor = self.connection.cursor()


