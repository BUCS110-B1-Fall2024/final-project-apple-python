import pygame

class Buttons:
    def __init__(self, x, y, width, height, color = '', display = ''):
        """Allows for the creation of buttons

        Args:
            x (int): x-coor. for the button
            y (int): y-coor. for the button
            width (int): Width of the button
            height (int): Height of the button
            color (str, optional): The color of the button. Defaults to nothing.
            display (str, optional): The message displayed onto the buttons surface. Defaults to nothing.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.display = display

    def create(self, screen):
        """Creates the button on screen

        Args:
            screen (str): Name of the pyagme screen instance
        """
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def is_clicked(self, mouse_pos):
        """Checks to see whether or not the button has been clicked

        Args:
            mouse_pos (int): postion of the mouse

        Returns:
            self.x (int): returns whether the mouse has been clicked inside of the button 
        """
        return self.rect.collidepoint(mouse_pos)