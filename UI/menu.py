# -*- coding: utf-8 -*-
from UI import element
from UI import button
import background
import sys

class Menu:
    """A user interface
    """

    def __init__(self, label="", background = None, _elements = []):
        """Create an instance of Menu
        
        Keyword Arguments:
            background {background.Background} -- The background
            label {str} -- A unique label (default: {""})
            _elements {list} -- List of elements (default: {[]})
        """
        self.elements = _elements
        self.label = label
        self.background = background
        pass

    def addButton(self, _elements):
        """Add an elements to the screen
        
        Arguments:
            _elements {UI.element.Element}
        """
        
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
            self.background.show()
            
        for element in self.elements:
            element.show()