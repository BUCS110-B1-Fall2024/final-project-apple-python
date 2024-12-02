import pygame

class Buttons():   #https://docs.python.org/3/tutorial/classes.html < how to set them up 
    ## if you change the class name then you need to change it in the controller too
    def __init__(self, x, y, w, h, color='', text =''):
         """Allows for the creation of buttons
        Args:
            x (int): x-coor. for the button
            y (int): y-coor. for the button
            width (int): Width of the button
            height (int): Height of the button
            color (str, optional): The color of the button. Defaults to nothing.
            display (str, optional): The message displayed onto the buttons surface. Defaults to nothing.
        """
         self.rect = pygame.Rect(x,y,w,h) #makes a button at these coordinates with these dimensions
         self.color = color  #colors of button
         self.text = text #button text

    def display_button(self, screen):
        """Creates the button on screen
        Args:
            screen (str): Name of the pyagme screen instance
        """
        pygame.draw.rect(screen, self.color, self.rect) #Creates the button using this method
        
        if self.text: #if there is text for the button this is called
            font = pygame.font.Font(None, 15) #sets the font
            surface = font.render(self.display, True, 'black') #Sets surface and color
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
    
    
    class displayimage(): #This can be done using the images class and just putting in the controller "if x button is clicked display x image"
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
            self.text=""#must be initially empty(?)
        def text(self,text):
            self.text=text
            self.text_surf= self.font.render(self.text,True,self.text_color)


        def display(self,screen):
            if self.back_color:
                pygame.draw.rect(screen,self.back_color,self.x,self.y,self.width,self.height)
            screen.blit(self.text_surf,(self.x+5,self.y+5))

class quitbeginbutton(): #just a simple button, because its simple we can hardcode its trait to quit the game or go back to the start outside of the function (I believe)
        def __init__(self,x,y,w,h,color,text,font):
            self.rect=pygame.Rect(x,y,w,h)
            self.color= color
            self.text = text
            self.font = font
            self.text_surf=self.font.render(self.text,True,(0,0,0))
            self.text_rect=self.text_surf.get_rect(center =self.rect.center)
        def display(self,screen):
            pygame.draw.rect(screen,self.color,self.rect)
            screen.blit(self.text_surf,self.text_rect)
        def clicked(self,pos):
            return self.rect.collidepoint(pos)
class State(): #???? Iouno maybe maybe 
    def __init__(self):
        self.current_buttons=[]
        self.previous_buttons=[]
    def addcurrent(self,button):
        
        self.current_buttons.append(button)    
    def removecurrent(self,button): 
        self.current_buttons.remove(button)
    def addprevious(self,button):
        self.previous_buttons.append(button)
    def removeprevious(self,button):
        self.previous_buttons.remove(button)
#need to make a back button, need to find a way to make previous buttons disappear and new buttons appear(same goes for textboxes), need to make a controller,
#maybe for making new buttons and old buttons appearing and disappearing make "States?", ex. I click a button the state of the program changes and loads data that was stored?
