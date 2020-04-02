# -*- coding: utf-8 -*-
import sys
from UI.element import Element
from IO import Terminal

class Button(Element):
    """A usable Button for user interface
    
    Arguments:
        Element {UI.element.Element} -- An Element
    """

    def __init__(self, position, label, name="", alignement="left"):
        """Create an instance of Button
        
        Arguments:
            position {tuple(int, int)} -- Position of the button on the screen
            label {str} -- Unique label of the button
        
        Keyword Arguments:
            name {str} -- A string that will be displayed
            alignement {str} -- (Left|Center|Right) Alignement of the button compared to the position (default: {Left})
        """
        super(Button, self).__init__(position, label)
                
        self.selected = False
        self.name = name
        self.alignement = alignement
        
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
        if self.alignement == "right":
            Terminal.move_cursor([self.x + 1 - len(self.name), self.y + 1])
        
        elif self.alignement == "center":
            Terminal.move_cursor([self.x - round((len(self.name)/2)), self.y + 1])
            
        else : 
            Terminal.move_cursor([self.x , self.y + 1])

        if self.selected :
            Terminal.change_color(Terminal.YELLOW)
            
        else :
            Terminal.change_color(Terminal.WHITE)

        Terminal.write(str(self.name))

    pass