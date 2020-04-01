# -*- coding: utf-8 -*-

# Standard imports
import sys
import random
import time

# Package imports
from UI import Menu
from IO import Terminal

# Internal imports
from characters import Castle, Background, Cannon, Zombie

class Game:

    def __init__(self, settings, _background, _castle, cannon):
        """Create a Game instance
        
        Arguments:
            settings {list} -- List of settings
            _background {Background} -- Background to display during the game
            _castle {Castle} -- Castle to display during the game
            cannon {Cannon} -- Cannon to display during the game
        """
        assert type(settings) is dict
        assert type(_background) is Background
        assert type(_castle) is Castle
        assert type(cannon) is Cannon

        self.background = _background
        self.castle = _castle
        self.cannon = cannon
        self.menus = {}
        self.monsters = []
        self.balls = []

        self.lastTimeSpawnMonster = 0
        self.spawnerFrequency = 0.5 # Monster/sec

        self.settings = settings

        self.currentMenu = None

        pass

    def addMenu(self, menus):
        """Add a menu to the list
        
        Arguments:
            menus {Menu} -- Menu to add
        """
        assert (type(menus) is list) or (type(menus) is Menu)

        if type(menus) is list :
            for menu in menus:
                self.menus[menu.label] = menu
        else :
            self.menus[menus.label] = menus

        pass

    def setMenu(self, label):
        """Change the menu to current labelled menu
        
        Arguments:
            label {str} -- Label of the menu
        """
        assert type(label) is str
        
        self.currentMenu = self.menus[label]

        pass

    def resetMenu(self):
        """Reset the menu to None
        """

        self.currentMenu = None
        
        pass

    def shootCannon(self):
        """Let the cannon shoot balls
        """

        if len(self.balls) < 10 :
            self.balls.append(self.cannon.shoot())

        pass

    def live(self):
        """Make elements live
        """

        if self.currentMenu != None:
            return

        screen_size = self.settings['screen_size']

        # Live Balls
        for ball in self.balls:
            ball.live()

            if ball.position[0] < 0 or ball.position[0] > (screen_size[0]-1):
                self.balls.remove(ball)
                continue
            if ball.position[1] > (screen_size[1]-1):
                self.balls.remove(ball)
                continue

        # Spawn Zombie
        if time.time() - self.lastTimeSpawnMonster > 1/self.spawnerFrequency :
            zombie = Zombie(self.settings['assets_folder']+"/monster_1.txt", 
                            [screen_size[0]-3, screen_size[1] - random.randint(1, 6)], random.randint(1, 3))
            self.monsters.append(zombie)
            self.lastTimeSpawnMonster = time.time()

        # Live Monsters
        for monster in self.monsters:
            monster.live()
            for ball in self.balls :
                if monster.isInCollision(ball.position):
                    if monster.getDamages(ball.power):
                        self.monsters.remove(monster)
                    self.balls.remove(ball)
        
        pass

    def show(self):
        """Display on the scrren
        """

        if self.currentMenu != None:
            self.currentMenu.show()
        else :
            self.background.show()
            self.castle.show()
            for ball in self.balls:
                if ball.position[1] > 0:
                    ball.show()

            for monster in self.monsters:
                monster.show()

        pass

    def quitGame(self):
        """Manage how the game quit
        """

        Terminal.reset()
        sys.exit()
        
        pass

    pass