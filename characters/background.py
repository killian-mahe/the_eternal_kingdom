# -*- coding: utf-8 -*-
import sys
from IO import Terminal

class Background:

    def __init__(self, file_name):
        assert type(file_name) is str

        f = open(file_name, "r")
        txt = f.read()
        f.close()

        splitedTxt = txt.splitlines()
        self.bg = list()

        for line in splitedTxt :
            self.bg.append(list(line))

        pass

    def update(self, file_name):
        assert type(file_name) is str

        f = open(file_name, "r")
        txt = f.read()
        f.close()

        splitedTxt = txt.splitlines()
        self.bg = list()

        for line in splitedTxt :
            self.bg.append(list(line))
        pass

    def getChar(self, x, y):
        return self.bg[x][y]

    def setChar(self, x, y, c):
        self.bg[x][y] = c

    def getArray(self):
        return [self.bg, (0, 0)]

    def show(self):
        for y in range(0,len(self.bg)):
            for x in range(0,len(self.bg[y])):
                Terminal.moveCursor([x, y])
                Terminal.changeColor(Terminal.WHITE)
                
                # Display
                Terminal.write(self.bg[y][x])
    pass