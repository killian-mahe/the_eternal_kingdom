# -*- coding: utf-8 -*-
import sys

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
                s="\033["+str(y+1+self.position[1])+";"+str(x+1+self.position[0])+"H"

                # Display in white
                sys.stdout.write("\033["+str(37)+"m")

                # Change cursor position
                sys.stdout.write(s)
                
                # Display
                sys.stdout.write(self.bg[y][x])

    pass