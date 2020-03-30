# -*- coding: utf-8 -*-
import sys
from IO import Terminal

class Castle:

    def __init__(self, file_name, window_size):
        assert type(file_name) is str
        assert type(window_size) is list

        f = open(file_name, "r")
        txt = f.read()
        f.close()

        splitedTxt = txt.splitlines()
        self.bg = list()

        for line in splitedTxt :
            self.bg.append(list(line))


        self.position = (2-1, window_size[1] - len(self.bg)-1)
        pass

    def getArray(self):
        return [self.bg, self.position]


    def show(self):
        
        for y in range(0,len(self.bg)):
            for x in range(0,len(self.bg[y])):

                # Display in white
                Terminal.changeColor(Terminal.WHITE)

                # Change cursor position
                Terminal.moveCursor([x + self.position[0], y + self.position[1]])
                
                # Display
                Terminal.write(self.bg[y][x])

    pass