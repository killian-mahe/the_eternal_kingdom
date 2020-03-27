# -*- coding: utf-8 -*-

"""
The Eternal Kingdom
~~~~~~~~~~~~~~~~~~~

A Python console game

:copyright: (c) 2020 Killian Mahé
:license: MIT, see LICENSE for more details.

"""

__title__ = 'the_eternal_kingdom'
__author__ = 'Killian Mahé'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 Killian Mahé'
__version__ = '0.0.6'

# Standard Imports
import sys
import os
import time
import select
import tty
import termios
import random
import json

# Module Imports
from IO.terminal import Terminal
from IO.keyboard import Keyboard
from UI import menu, button

# Internal Imports
from background import Background
from castle import Castle
from game import Game

# Load Settings
f = open("settings.json", "r")
settings = json.load(f)
f.close()

# Global variables
timeStep = None
game = None

def init() :
    """Initialize the game configuration
    """
    global timeStep, settings, game
    
    timeStep = 0.05

    background = Background(settings['assets_folder'] + "/background_1.txt")

    castle = Castle(settings['assets_folder'] + "/castle_1.txt", settings['screen_size'])

    game = Game(background, castle)

    # Setting up home_screen menu
    home_screen = menu.Menu("home_screen", Background(settings['assets_folder'] + "/menu_1.txt"))
    home_screen.addButton(button.Button((94, 18), "start", "Lancer une partie", alignement="center"))
    home_screen.addButton(button.Button((94, 20), "exit", "Quitter", alignement="center"))
    game.addMenu(home_screen)
    

    game.setMenu("home_screen")
    game.currentMenu.selectButton("start")

    Terminal.init()

    return



def interact() :
    """Interaction with the player
    """
    global game
    if Keyboard.isEvent():

        menu = game.currentMenu
        if menu : # In a menu

            if menu.label == "home_screen" :

                if Keyboard.isPressed('z') :
                    menu.selectButton("start")
                if Keyboard.isPressed('s') :
                    menu.selectButton("exit")
        
        if Keyboard.isPressed('\033'): # ESC
            quitGame()

    return
		


def live():
    global timeStep

    return



def show() :
    """Manage the screen
    """
    global timeStep, Game
    
    game.show()
    sys.stdout.flush()
    Terminal.moveCursor((0, 0))
    return



def quitGame():
    """Manage how the game quit
    """
    
    Terminal.reset()
    sys.exit()
    return



def run():
    global timeStep

    lastTimeShow = 0

    while (True):
        interact()
        live()

        if(time.time()-lastTimeShow > timeStep):
            show()
            lastTimeShow = time.time()
        
    pass


if __name__ == "__main__":

    try :
        init()
        run()
        quitGame()
    except KeyboardInterrupt:
        quitGame()
    pass