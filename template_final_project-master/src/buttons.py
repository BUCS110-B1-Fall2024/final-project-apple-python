import pygame

class Buttons():  
    def __init__(self, x, y, w, h, color='', text ='', size = 15):
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
         self.width = w
         self.y = y
         self.height = h
         self.rect = pygame.Rect(x,y,w,h) #makes a button at these coordinates with these dimensions
         self.color = color  #colors of button
         self.text = text #button text
         self.font_size = size

    def create(self, screen):
        """Creates the button on screen
        Args:
            screen (str): Name of the pyagme screen instance
        """
        pygame.draw.rect(screen, self.color, self.rect) #Creates the button using this method
        
        if self.text: #if there is text for the button this is called
            font = pygame.font.Font(None, self.font_size) #sets the font
            surface = font.render(self.text, True, 'black') #Sets surface and color
            textrect = surface.get_rect(center = (self.x +self.width // 2, self.y + self.height // 2)) #Puts text in center
            screen.blit(surface, textrect) #Puts it onto screen

    def is_clicked(self, mouse_pos):
        """Checks to see whether or not the button has been clicked

        Args:
            mouse_pos (int): position of the mouse

        Returns:
            self.rect.collidepoint (int): returns whether the mouse has been clicked inside the button
        """
        return self.rect.collidepoint(mouse_pos)