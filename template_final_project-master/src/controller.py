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
    self.font = pygame.font.Font(None, 60)
    
    ##Background Picture
    self.backmain = Images(r"assets\BUOverview(upd).png")
    self.backmenu = Images(r"assets\bearcat_1.png", 10, 10)
    
    #Buttons for Menuloop
    self.start = Buttons(100, 420, 200, 75, 'chartreuse4', 'Start', 30) 
    self.quit = Buttons(500, 420, 200, 75, 'coral1', 'Quit', 30)
    
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
        self.screen.fill('aquamarine4') #fills screen with color
        text = self.font.render('Binghamton Tour', True, 'black', 'aquamarine4')
        trect = text.get_rect()
        trect.center = (self.width // 2, self.height // 4)
        self.screen.blit(text, trect)
        self.backmenu.blit(self.screen)
        
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
      #Dickinson
      #Hinman
      #Mountain View
      #Newing
      #Old Dickinson
      #Lecture Hall
      #Art Building
      #Science Building
      
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
    ciw_pic = Images(r"assets\CIW community.png")
    
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
      