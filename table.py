import sqlite3

# Crea una conexión a la BD, desactiva la transaccionalidad
conn = sqlite3.connect('interfaces.db', isolation_level=None)

class Table:

    def __init__(self, tableName):
        self.tableName = tableName

    def get(self, id):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM %s WHERE id=?' % self.tableName, id)
        return cursor

    def findAll(self):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM %s' % self.tableName)
        return cursor

    def create(self, data):
        pass

    def update(self, data):
        pass

    def delete(self, id):
        cursor = conn.cursor()
        cursor.execute('DELETE FROM %s WHERE id=?' % self.tableName, id)
