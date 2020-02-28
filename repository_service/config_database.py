import os


class ConfigDatabase(object):

    @staticmethod
    def get_path(path: str = 'E:\\PYTHON\\code\\GraphProject\\SQL') -> str:
        default_path = os.path.join(path, 'graph.db')
        return default_path
