# -*- coding: utf-8 -*-

# Standard imports
import sys

# Package imports
from IO import Terminal

class Background:

    def __init__(self, file_name):
        """Create an instance of Background
        
        Arguments:
            file_name {str} -- File where the background is stored
        """
        assert type(file_name) is str

        # Read the file
        f = open(file_name, "r")
        txt = f.read()
        f.close()

        # Transfom string into list of lists
        splitedTxt = txt.splitlines()
        self.bg = list()
        for line in splitedTxt :
            self.bg.append(list(line))

        pass

    def update(self, file_name):
        """Update the Background
        
        Arguments:
            file_name {str} -- File where the background is stored
        """
        assert type(file_name) is str

        # Read the file
        f = open(file_name, "r")
        txt = f.read()
        f.close()

        # Transform string into list of lists
        splitedTxt = txt.splitlines()
        self.bg = list()
        for line in splitedTxt :
            self.bg.append(list(line))

        pass

    def getChar(self, x, y):
        """Get the character at a given position
        
        Arguments:
            x {int} -- X parameter
            y {int} -- Y parameter
        
        Returns:
            str -- Character searched
        """
        return self.bg[x][y]

    def setChar(self, x, y, c):
        """Set character at a given position
        
        Arguments:
            x {int} -- X parameter
            y {int} -- Y parameter
            c {str} -- Character to change
        """
        self.bg[x][y] = c

        pass

    def getArray(self):
        """Return the background as a list of lists
        
        Returns:
            list
        """
        return [self.bg, (0, 0)]

    def show(self):
        """Display on the screen
        """
        for y in range(0,len(self.bg)):
            for x in range(0,len(self.bg[y])):
                Terminal.moveCursor([x, y])
                Terminal.changeColor(Terminal.WHITE)
                
                # Display
                Terminal.write(self.bg[y][x])

        pass

    pass