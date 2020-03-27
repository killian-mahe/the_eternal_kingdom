# -*- coding: utf-8 -*-

class Screen:

    def __init__(self, screens=[], window_size=[500, 500]):
        assert type(screens) is list
        self.screens = screens
        self.windowSize = window_size
        pass

    def display(self):

        # Initial screen size
        displaied_screen = list()
        for i in range(0, self.windowSize[1]):
            displaied_screen.append([" "] * self.windowSize[0])
        
        for screen in self.screens:
            [bg, (x0, y0)] = screen.getArray()
            
        pass
    pass