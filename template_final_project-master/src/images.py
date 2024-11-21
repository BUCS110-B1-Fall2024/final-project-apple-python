import pygame

class Images:
    def __init__(self, screen, pic_path):
        """Allows an image from a file to be put onto the screen

        Args:
            screen (str): Where in pyagme the pic will be put
            pic_path (str): File pathway to the picture being blit onto the screen
        """
        self.screen = screen
        self.pic_path = pic_path
    
    def load(self, pic_path):
        """Using the picture pathway it loads the image

        Args:
            pic_path (str): The file pathway
        """
        self.pic = pygame.image.load(pic_path)
    
    def blit(self):
        self.screen.blit(self.pic, (0,0))
        pygame.display.flip()
        