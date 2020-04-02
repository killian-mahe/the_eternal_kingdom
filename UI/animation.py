# -*- coding: utf-8 -*-

# Package imports
from IO import Terminal, File

class Animation:

    def __init__(self, file_name, position):
        assert type(file_name) is str
        assert type(position) is list

        self.position = position
        self.frames = File.read_frames(file_name)
        
        pass