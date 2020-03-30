# -*- coding: utf-8 -*-

import sys
import termios
import tty

class Terminal():
    """A Terminal
    """

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
        """Init the terminal and set default settings
        """
        Terminal.defaultSettings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        sys.stdout.write("\033[2J") # Clear terminal
        sys.stdout.write("\033[?25l") # Hide cursor
        sys.stdout.write("\033[40m\033[1;34m") # Change bakcground color and characters color
        pass

    @staticmethod
    def write(c, position=None, color = None):
        """Write a character in the Terminal
        
        Arguments:
            c {str} -- The character to display
        
        Keyword Arguments:
            position {tuple(int, int)} -- The position of the cursor (default: {None})
            color {int} -- The color code (default: {None})
        """

        if position :
            assert type(position) is list
            x, y = position
            sys.stdout.write("\033["+str(y+1)+";"+str(x+1)+"H")
        if color :
            assert type(color) is int
            sys.stdout.write("\033["+str(color)+"m")
        sys.stdout.write(str(c))
        pass

    @staticmethod
    def clear():
        """Clear terminal
        """
        sys.stdout.write("\033[2J")
        pass

    @staticmethod
    def moveCursor(position) :
        """Move the cursor to the given position
        
        Arguments:
            position {tple(int, int)} -- Positino of the cursor
        """
        assert type(position) is list

        x, y = position
        sys.stdout.write("\033["+str(y+1)+";"+str(x+1)+"H")
        pass

    @staticmethod
    def changeColor(color):
        """Change the color of the terminal cursor
        
        Arguments:
            color {int} -- The color code
        """
        assert type(color) is int
        sys.stdout.write("\033["+str(color)+"m")
        pass


    @staticmethod
    def reset():
        """Reset terminal to old settings
        """
        sys.stdout.write("\033[0m")
        sys.stdout.write("\033[2J")
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, Terminal.defaultSettings)
        sys.stdout.write("\033[?25h")
        pass
    pass