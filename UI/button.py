# -*- coding: utf-8 -*-
import sys
from UI.element import Element

class Button(Element):
    """A usable Button for user interface
    
    Arguments:
        Element {UI.element.Element} -- An Element
    """

    def __init__(self, position, label, action=None):
        """Create an instance of Button
        
        Arguments:
            position {tuple(int, int)} -- Position of the button on the screen
            label {str} -- Unique label of the button
        
        Keyword Arguments:
            action {func} -- Function called when button is selectionned (default: {None})
        """
        super().__init__(position, label)
                
        self.selected = False

        if action:
            self.action = action
        
        pass

    def select(self, selected):
        """Select the button
        
        Arguments:
            selected {bool} -- Wether the button should be selected or not
        """
        assert type(selected) is bool
        self.selected = selected
        pass

    def show(self):
        """Display the button on the screen
        """

        s="\033["+str(self.y+1)+";"+str(self.x+1)+"H"
        sys.stdout.write(s)

        if self.selected :
            sys.stdout.write("\033["+str(33)+"m") # Change color to yellow
            
        else :
            sys.stdout.write("\033["+str(37)+"m") # Reset color to white

        sys.stdout.write(str(self.label))

    pass