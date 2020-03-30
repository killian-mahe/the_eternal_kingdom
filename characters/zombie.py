# -*- coding: utf-8 -*-

# Standard imports
import time

# Package imports
from IO import Terminal

# Internal imports
from characters import Monster

class Zombie(Monster):

    def __init__(self, monster_model_file, position, life=1):
        """Create an instance of Zombie
        
        Arguments:
            monster_model_file {str} -- Where the zombie modele file is stored
            position {list} -- 2D position

        Keyword Arguments:
            life {int} -- Monster life (default: {1})
        """
        super(Zombie, self).__init__(monster_model_file, position, life)

        pass

    def live(self):
        """Live method
        """

        if time.time() - self.lastTimeMove > 1/self.speed :
            self.position[0] -= 1
            self.lastTimeMove = time.time()

        pass

    pass