# -*- coding: utf-8 -*-

# Standard imports
import time

# Package imports
from IO import Terminal, File

class Animation:

    def __init__(self, file_name, position, label, frequency=2):
        """Create an instance of Animation
        
        Arguments:
            file_name {str} -- File where animation is stored
            position {list} -- 2D position
            label {str} -- Unique label of animation
        
        Keyword Arguments:
            frequency {int} -- Frequency (frame/sec) (default: {2})
        """
        assert type(file_name) is str
        assert type(position) is list

        self.position = position
        self.label = label
        self.frames = File.read_frames(file_name)
        self.frequency = frequency # frame/sec
        self.current_time = 0
        self.current_frame = 0
        self.state = False
        
        pass

    def start(self):
        """Start or resume animation
        """
        self.state = True

        pass

    def pause(self):
        """Pause animaation
        """
        self.state = False

        pass

    def stop(self):
        """Stop and reset animation
        """
        self.state = False
        self.current_frame = 0
        self.current_time = 0
        
        pass

    def show(self):
        """Display animation on screen
        """
        if not self.state :
            return

        if time.time() - self.current_time > 1/self.frequency:
        
            if self.current_frame == len(self.frames) - 1 :
                self.stop()
                return
            else:
                self.current_frame += 1
            self.current_time = time.time()
            
        for y in range(0, len(self.frames[self.current_frame])):
            for x in range(0, len(self.frames[self.current_frame][y])):
                Terminal.write(self.frames[self.current_frame][y][x], [x, y], Terminal.GREEN)
            
        pass

    pass