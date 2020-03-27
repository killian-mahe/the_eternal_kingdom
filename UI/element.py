# -*- coding: utf-8 -*-

class Element:

    def __init__(self, position, label):
        assert type(position) is tuple
        assert type(label) is str
        
        self.x, self.y = position
        self.label = label
        pass

    def show(self):
        raise NotImplementedError