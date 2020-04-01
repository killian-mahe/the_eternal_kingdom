# -*- coding: utf-8 -*-
from UI import element
from UI import button
from IO import Keyboard
from characters import Background
import sys

class Menu:
    """A user interface
    """

    def __init__(self, label="", background = [], _elements = [], position=[0, 0]):
        """Create an instance of Menu
        
        Keyword Arguments:
            background {background.Background} -- The background (default: {[]})
            label {str} -- A unique label (default: {""})
            _elements {list} -- List of elements (default: {[]})
            position {list} -- left-up menu position (default: {[0, 0]})
        """
        self.elements = _elements
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
        for element in self.elements:
            if element.label == label:
                return element
        return None

    def selectButton(self, label):
        """Select only a Button in the current menu
        
        Arguments:
            label {str} -- The label of the button to select
        """
        for element in self.elements:
            if type(element) is button.Button:
                if element.label == label :
                    element.select(True)
                else :
                    element.select(False)

    def show(self):
        """Display elements on the screen
        """
        if self.background :
            for background in self.background :
                background.show()
            
        for element in self.elements:
            element.show()