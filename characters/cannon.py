# -*- coding: utf-8 -*-
from characters import Ball
from IO import Terminal
import math

class Cannon(object):

    def __init__(self, position):
        assert type(position) is list

        self.position = position
        self.force = 20
        self.angle = 45
        pass

    def shoot(self):
        vx = round(math.cos(math.radians(-self.angle)) * self.force, 3)
        vy = round(math.sin(math.radians(-self.angle)) * self.force, 3)
        return Ball(self.position, [vx, vy])

    def show(self):
        pass

    pass