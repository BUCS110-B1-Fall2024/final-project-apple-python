import pygame

class Images:
    def __init__(self, pic_path, x = 0, y = 0):
        """Allows an image to be put onto the screen, transforms image to our screen size

        Args:
            pic_path (str): File pathway of the image
            x (int): x-coor. for the picture
            y (int): y-coor. for the picture
        """
        self.pic = pygame.image.load(pic_path)
        self.pic = pygame.transform.scale(self.pic, (800, 800))
        self.coor = x, y
        
    def blit(self, screen):
        """Allows the image to be put onto the pyagme screen

        Args:
            screen (str): the instance name for the pyagme window
        """
        screen.blit(self.pic, (self.coor))
        