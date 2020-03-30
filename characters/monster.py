# -*- coding: utf-8 -*-

# Standard imports
import random
import time

# Package imports
from IO import Terminal


class Monster:
    
    def __init__(self, monster_model_file, position):
        """Create an instance of Monster
        
        Arguments:
            monster_model_file {str} -- File where monster model is stored
            position {list} -- 2D position
        """
        assert type(monster_model_file) is str
        assert type(position) is list

        # Read the file
        f = open(monster_model_file, "r")
        txt = f.read()
        f.close()

        # Transform string info list of lists
        splitedTxt = txt.splitlines()
        self.model = list()
        for line in splitedTxt :
            self.model.append(list(line))

        self.position = position
        self.speed = 3 # px/sec
        self.lastTimeMove = 0

        pass

    def live(self):
        """Live
        
        Raises:
            NotImplementedError: Abstract method, must be implemented
        """
        raise NotImplementedError

    def show(self):
        """Display on the screen
        """
        for y in range(0,len(self.model)):
            for x in range(0,len(self.model[y])):
                Terminal.moveCursor([self.position[0] + x, self.position[1] + y - len(self.model)])
                Terminal.changeColor(Terminal.WHITE)
                
                # Display
                Terminal.write(self.model[y][x])
            
        pass

    pass