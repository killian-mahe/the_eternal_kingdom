# -*- coding: utf-8 -*-
from UI import element
import sys

class Menu:
    """A user interface
    """

    def __init__(self, label="", _elements = []):
        """Create an instance of Menu
        
        Keyword Arguments:
            label {str} -- A unique label (default: {""})
            _elements {list} -- List of elements (default: {[]})
        """
        self.elements = _elements
        self.label = label
        pass

    def addButton(self, _elements):
        """Add an elements to the screen
        
        Arguments:
            _elements {UI.element.Element}
        """
        
        self.elements.append(_elements)
        pass

    def getElement(self, label):
        for element in self.elements:
            if element.label == label:
                return element
        return None

    def show(self):
        """Display elements on the screen
        """
        for element in self.elements:
            element.show()