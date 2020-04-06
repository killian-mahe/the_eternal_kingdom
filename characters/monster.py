# -*- coding: utf-8 -*-

# Standard imports
import random
import time

# Package imports
from IO import Terminal, File


class Monster:
    
    def __init__(self, monster_model_file, position, life=1):
        """Create an instance of Monster
        
        Arguments:
            monster_model_file {str} -- File where monster model is stored
            position {list} -- 2D position
        
        Keyword Arguments:
            life {int} -- Monster life (default: {1})
        """
        assert type(monster_model_file) is str
        assert type(position) is list

        # Read the file
        self.model = File.read_as_array(monster_model_file)

        x, y = position
        self.position = [x, y-len(self.model)]
        self.speed = 3 # px/sec
        self.last_time_move = 0

        self.life = life
        self.score = life

        pass

    def is_in_collision(self, ePosition):
        """Check if position is in collision with the monster
        
        Arguments:
            ePosition {list} -- Coordinates to check
        
        Returns:
            bool
        """
        assert type(ePosition) is list

        if ePosition[0] >= self.position[0] and ePosition[0] < (self.position[0] + len(self.model[0])) :
            if ePosition[1] >= self.position[1] and ePosition[1] < (self.position[1] + len(self.model)) :
                return True
        
        return False

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
                if self.model[y][x] != " ":
                    Terminal.move_cursor([self.position[0] + x, self.position[1] + y])
                    Terminal.change_color(Terminal.WHITE)
                    
                    # Display
                    Terminal.write(self.model[y][x])

        Terminal.write("[" + str(self.life) + "]", [self.position[0], self.position[1]-1], Terminal.BLUE)
            
        pass

    pass