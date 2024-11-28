import pygame

class buttonimages():
    def __init__(self,x,y,w,h,color,text,font):
         self.rect = pygame.Rect(x,y,w,h) #makes a button at these coordinates with these dimensions
         self.color = color  #colors of button
         self.text = text #button text
         self.font = font #button font
         self.text_surf=self.font.render(self.text, True, (0,0,0)) #text inside the button
         self.text_rect=self.text_surf.get_rect(center=self.rect.center) #centers itself in the button
    def display_button(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def clicked(self, position):
        return self.rect.collidepoint(position)
    class displayimage():
        def __init__(self,screen):
            self.screen = screen
        def show_image(self, image_path, x, y):
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (800, 600))  # Resize if necessary
            self.screen.blit(image, (0, 0))
    
class buttonvideos():
    def __init__(self,x,y,w,h,color,text,font):
         self.rect = pygame.Rect(x,y,w,h) #makes a button at these coordinates with these dimensions
         self.color = color  #colors of button
         self.text = text #button text
         self.font = font #button font
         self.text_surf=self.font.render(self.text, True, (0,0,0)) #text inside the button
         self.text_rect=self.text_surf.get_rect(center=self.rect.center) #centers itself in the button
    def display_button(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def clicked(self, position):
        return self.rect.collidepoint(position)
    class displayvideo():
        #placeholder
        pass

class buttontextbox():
    def __init__(self,x,y,w,h,color,text,font):
         self.rect = pygame.Rect(x,y,w,h) #makes a button at these coordinates with these dimensions
         self.color = color  #colors of button
         self.text = text #button text
         self.font = font #button font
         self.text_surf=self.font.render(self.text, True, (0,0,0)) #text inside the button
         self.text_rect=self.text_surf.get_rect(center=self.rect.center) #centers itself in the button
    def display_button(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def clicked(self, position):
        return self.rect.collidepoint(position)
    class textboxdisplay():
        def __init__(self, x,y,w,h,text_size,text_color,back_color=None ):
            self.x=x
            self.y=y #coordinates of the text
            self.width=w 
            self.height=h #dimensions of the text box (both coordinates and dimensions should be same to make life simpler)
            self.font=pygame.font.Font(None,text_size) #how big the text is
            self.text_color=text_color #color of the text (should be white or black imo)
            self.back_color=back_color #background color of the textbox
            self.text=""#must be initially empty
        def text(self,text):
            self.text=text
            self.text_surf= self.font.render(self.text,True,self.text_color)
        def display(self,screen):
            if self.back_color:
                pygame.draw.rect(screen,self.back_color,self.x,self.y,self.width,self.height)
            screen.blit(self.text_surf,(self.x+5,self.y+5))
