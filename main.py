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
__version__ = '0.0.5'

# Standard import
import sys
import os
import time
import select
import tty
import termios
import random
import json

# Package import

# Module import
from castle import Castle
from background import Background
from UI import menu, button
from game import Game
from IO.terminal import Terminal
from IO.keyboard import Keyboard

# Load settings
f = open("settings.json", "r")
settings = json.load(f)
f.close()


# Global variables
timeStep = None
game = None

def init() :
    global timeStep, settings, game
    
    timeStep = 0.05

    # Init backgrounds
    background = Background(settings['assets_folder'] + "/background_1.txt")

    # Init castles
    castle = Castle(settings['assets_folder'] + "/castle_1.txt", settings['screen_size'])

    game = Game(background, castle)

    default_menu = menu.Menu(label="default_menu")
    default_menu.addButton(button.Button((10, 10), "Start_game"))
    game.addMenu(default_menu)

    game.setMenu("default_menu")
    Terminal.init()

    return



def interact() :
    global game

    #gestion des evenement clavier
    if Keyboard.isEvent():
        
        menu = game.currentMenu
        if menu :
            if menu.label == "default_menu":

                if Keyboard.isPressed('s'):
                    menu.getElement("Start_game").select(True)

                if Keyboard.isPressed('z'):
                    menu.getElement("Start_game").select(False)

                if Keyboard.isPressed('p'):
                    game.resetMenu()

        if Keyboard.isPressed('\033'):
            quitGame()

    return
		


def live():
    global timeStep

    return



def show() :
    global timeStep, game
    #Affichage des différents élément
    
    # Show the background
    game.show()
    sys.stdout.flush()
    Terminal.moveCursor((0, 0))
    return



def quitGame():
    #restoration parametres terminal
    Terminal.reset()
    sys.exit()
    return



def run():
    global timeStep
    #Boucle de simulation
    
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