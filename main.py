#!/usr/bin/env python3
from controller import Controller
from model import Model
from view import View

controller = Controller()
model = Model(controller)
view = View(controller)

controller.setModel(model)
controller.setView(view)

view.start()
