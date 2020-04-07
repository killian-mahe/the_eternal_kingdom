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

        self.life = 100

        pass

    def getArray(self):
        """Return the Castle as a list of lists
        
        Returns:
            list
        """
        return [self.bg, self.position]

    def get_damages(self, damages):
        """Get damages and return if the monster is dead or not
        
        Arguments:
            damages {int} -- Damages the monster receive
        
        Returns:
            bool -- Wether monster is dead or not
        """
        assert type(damages) is int

        self.life -= damages

        if self.life <= 0:
            return True

        return False

    def is_in_collision(self, ePosition):
        """Check if a given position is in collision with the castle
        
        Arguments:
            ePosition {list} -- 2D position
        
        Returns:
            bool
        """
        assert type(ePosition) is list

        x, y = ePosition
        if x < (self.position[0] + len(self.bg[-1])):
            if y > self.position[1]:
                return True

        return False

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