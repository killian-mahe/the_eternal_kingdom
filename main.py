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
__version__ = '0.0.1'

# Standard import
import sys
import os
import time
import select
import tty
import termios
import random

# Package import
from Utils import json

# Module import


settings = json.Json("settings.json")
settings.load()

#Données globales
timeStep = None

#interaction clavier
old_settings = termios.tcgetattr(sys.stdin)

def init() :
	global timeStep

	#Initialistion du temps de jeu
	timeStep = 0.02

	# interaction clavier
	tty.setcbreak(sys.stdin.fileno())

	#Effacer la console
	sys.stdout.write("\033[2J")
	sys.stdout.write("\033[?25l")
	sys.stdout.write("\033[40m\033[1;34m")
	return



def interact() :
	global old_settings
	
	#gestion des evenement clavier
	if isData():
		c = sys.stdin.read(1)

	return
		


def live():
	global timeStep
    
	return



def isData():
	#recuperation evenement clavier

	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])



def show() :
	global timeStep
	#Affichage des différents élément

	sys.stdout.flush()
	return



def quitGame():
	#restoration parametres terminal
	global old_settings
	#couleur white
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
	sys.exit()
	return



def run():
	global timeStep
	#Boucle de simulation
	while 1:
		interact()
		live()
		show()
		time.sleep(timeStep)
	return



init()
run()
quitGame()