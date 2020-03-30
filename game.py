# -*- coding: utf-8 -*-
import sys
from characters import Castle, Background, Cannon
import screen
from UI.menu import Menu
from IO import Terminal

class Game:

    def __init__(self, settings, _background, _castle, cannon):
        assert type(settings) is dict
        assert type(_background) is Background
        assert type(_castle) is Castle
        assert type(cannon) is Cannon

        self.background = _background
        self.castle = _castle
        self.cannon = cannon
        self.menus = None
        self.balls = []

        self.settings = settings

        self.currentMenu = None

        pass

    def addMenu(self, menus):
        assert (type(menus) is list) or (type(menus) is Menu)

        if type(menus) is list :
            for menu in menus:
                self.menus[menu.label] = menu
        else :
            self.menus = {str(menus.label): menus}
        pass

    def setMenu(self, label):
        assert type(label) is str
        
        self.currentMenu = self.menus[label]
        pass

    def resetMenu(self):
        self.currentMenu = None
        pass

    def shootCannon(self):

        if len(self.balls) < 10 :
            self.balls.append(self.cannon.shoot())

        pass

    def live(self):
        screen_size = self.settings['screen_size']

        for ball in self.balls:
            ball.live()

            if ball.position[0] < 0 or ball.position[0] > (screen_size[0]-1):
                self.balls.remove(ball)
                continue
            if ball.position[1] > (screen_size[1]-1):
                self.balls.remove(ball)
                continue
        pass

    def show(self):

        if self.currentMenu != None:
            self.currentMenu.show()
        else :
            self.background.show()
            self.castle.show()
            for ball in self.balls:
                if ball.position[1] > 0:
                    ball.show()
        pass

    pass

    def quitGame(self):
        """Manage how the game quit
        """
        Terminal.reset()
        sys.exit()
        pass