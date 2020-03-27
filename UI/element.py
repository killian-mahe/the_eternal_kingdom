# -*- coding: utf-8 -*-

class Element:
    """An Element is an object that can be integrated in a user interface
    
    Raises:
        NotImplementedError: Abstract method
    """

    def __init__(self, position, label):
        """Create an instance of Element
        
        Arguments:
            position {tuple(int, int)} -- The position of the Element in the interface
            label {str} -- Unique label of Element
        """
        assert type(position) is tuple
        assert type(label) is str

        self.x, self.y = position
        self.label = label
        pass

    def show(self):
        """Display the Element on the screen
        
        Raises:
            NotImplementedError: Method must be implemented
        """
        raise NotImplementedError