# -*- coding: utf-8 -*-
from UI import Button
from IO import Keyboard
from characters import Background
import copy
import sys

class Menu:
    """A user interface
    """

    def __init__(self, label="", background = [], position=[0, 0]):
        """Create an instance of Menu
        
        Keyword Arguments:
            background {background.Background} -- The background (default: {[]})
            label {str} -- A unique label (default: {""})
            position {list} -- left-up menu position (default: {[0, 0]})
        """
        self.elements = []
        self.label = label
        self.background = background
        self.position = position
        pass

    def addButton(self, _elements):
        """Add an elements to the screen
        
        Arguments:
            _elements {UI.element.Element}
        """
        _elements.x += self.position[0]
        _elements.y += self.position[1]
        self.elements.append(_elements)
        pass

    def getElement(self, label):
        """Get an element in the menu
        
        Arguments:
            label {str} -- The label of the searched element

        Returns:
            element.Element -- The element searched or None
        """
        for _element in self.elements:
            if _element.label == label:
                return _element
        return None

    def selectButton(self, label):
        """Select only a Button in the current menu
        
        Arguments:
            label {str} -- The label of the button to select
        """
        for _element in self.elements:
            if type(_element) is Button:
                if _element.label == label :
                    _element.select(True)
                else :
                    _element.select(False)

    def show(self):
        """Display elements on the screen
        """
        if self.background :
            for background in self.background :
                background.show(self.position)
            
        for _element in self.elements:
            _element.show()