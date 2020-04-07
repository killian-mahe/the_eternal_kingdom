# -*- coding: utf-8 -*-

# Standard imports
import math

# Package imports
from IO import Terminal

# Internal imports
from characters import Ball


class Cannon(object):

    def __init__(self, position):
        """Create an instance of Cannon
        
        Arguments:
            position {list} -- 2D coordinates
        """
        assert type(position) is list

        self.position = position
        self.force = 20
        self.angle = 45
        pass

    def shoot(self):
        """Create a Ball with particular settings from the cannon
        
        Returns:
            Ball -- Ball created
        """
        vx = round(math.cos(math.radians(-self.angle)) * self.force, 3)
        vy = round(math.sin(math.radians(-self.angle)) * self.force, 3)
        return Ball(self.position, [vx, vy])

    def show(self, position_range):
        """Display simulation on screen
        
        Arguments:
            position_range {list} -- 2D window size to display simulation
        """
        assert type(position_range) is list
        x_range, y_range = position_range
        
        simulated_ball = self.shoot()

        positions = simulated_ball.simulate(x_range)

        for position in positions :
            x, y = position
            if y > min(y_range) and y < max(y_range) and not x%5:
                Terminal.write("o", position, Terminal.MAGENTA)

        pass

    pass