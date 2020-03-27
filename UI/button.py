# -*- coding: utf-8 -*-
import sys

class Button:

    def __init__(self, position, label, action=None):
        assert type(position) is tuple
        assert type(label) is str

        self.x, self.y = position
        self.label = label
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