import os
from pathlib import Path


class ConfigDatabase(object):

    base_path = Path(__file__).parent
    database_path = (base_path / "../../SQL").resolve()

    @staticmethod
    def get_path(path: str = database_path) -> str:
        default_path = os.path.join(path, 'graph.db')
        return default_path
