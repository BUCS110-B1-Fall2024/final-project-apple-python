import pygame
from src.buttons import Buttons
from src.images import Images

class Controller:
  
  def __init__(self):
    #sets up the initial pygame screen
    pygame.init()
    self.width = 800
    self.height = 800
    self.screen = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption('College Tour')
    self.font = pygame.font.Font(None, 20)
    
    #You can just pull color names from https://www.pygame.org/docs/ref/color_list.html
    #self.darkgreen = (34,139,34)
    #self.white = (255,255,255)
    
    ##Pictures
    self.backmain = Images(r"C:\Users\apjen\Desktop\final-project-apple-python\template_final_project-master\assets\BUOverview(upd).png")
    
    #Buttons for Menuloop
    self.start = Buttons(200, 350, 75, 50, 'chartreuse4', 'Start') 
    self.quit = Buttons(525, 350, 75, 50, 'coral1', 'Quit')
    
    self.clock = pygame.time.Clock()
    self.clock.tick(60)
    
  def mainloop(self):
    #selects state loop
    state = "MENU"
    running = True
    
    while running:
      if state == "MENU":
        state = self.menuloop()
      elif state == "main":
        state = self.mainmap()
      elif state == "places":
        state = self.places()
        
    pygame.quit()

  def menuloop(self):
    # Brings up the menu with start and quit buttons
    running = True
    while running:
        self.screen.fill('floralwhite') #fills screen with color
        text = self.font.render('Binghamton Tour', True, 'black', 'floralwhite')
        trect = text.get_rect()
        trect.center = (self.width // 2, self.height // 4)
        self.screen.blit(text, trect)
        
        #Buttons
        self.start.create(self.screen)
        self.quit.create(self.screen)
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            quit()
          if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start.is_clicked(event.pos):
              return "main"
            elif self.quit.is_clicked(event.pos):
              pygame.quit()
              quit()
          
        pygame.display.update()
      
  def mainmap(self):
    #Brings user to main map where they can pick were to start
      running = True
      
      ##Main Map Buttons
      quit1 = Buttons(720, 20, 50, 25, 'azure4', 'Quit')
      ciw = Buttons(250, 150, 50, 25, 'chartreuse4', 'CIW')
      
      place = None
      
      while running:
        self.backmain.blit(self.screen)
        
        #Creates Buttons
        quit1.create(self.screen)
        ciw.create(self.screen)
        
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            if quit1.is_clicked(event.pos):
              return "MENU"
            elif ciw.is_clicked(event.pos):
              place = "CIW"
              return self.places(place)
        pygame.display.update()
    
  def places(self, place):
    #Brings user to different places, with an info button
    running = True
    
    #Images
    ciw_pic = Images(r"C:\Users\apjen\Desktop\final-project-apple-python\template_final_project-master\assets\CIW community.png")
    
    quit_places = Buttons(720, 20, 50, 25, 'azure4', 'Quit')
    
    while running:
      if place == "CIW":
        ciw_pic.blit(self.screen)
      #elif other places same set up
      
      quit_places.create(self.screen)
      
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          if quit_places.is_clicked(event.pos):
            return "main"
      pygame.display.update()
      