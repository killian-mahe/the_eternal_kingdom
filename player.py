# -*- coding: utf-8 -*-

class Player:
    """A Player
    """

    def __init__(self):
        """Create an instance of Player
        """

        self.score = 0
        self.name = ""

        pass

    def add_score(self, score):
        """Add score to the player
        
        Arguments:
            score {int} -- score to add
        """
        assert type(score) is int

        self.score += score

        pass

    pass