# -*- coding: utf-8 -*-

# Standard imports
import sys

# Package imports
from IO import Terminal

class Castle:

    def __init__(self, file_name, window_size):
        """Create an instance of Castle
        
        Arguments:
            file_name {str} -- File where the castle appearance is stored
            window_size {list} -- Window size
        """
        assert type(file_name) is str
        assert type(window_size) is list

        # Read the file
        f = open(file_name, "r")
        txt = f.read()
        f.close()

        # Transform string into list of lists
        splitedTxt = txt.splitlines()
        self.bg = list()
        for line in splitedTxt :
            self.bg.append(list(line))

        # Change the position of the Castle
        self.position = (2-1, window_size[1] - len(self.bg)-1)

        pass

    def getArray(self):
        """Return the Castle as a list of lists
        
        Returns:
            list
        """
        return [self.bg, self.position]


    def show(self, offset=[0, 0]):
        """Display on the screen
        """
        for y in range(0,len(self.bg)):
            for x in range(0,len(self.bg[y])):

                # Display in white
                Terminal.changeColor(Terminal.WHITE)

                # Change cursor position
                Terminal.moveCursor([x + self.position[0], y + self.position[1]])
                
                # Display
                Terminal.write(self.bg[y][x])

        pass

    pass