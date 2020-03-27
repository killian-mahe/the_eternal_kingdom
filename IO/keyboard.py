# -*- coding: utf-8 -*-
import sys
import select

class Keyboard:
    """A Keyboard
    """

    lastKey = None

    def __init__(self):
        pass

    @staticmethod
    def isEvent():
        """Detect if an Event occured since the last call
        
        Returns:
            bool -- Wether there is pending Event or not
        """
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []) : 
            Keyboard.lastKey = sys.stdin.read(1)
            return True
        return False
        
    @staticmethod
    def isPressed(keyChar):
        """Return the last pressed key
        
        Arguments:
            keyChar {str} -- The key ASCII code
        
        Returns:
            bool -- Wether the key was pressed or not
        """
        assert type(keyChar) is str
        if Keyboard.lastKey == keyChar :
            return True
        return False

    pass