# -*- coding: utf-8 -*-
import sys

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

    def getChar(self, x, y):
        return self.bg[x][y]

    def setChar(self, x, y, c):
        self.bg[x][y] = c

    def show(self):
        for y in range(0,len(self.bg)):
            for x in range(0,len(self.bg[y])):
                s="\033["+str(y+1)+";"+str(x+1)+"H"
                sys.stdout.write("\033["+str(37)+"m")
                sys.stdout.write(s)
                
                # Display
                sys.stdout.write(self.bg[y][x])
    pass