# -*- coding: utf-8 -*-

# Standard imports
import sys
import random
import time

# Package imports
from UI import Menu, Animation, Image
from IO import Terminal

# Internal imports
from characters import Castle, Background, Cannon, Zombie
from player import Player

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
        self.state = False # Pause

        self.levels = settings['levels']
        self.current_level = 0

        self.last_time_spawn_monster = 0
        self.spawner_frequency = self.get_current_level()['spawner_frequency'] # Monster/sec

        self.game_status_window = Image(settings["assets_folder"]+"/game_status.txt")

        self.player = Player()

        self.settings = settings

        self.max_balls = 10

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
        
        self.state = False
        self.current_menu = self.menus[label]

        pass

    def reset_menu(self):
        """Reset the menu to None
        """

        self.state = True
        self.current_menu = None
        
        pass

    def shoot_cannon(self):
        """Let the cannon shoot balls
        """

        if len(self.balls) < self.max_balls :
            self.balls.append(self.cannon.shoot())

        pass

    def get_current_level(self):
        """Get the current level
        
        Returns:
            dict -- Current level settings
        """
        return self.levels[self.current_level]

    def level_up(self):
        """Level up
        """

        if self.current_level +1 == len(self.levels):
            self.set_menu("win_menu")
        else:
            self.current_level += 1
            self.spawner_frequency = self.get_current_level()['spawner_frequency']
            level_up_animation = Animation(self.settings['assets_folder']+"/level_up.txt", [83, 19], "level_up", frequency=6,color=Terminal.YELLOW)
            level_up_animation.start()
            self.add_animation(level_up_animation)
        pass

    def loose(self):
        """Loose the game
        """
        self.state = False
        loose_animation = Animation(self.settings['assets_folder'] + "/loose.txt", [83, 19], "loose", frequency=6, color=Terminal.RED)
        loose_animation.start()
        self.add_animation(loose_animation)

        pass

    def live(self):
        """Make elements live
        """

        if not self.state:
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

        if self.castle.life <= 0:
            self.loose()

        # Spawn Zombie
        if time.time() - self.last_time_spawn_monster > 1/self.spawner_frequency :
            zombie = Zombie(self.settings['assets_folder']+"/monster_1.txt", 
                            [screen_size[0]-3, screen_size[1] - random.randint(1, 6)],
                            random.randint(self.get_current_level()["min_monster_level"], self.get_current_level()["max_monster_level"]),
                            speed=self.get_current_level()["monster_speed"])
            self.monsters.append(zombie)
            self.last_time_spawn_monster = time.time()

        # Live Monsters
        for monster in self.monsters:
            monster.live()
            for ball in self.balls :
                if monster.is_in_collision(ball.position):
                    if monster.get_damages(ball.power):
                        death_animation = Animation(self.settings['assets_folder']+"/death_animation.txt", monster.position, "death_animation", frequency=6, color=Terminal.RED)
                        death_animation.start()
                        self.add_animation(death_animation)
                        self.player.add_score(monster.score)
                        self.monsters.remove(monster)
                    self.balls.remove(ball)

            if self.castle.is_in_collision(monster.position):
                if self.castle.get_damages(monster.life):
                    pass
                self.monsters.remove(monster)

        # Live Player
        if self.player.score >= self.get_current_level()["score"]:
            self.level_up()
            pass

        # Animation garbage
        for animation in self.animations:
            if animation.is_finished():
                self.animations.remove(animation)
                pass
        
        pass

    def show(self):
        """Display on the scrren
        """

        if self.current_menu != None:
            self.current_menu.show()
            return       

        if self.state :
            self.background.show()
            self.castle.show()

            # Display balls
            for ball in self.balls:
                if ball.position[1] > 0:
                    ball.show()

            # Display monsters
            for monster in self.monsters:
                monster.show()

            # Display ball path simulation
            self.cannon.show([list(range(self.cannon.position[0], self.settings['screen_size'][0])),
                              list(range(0, self.settings['screen_size'][1]))])
        
            
            # Display Game informations
            self.game_status_window.show()
            Terminal.write(str(self.current_level +1 ), [25, 3], Terminal.YELLOW)
            Terminal.write(str(self.player.score), [35 - int(len(str(self.player.score))/2), 3], Terminal.YELLOW)
            Terminal.write("■"*(self.max_balls-len(self.balls)), [5, 2], Terminal.GREEN)
            Terminal.write("■"*int(self.castle.life/10), [5, 4], Terminal.RED)

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