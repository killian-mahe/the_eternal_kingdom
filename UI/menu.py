# -*- coding: utf-8 -*-
from UI import button
import sys

class Menu:

    def __init__(self, label="", _buttons = []):
        self.buttons = _buttons
        self.label = label
        pass

    def addButton(self, _button):
        assert type(_button) is button.Button
        print(self.buttons)
        self.buttons.append(_button)
        pass

    def show(self):
        for button in self.buttons:
            button.show()