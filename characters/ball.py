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
        self.initPosition = position
        self.initSpeed = speed

        # Save create time
        self.initTime = time.time()

        self.position = copy.copy(self.initPosition)

        self.power = 1
        
        pass

    def live(self):
        """Live method
        """

        # Compute the t instant for movement equations
        t = round(time.time()-self.initTime, 3)

        # Positional movement equations
        self.position[0] = round((t*self.initSpeed[0]) + self.initPosition[0])
        self.position[1] = round((0.5*Ball.g*math.pow(t, 2)) + (t*self.initSpeed[1]) + (self.initPosition[1]))

        pass

    def show(self):
        """Display on the screen
        """

        Terminal.changeColor(Terminal.GREEN)
        Terminal.moveCursor(self.position)
        Terminal.write("o")
        
        pass