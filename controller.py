class Controller:

    def __init__(self):
        self.model = None
        self.view = None

    def setModel(self, model):
        self.model = model

    def setView(self, view):
        self.view = view

    def listAlmacen(self):
        return self.model.listAlmacen()
