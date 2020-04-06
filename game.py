# -*- coding: utf-8 -*-

# Standard imports
import sys
import random
import time

# Package imports
from UI import Menu, Animation
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
        self.animations = []
        self.monsters = []
        self.balls = []

        self.last_time_spawn_monster = 0
        self.spawner_frequency = 0.5 # Monster/sec

        self.settings = settings

        self.current_menu = None

        pass

    def add_menu(self, menus):
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

    def add_animation(self, animation):
        """Add animations to the game
        
        Arguments:
            animation {Animation}
        """
        assert type(animation) is Animation
        self.animations.append(animation)

        pass

    def set_menu(self, label):
        """Change the menu to current labelled menu
        
        Arguments:
            label {str} -- Label of the menu
        """
        assert type(label) is str
        
        self.current_menu = self.menus[label]

        pass

    def reset_menu(self):
        """Reset the menu to None
        """

        self.current_menu = None
        
        pass

    def shoot_cannon(self):
        """Let the cannon shoot balls
        """

        if len(self.balls) < 10 :
            self.balls.append(self.cannon.shoot())

        pass

    def live(self):
        """Make elements live
        """

        if self.current_menu != None:
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
        if time.time() - self.last_time_spawn_monster > 1/self.spawner_frequency :
            zombie = Zombie(self.settings['assets_folder']+"/monster_1.txt", 
                            [screen_size[0]-3, screen_size[1] - random.randint(1, 6)], random.randint(1, 3))
            self.monsters.append(zombie)
            self.last_time_spawn_monster = time.time()

        # Live Monsters
        for monster in self.monsters:
            monster.live()
            for ball in self.balls :
                if monster.is_in_collision(ball.position):
                    if monster.get_damages(ball.power):
                        death_animation = Animation(self.settings['assets_folder']+"/death_animation.txt", monster.position, "death_animation", 6)
                        death_animation.start()
                        self.add_animation(death_animation)
                        self.monsters.remove(monster)
                    self.balls.remove(ball)
        
        pass

    def show(self):
        """Display on the scrren
        """

        if self.current_menu != None:
            self.current_menu.show()
        else :
            self.background.show()
            self.castle.show()
            for ball in self.balls:
                if ball.position[1] > 0:
                    ball.show()

            for monster in self.monsters:
                monster.show()
            
            for animation in self.animations:
                animation.show()

        pass

    def quit_game(self):
        """Manage how the game quit
        """

        Terminal.reset()
        sys.exit()
        
        pass

    pass