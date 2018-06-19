from guizero import App, PushButton, Text

class View:

    def __init__(self, controller):
        self.controller = controller
        self.app = App(title="Interfaces")
        self.text = Text(self.app, "")
        self.button = PushButton(self.app, command=self.onButtonClick)

    def start(self):
        self.app.display()

    def setText(self, text):
        self.text.value = text

    def onButtonClick(self):
        almacenes = self.controller.listAlmacen()
        self.setText(''.join(str(e) for e in almacenes))
