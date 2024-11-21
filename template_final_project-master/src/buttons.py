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
        self.rect = pygame.Rect(x, y, width, height)

    def create(self, screen):
        """Creates the button on screen

        Args:
            screen (str): Name of the pyagme screen instance
        """
        pygame.draw.rect(screen, self.color, self.rect)
        if self.display:
            font = pygame.font.Font(None, 15)
            surface = font.render(self.display, True, 'black')
            textrect = surface.get_rect(center = (self.x +self.width // 2, self.y + self.height // 2))
            screen.blit(surface, textrect)
        
        
    
    def is_clicked(self, mouse_pos):
        """Checks to see whether or not the button has been clicked

        Args:
            mouse_pos (int): postion of the mouse

        Returns:
            self.x (int): returns whether the mouse has been clicked inside of the button 
        """
        return self.rect.collidepoint(mouse_pos)




#class buttons:
#    def __init__(self, shape, x,y ,type, color,text,font_size=12, t_color=white, mediapath=None,):
#        self.shape = shape
#        self.x = x
#        self.y = y
#        self.width = 200
#        self.height = 60
#        self.type = type
#        self.color = color
#        self.text = text
#        self.font = pygame.font.Font(None,font_size)
#        self.t_color = t_color
#        self.mediapath = mediapath
#        return self.shape, self.coords, self.type,self.color,self.text,
#    def drawing(self,screen):'
#        pygame.draw.rect(screen,self.color,self.rect)
#    def clicking(self,event):
#        if event.type == pygame.MOUSEBUTTONDOWN:
#            if self.rect.collidepoint(event.pos):
#                return True
#        return False
#    def displayvid(self):
#        if self.mediapath:
#            #iouno, will look further into video displayers
#    def displayimg(self,screen):
#        if self.mediapath:
#         try:
#             image = pygame.image.load(self.mediapath)
#             
#         except pygame.error:
#    def displayinfo(self, screen,info):
#        #display a text box at the top of the screen
