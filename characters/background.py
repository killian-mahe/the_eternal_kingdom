# -*- coding: utf-8 -*-

# Standard imports
import sys

# Package imports
from IO import Terminal, File

class Background:

    def __init__(self, file_name):
        """Create an instance of Background
        
        Arguments:
            file_name {str} -- File where the background is stored
        """
        assert type(file_name) is str

        # Read the file
        self.bg = File.read_as_array(file_name)

        pass

    def update(self, file_name):
        """Update the Background
        
        Arguments:
            file_name {str} -- File where the background is stored
        """
        assert type(file_name) is str

        # Read the file
        self.bg = File.read_as_array(file_name)

        pass

    def get_char(self, x, y):
        """Get the character at a given position
        
        Arguments:
            x {int} -- X parameter
            y {int} -- Y parameter
        
        Returns:
            str -- Character searched
        """
        return self.bg[x][y]

    def set_char(self, x, y, c):
        """Set character at a given position
        
        Arguments:
            x {int} -- X parameter
            y {int} -- Y parameter
            c {str} -- Character to change
        """
        self.bg[x][y] = c

        pass

    def get_array(self):
        """Return the background as a list of lists
        
        Returns:
            list
        """
        return [self.bg, (0, 0)]

    def show(self, offset=[0, 0]):
        """Display on the screen
        """
        for y in range(0,len(self.bg)):
            for x in range(0,len(self.bg[y])):
                Terminal.move_cursor([offset[0]+x, offset[1]+y])
                Terminal.change_color(Terminal.WHITE)
                
                # Display
                Terminal.write(self.bg[y][x])

        pass

    pass