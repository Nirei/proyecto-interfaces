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
        cursor.execute('SELECT rowid, * FROM %s' % self.tableName)
        return cursor

    def create(self, data):
        pass

    def update(self, data):
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE %s SET nombre=?, direccion=?, provincia=?, cp=?, telefono=? WHERE rowid=?' % self.tableName,
            (data[1], data[2], data[3], data[4], data[5], data[0])
        )
        return cursor

    def delete(self, id):
        cursor = conn.cursor()
        cursor.execute('DELETE FROM %s WHERE id=?' % self.tableName, id)
