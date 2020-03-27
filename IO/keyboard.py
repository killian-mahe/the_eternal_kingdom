# -*- coding: utf-8 -*-
import sys
import select

class Keyboard:

    lastKey = None

    def __init__(self):
        pass

    @staticmethod
    def isEvent():
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []) : 
            Keyboard.lastKey = sys.stdin.read(1)
            return True
        return False
        
    @staticmethod
    def isPressed(keyChar):
        assert type(keyChar) is str
        if Keyboard.lastKey == keyChar :
            return True
        return False