# -*- coding: utf-8 -*-

import sys
import termios
import tty

class Terminal():

    defaultSettings = None

    # Color constants
    WHITE = 37
    GREEN = 32
    BLACK = 30
    RED = 31
    YELLOW = 33
    BLUE = 34
    CYAN = 36
    MAGENTA = 35

    @staticmethod
    def init():
        Terminal.defaultSettings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        sys.stdout.write("\033[2J") # Clear terminal
        sys.stdout.write("\033[?25l") # Hide cursor
        sys.stdout.write("\033[40m\033[1;34m") # Change bakcground color and characters color
        pass

    @staticmethod
    def write(c, position, color = None):
        assert type(c) is str
        assert type(position) is tuple

        x, y = position
        sys.stdout.write("\033["+str(y+1)+";"+str(x+1)+"H")
        if color :
            assert type(color) is int
            sys.stdout.write("\033["+str(color)+"m")
        sys.stdout.write(c)
        pass

    @staticmethod
    def moveCursor(position) :
        assert type(position) is tuple

        x, y = position
        sys.stdout.write("\033["+str(y+1)+";"+str(x+1)+"H")
        pass

    @staticmethod
    def changeColor(color):
        assert type(color) is int
        sys.stdout.write("\033["+str(color)+"m")
        pass


    @staticmethod
    def reset():
        sys.stdout.write("\033[0m")
        sys.stdout.write("\033[2J")
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, Terminal.defaultSettings)
        sys.stdout.write("\033[?25h")
        pass
    pass