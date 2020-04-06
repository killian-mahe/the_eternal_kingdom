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
time_step = None
game = None

def init() :
    """Initialize the game configuration
    """
    global time_step, settings, game
    
    time_step = 0.05

    Terminal.init()

    background = Background(settings['assets_folder'] + "/background_1.txt")

    castle = Castle(settings['assets_folder'] + "/castle_1.txt", settings['screen_size'])

    cannon = Cannon([21, 28])

    game = Game(settings, background, castle, cannon)

    # Setting up home_screen menu
    home_screen = Menu("home_screen", [Background(settings['assets_folder'] + "/menu_1.txt"), castle])
    home_screen.add_button(Button([94, 18], "start", "Lancer une partie", alignement="center"))
    home_screen.add_button(Button([94, 20], "exit", "Quitter", alignement="center"))
    
    # Setting up pause_menu
    pause_menu = Menu("pause_menu", [Background(settings['assets_folder'] + "/pause_menu.txt")], position=[83, 19])
    pause_menu.add_button(Button([14, 2], "continu", "Continuer", alignement="center"))
    pause_menu.add_button(Button([15, 5], "quit", "Quitter", alignement="center"))

    # Setting up win_menu
    win_menu = Menu("win_menu", [Background(settings['assets_folder'] + "/win_menu.txt")])

    game.add_menu([home_screen, pause_menu, win_menu])

    game.set_menu("home_screen")
    game.current_menu.select_button("start")


    sys.stdout.flush()
    return



def interact() :
    """Interaction with the player
    """
    global game
    if Keyboard.is_event():

        menu = game.current_menu
        if menu : # In a menu
            if menu.label == "home_screen":
                if Keyboard.is_pressed('z') :
                    menu.select_button("start")
                if Keyboard.is_pressed('s') :
                    menu.select_button("exit")
                if Keyboard.is_pressed('\n'):
                    if menu.get_element("start").selected :
                        game.reset_menu()
                    elif menu.get_element("exit").selected :
                        game.quit_game()

            if menu.label == "pause_menu":
                if Keyboard.is_pressed('z') :
                    menu.select_button("continu")
                if Keyboard.is_pressed('s') :
                    menu.select_button("quit")
                if Keyboard.is_pressed('\n'):
                    if menu.get_element("continu").selected :
                        game.reset_menu()
                    elif menu.get_element("quit").selected :
                        game.quit_game()
        
        else :            
            if Keyboard.is_pressed('\n'):
                game.shoot_cannon()

            if Keyboard.is_pressed('z'):
                game.cannon.angle = min(game.cannon.angle + 5, 90)

            if Keyboard.is_pressed('s'):
                game.cannon.angle = max(game.cannon.angle - 5, 0)

            if Keyboard.is_pressed('q'):
                game.cannon.force = max(game.cannon.force - 5, 5)

            if Keyboard.is_pressed('d'):
                game.cannon.force = min(game.cannon.force + 5, 50)
        
            if Keyboard.is_pressed('\033'): # ESC
                game.set_menu("pause_menu")
                game.current_menu.select_button("continu")

    return
		


def live():
    """Live loop
    """
    global time_step, game

    game.live()

    return

def quit_game():
    """Manage how the game end
    """
    global game
    game.quit_game()
    pass


def show() :
    """Manage the screen
    """
    global game

    game.show()
    sys.stdout.flush()
    Terminal.move_cursor([0, 0])
    return



def run():
    """Simulation loop
    """
    global time_step

    last_time_show = 0

    while (True):
        interact()
        live()

        if(time.time()-last_time_show > time_step):
            show()
            last_time_show = time.time()
        
    pass


if __name__ == "__main__":

    try :
        init()
        run()
        quit_game()
    except KeyboardInterrupt:
        quit_game()
    pass