# -*- coding: utf-8 -*-

# Standard imports
import time
import math
import copy

# Package imports
from IO import Terminal

class Ball(object):

    g = 9.807 # Gravity constant
    
    def __init__(self, position, speed):
        """Create an instance of Ball
        
        Arguments:
            position {list} -- Initial position
            speed {list} -- Initial speed
        """
        assert type(position) is list
        assert type(speed) is list

        # Initial parameters
        self.init_position = position
        self.init_speed = speed

        # Save create time
        self.init_time = time.time()

        self.position = copy.copy(self.init_position)

        self.power = 1
        
        pass

    def live(self):
        """Live method
        """

        # Compute the t instant for movement equations
        t = round(time.time()-self.init_time, 3)

        # Positional movement equations
        self.position[0] = round((t*self.init_speed[0]) + self.init_position[0])
        self.position[1] = round((0.5*Ball.g*math.pow(t, 2)) + (t*self.init_speed[1]) + (self.init_position[1]))

        pass

    def simulate(self, x_list):
        """Simulate ball mouvement
        
        Arguments:
            x_list {list} -- X range
        
        Returns:
            list -- List of 2D position in the x range given
        """
        assert type(x_list) is list
        positions = list()
        for x in x_list:
            a = (x - self.init_position[0])/(self.init_speed[0])
            y = round((0.5*Ball.g*math.pow(a, 2)) + (a*self.init_speed[1]) + (self.init_position[1]))

            positions.append([x, y])

        return positions
    
    def show(self):
        """Display on the screen
        """

        Terminal.change_color(Terminal.GREEN)
        Terminal.move_cursor(self.position)
        Terminal.write("o")
        
        pass