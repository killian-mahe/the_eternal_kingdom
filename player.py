# -*- coding: utf-8 -*-

class Player:

    def __init__(self):

        self.score = 0
        self.name = ""
        pass

    def add_score(self, score):
        assert type(score) is int
        self.score += score
        pass

    pass