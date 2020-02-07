import os


class ConfigDatabase(object):

    @staticmethod
    def get_path(path='E:\\PYTHON\\code\\GraphProject\\SQL'):
        default_path = os.path.join(os.path.dirname(__file__), 'graph.db')
        return default_path
