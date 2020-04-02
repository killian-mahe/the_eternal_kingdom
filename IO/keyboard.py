# -*- coding: utf-8 -*-

import sys
import select

class Keyboard:
    """A Keyboard
    """

    last_key = None

    def __init__(self):
        pass

    @staticmethod
    def is_event():
        """Detect if an Event occured since the last call
        
        Returns:
            bool -- Wether there is pending Event or not
        """
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []) : 
            Keyboard.last_key = sys.stdin.read(1)
            return True
        return False
        
    @staticmethod
    def is_pressed(key_char):
        """Return the last pressed key
        
        Arguments:
            keyChar {str} -- The key ASCII code
        
        Returns:
            bool -- Wether the key was pressed or not
        """
        assert type(key_char) is str
        if Keyboard.last_key == key_char :
            return True
        return False

    pass