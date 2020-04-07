# -*- coding: utf-8 -*-

from IO import File, Terminal

class Image:
    """An Image represent a background to display on the screen
    """

    def __init__(self, file_name, position=[0,0], color=Terminal.WHITE):
        """Create an instance of Image
        
        Arguments:
            file_name {str} -- Image file path
        
        Keyword Arguments:
            position {list} -- 2D position (default: {[0,0]})
            color {int} -- Terminal color (default: {Terminal.WHITE})
        """
        assert type(file_name) is str
        assert type(position) is list
        assert type(color) is int

        self.position = position
        self.content = File.read_as_array(file_name)
        self.color = color
        
        pass

    def show(self):
        """Display image on screen
        """
        for y in range(0, len(self.content)):
            for x in range(0, len(self.content[y])):
                Terminal.write(self.content[y][x], [self.position[0] + x, self.position[1] + y], self.color)
        
        pass

    pass