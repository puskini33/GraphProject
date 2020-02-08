import os


class ConfigDatabase(object):

    @staticmethod
    def get_path(path='E:\\PYTHON\\code\\GraphProject\\SQL'):
        default_path = os.path.join(path, 'graph.db')
        return default_path
