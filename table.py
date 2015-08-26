from os import path

root_path = path.abspath(path.dirname(__file__))

class Table(object):

    def __init__(self, name):
        self.name = name

    def _sql(self, operation):
        file_path = '{root_path}/tables/{directory}/{operation}.sql'.format(
            root_path=root_path,
            directory=self.name,
            operation=operation)
        with open(file_path, 'rb') as file_handle:
            return file_handle.read()

    @property
    def create_sql(self):
        return self._sql('create')

    @property
    def insert_sql(self):
        return self._sql('insert')

    def insert(self, cursor, values):
        cursor.execute(self.insert_sql, values)
        return cursor.lastrowid

    def create(self, cursor):
        cursor.execute(self.create_sql)
