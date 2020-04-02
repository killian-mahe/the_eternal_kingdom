# -*- coding: utf-8 -*-

# Standard imports
import sys

# Package imports
from IO import Terminal, File

class Castle:

    def __init__(self, file_name, window_size):
        """Create an instance of Castle
        
        Arguments:
            file_name {str} -- File where the castle appearance is stored
            window_size {list} -- Window size
        """
        assert type(file_name) is str
        assert type(window_size) is list

        # Get background
        self.bg = File.read_as_array(file_name)

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
                Terminal.change_color(Terminal.WHITE)

                # Change cursor position
                Terminal.move_cursor([x + self.position[0], y + self.position[1]])
                
                # Display
                Terminal.write(self.bg[y][x])

        pass

    pass