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
__version__ = '0.0.7'

# Standard Imports
import sys
import os
import time
import select
import tty
import termios
import random
import json

# Package Imports
from IO import Terminal, Keyboard
from UI import Menu, Button

# Internal Imports
from characters import Background, Castle, Cannon, Ball
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

    Terminal.init()

    background = Background(settings['assets_folder'] + "/background_1.txt")

    castle = Castle(settings['assets_folder'] + "/castle_1.txt", settings['screen_size'])

    cannon = Cannon([21, 28])

    game = Game(settings, background, castle, cannon)

    # Setting up home_screen menu
    home_screen = Menu("home_screen", [Background(settings['assets_folder'] + "/menu_1.txt"), castle])
    home_screen.addButton(Button([94, 18], "start", "Lancer une partie", alignement="center"))
    home_screen.addButton(Button([94, 20], "exit", "Quitter", alignement="center"))
    
    # Setting up pause_menu
    pause_menu = Menu("pause_menu", [Background(settings['assets_folder'] + "/pause_menu.txt")], position=[83, 19])
    pause_menu.addButton(Button([14, 2], "continu", "Continuer", alignement="center"))
    pause_menu.addButton(Button([15, 5], "quit", "Quitter", alignement="center"))

    game.addMenu([home_screen, pause_menu])

    game.setMenu("home_screen")
    game.currentMenu.selectButton("start")


    sys.stdout.flush()
    return



def interact() :
    """Interaction with the player
    """
    global game
    if Keyboard.isEvent():

        menu = game.currentMenu
        if menu : # In a menu
            if menu.label == "home_screen":
                if Keyboard.isPressed('z') :
                    menu.selectButton("start")
                if Keyboard.isPressed('s') :
                    menu.selectButton("exit")
                if Keyboard.isPressed('\n'):
                    if menu.getElement("start").selected :
                        game.resetMenu()
                    elif menu.getElement("exit").selected :
                        game.quitGame()

            if menu.label == "pause_menu":
                if Keyboard.isPressed('z') :
                    menu.selectButton("continu")
                if Keyboard.isPressed('s') :
                    menu.selectButton("quit")
                if Keyboard.isPressed('\n'):
                    if menu.getElement("continu").selected :
                        game.resetMenu()
                    elif menu.getElement("quit").selected :
                        game.quitGame()
        
        else :
            if Keyboard.isPressed('\n'):
                game.shootCannon()

            if Keyboard.isPressed('z'):
                game.cannon.angle = min(game.cannon.angle + 5, 90)

            if Keyboard.isPressed('s'):
                game.cannon.angle = max(game.cannon.angle - 5, 0)

            if Keyboard.isPressed('q'):
                game.cannon.force = max(game.cannon.force - 5, 5)

            if Keyboard.isPressed('d'):
                game.cannon.force = min(game.cannon.force + 5, 50)
        
            if Keyboard.isPressed('\033'): # ESC
                game.setMenu("pause_menu")
                game.currentMenu.selectButton("continu")

    return
		


def live():
    """Live loop
    """
    global timeStep, game

    game.live()

    return

def quitGame():
    """Manage how the game end
    """
    global game
    game.quitGame()
    pass


def show() :
    """Manage the screen
    """
    global timeStep, game

    game.show()
    
    sys.stdout.flush()
    Terminal.moveCursor([0, 0])
    return



def run():
    """Simulation loop
    """
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