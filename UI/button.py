# -*- coding: utf-8 -*-
import sys
from UI.element import Element

class Button(Element):

    def __init__(self, position, label, action=None):
        super.__init__(position, label)
        
        self.selected = False

        if action:
            self.action = action
        
        pass

    def select(self, selected):
        assert type(selected) is bool
        self.selected = selected

    def show(self):
        s="\033["+str(self.y+1)+";"+str(self.x+1)+"H"
        sys.stdout.write(s)
        if self.selected :
            sys.stdout.write("\033["+str(33)+"m") # Change color to yellow
        else :
            sys.stdout.write("\033["+str(37)+"m") # Reset color to white

        sys.stdout.write(str(self.label))

    pass