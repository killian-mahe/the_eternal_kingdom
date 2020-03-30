# -*- coding: utf-8 -*-
from IO import Terminal
import time
import math
import copy

class Ball(object):

    g = 9.807
    
    def __init__(self, position, speed):
        assert type(position) is list
        assert type(speed) is list
        
        self.initPosition = position
        self.initSpeed = speed
        self.initTime = time.time()

        self.position = copy.copy(position)

        pass

    def live(self):

        t = round(time.time()-self.initTime, 3)

        # Position
        self.position[0] = round((t*self.initSpeed[0]) + self.initPosition[0])
        self.position[1] = round((0.5*Ball.g*math.pow(t, 2)) + (t*self.initSpeed[1]) + (self.initPosition[1]))

        pass

    def show(self):
        Terminal.changeColor(Terminal.GREEN)
        Terminal.moveCursor(self.position)
        Terminal.write("o")
        pass