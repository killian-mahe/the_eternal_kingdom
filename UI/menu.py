# -*- coding: utf-8 -*-
from UI import Button
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

    def add_button(self, elements):
        """Add an elements to the screen
        
        Arguments:
            elements {UI.element.Element}
        """
        elements.x += self.position[0]
        elements.y += self.position[1]
        self.elements.append(elements)
        pass

    def get_element(self, label):
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

    def select_button(self, label):
        """Select only a Button in the current menu
        
        Arguments:
            label {str} -- The label of the button to select
        """
        for element in self.elements:
            if type(element) is Button:
                if element.label == label :
                    element.select(True)
                else :
                    element.select(False)

    def show(self):
        """Display elements on the screen
        """
        if self.background :
            for background in self.background :
                background.show(self.position)
            
        for element in self.elements:
            element.show()