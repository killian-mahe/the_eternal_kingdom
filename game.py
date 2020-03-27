# -*- coding: utf-8 -*-
import sys
import background
import castle
import screen
from UI.menu import Menu

class Game:

    def __init__(self, _background, _castle):
        assert type(_background) is background.Background
        assert type(_castle) is castle.Castle

        self.background = _background
        self.castle = _castle
        self.menus = None

        self.currentMenu = None

        pass

    def addMenu(self, menus):
        assert (type(menus) is list) or (type(menus) is Menu)

        if type(menus) is list :
            for menu in menus:
                self.menus[menu.label] = menu
        else :
            self.menus = {str(menus.label): menus}
        pass

    def setMenu(self, label):
        assert type(label) is str
        
        self.currentMenu = self.menus[label]
        pass

    def resetMenu(self):
        self.currentMenu = None
        pass

    def show(self):

        if self.currentMenu != None:
            self.currentMenu.show()
        else :
            self.background.show()
            self.castle.show()
        pass

    pass