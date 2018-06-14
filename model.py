from table import Table

class Model:

    def __init__(self, controller):
        self.controller = controller
        self.tablaAlmacen = Table('Almacen')
        self.tableLineaArticulos = Table('LineaArticulos')

    def addAlmacen(self, almacen):
        self.tablaAlmacen.create(almacen)

    def listAlmacen(self):
        return [almacen for almacen in self.tablaAlmacen.findAll()]
