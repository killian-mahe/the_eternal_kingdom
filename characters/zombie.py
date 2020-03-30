# -*- coding: utf-8 -*-

# Standard imports
import time

# Package imports
from IO import Terminal

# Internal imports
from characters import Monster

class Zombie(Monster):

    def __init__(self, monster_model_file, position):
        """Create an instance of Zombie
        
        Arguments:
            monster_model_file {str} -- Where the zombie modele file is stored
            position {list} -- 2D position
        """
        super(Zombie, self).__init__(monster_model_file, position)

        pass

    def live(self):
        """Live method
        """

        if time.time() - self.lastTimeMove > 1/self.speed :
            self.position[0] -= 1
            self.lastTimeMove = time.time()

        pass

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