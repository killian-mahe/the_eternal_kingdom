# -*- coding: utf-8 -*-

import sys
import termios
import tty

class Terminal:
    """A Terminal
    """

    default_settings = None

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
        Terminal.default_settings = termios.tcgetattr(sys.stdin)
        Terminal.cbreak_input_mode()
        Terminal.clear()
        Terminal.hide_cursor()
        sys.stdout.write("\033[40m\033[1;34m") # Change bakcground color and characters color
        pass

    @staticmethod
    def raw_input_mode():
        """Set the terminal input mode to raw
        """
        tty.setraw(sys.stdin.fileno())
        
        pass

    @staticmethod
    def cbreak_input_mode():
        """Set the terminal input mode to cbreak
        """
        tty.setcbreak(sys.stdin.fileno())

        pass

    @staticmethod
    def hide_cursor():
        """Hide the cursor
        """
        sys.stdout.write("\033[?25l")

        pass

    @staticmethod
    def show_cursor():
        """Show the cursor
        """
        sys.stdout.write("\033[?25h")

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
    def move_cursor(position) :
        """Move the cursor to the given position
        
        Arguments:
            position {tple(int, int)} -- Positino of the cursor
        """
        assert type(position) is list

        x, y = position
        sys.stdout.write("\033["+str(y+1)+";"+str(x+1)+"H")
        pass

    @staticmethod
    def change_color(color):
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
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, Terminal.default_settings)
        sys.stdout.write("\033[?25h")
        pass
    pass