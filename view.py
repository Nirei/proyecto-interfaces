from guizero import App, Box, ListBox, PushButton, Text, TextBox

DETALLE_LABEL_FSIZE = 10

class View:

    def __init__(self, controller):
        self.almacenes = []
        self.selected = None

        self.controller = controller
        self.app = App(title="Interfaces", layout="grid", width=600, height=200)

        # 0, 0
        self.lista = ListBox(self.app, items=[], grid=[0,0], command=self.handleListChange)
        self.lista.width = 30

        # 1, 0
        self.detalle = Box(self.app, grid=[1,0], layout="grid")
        self.nombreLabel = Text(self.detalle, size=DETALLE_LABEL_FSIZE, text="Nombre", grid=[0,0])
        self.direcionLabel = Text(self.detalle, size=DETALLE_LABEL_FSIZE, text="Dirección", grid=[0,1])
        self.provinciaLabel = Text(self.detalle, size=DETALLE_LABEL_FSIZE, text="Provincia", grid=[0,2])
        self.cpLabel = Text(self.detalle, size=DETALLE_LABEL_FSIZE, text="CP", grid=[0,3])
        self.telefonoLabel = Text(self.detalle, size=DETALLE_LABEL_FSIZE, text="Teléfono", grid=[0,4])

        self.nombre = TextBox(self.detalle, "", grid=[1,0], width=30, enabled=False)
        self.direccion = TextBox(self.detalle, "", grid=[1,1], width=30, enabled=False)
        self.provincia = TextBox(self.detalle, "", grid=[1,2], width=30, enabled=False)
        self.cp = TextBox(self.detalle, "", grid=[1,3], width=30, enabled=False)
        self.telefono = TextBox(self.detalle, "", grid=[1,4], width=30, enabled=False)

        # 0, 1
        self.toolbar = Box(self.app, grid=[0,1], layout="grid")
        self.buttonEdit = PushButton(self.toolbar, command=self.handleEdit, text="Editar", grid=[0,0])
        self.buttonAdd = PushButton(self.toolbar, command=self.handleAdd, text="Añadir", grid=[1,0])

        # 1, 1
        self.detalleToolbar = Box(self.app, grid=[1,1], layout="grid")
        self.buttonSave = PushButton(self.detalleToolbar, command=self.handleSave, text="Guardar", grid=[0,0], enabled=False)

    def start(self):
        self.refreshData()
        self.app.display()

    def refreshData(self):
        self.almacenes = self.controller.listAlmacen()
        self.lista.clear()
        [self.lista.append(x[1]) for x in self.almacenes]

    def editableState(self, editable):
        self.nombre.enabled = editable
        self.direccion.enabled = editable
        self.provincia.enabled = editable
        self.cp.enabled = editable
        self.telefono.enabled = editable
        self.buttonSave.enabled = editable

    def handleListChange(self, nombreAlmacen):
        [self.selected] = [tupla for tupla in self.almacenes if tupla[1] == nombreAlmacen]
        self.nombre.value = self.selected[1]
        self.direccion.value = self.selected[2]
        self.provincia.value = self.selected[3]
        self.cp.value = self.selected[4]
        self.telefono.value = self.selected[5]
        self.editableState(False)

    def handleEdit(self):
        if self.selected:
            self.editableState(True)

    def handleAdd(self):
        pass

    def handleSave(self):
        actualizado = (
            self.selected[0],
            self.nombre.value,
            self.direccion.value,
            self.provincia.value,
            self.cp.value,
            self.telefono.value
        )
        self.controller.updateAlmacen(actualizado)
        self.refreshData()
        self.editableState(False)
