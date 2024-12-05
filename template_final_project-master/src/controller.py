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
      ciw = Buttons(250, 150, 50, 25, 'chartreuse4', 'CIW') #IP
      Newing = Buttons(35, 380, 50, 25,'chartreuse4','Newing') #IP
      Dickinson = Buttons(120,240,50, 25,'chartreuse4','Dickinson') #IP
      Mountainview = Buttons(415, 75, 50, 25,'chartreuse4', 'Mountainview') #IP
      Union = Buttons(270, 280, 50, 25, 'chartreuse4', 'Union') #IP
      Library = Buttons(400, 300, 50, 25, 'chartreuse4', 'Library') #IP
      Admissions = Buttons(210, 290, 50, 25, 'chartreuse4', 'Admissions')  #IP    
      Hinman = Buttons(550, 220, 50, 25, 'chartreuse4', 'Hinman') #IP
      old_digman = Buttons(180, 415, 50, 25, 'chartreuse4', 'Old Digman') #IP
      fine_arts = Buttons(360, 420, 50, 25, 'chartreuse4', 'Fine Arts')
      west_gym = Buttons(500, 700, 50, 25, 'chartreuse4', 'West Gym')
      
      #B2Beginning = don't know yet 
      #Lecture Hall  
      #Science Building
      
      place = None
      
      while running:
        self.backmain.blit(self.screen)
        
        #Creates Buttons
        quit1.create(self.screen)
        ciw.create(self.screen)
        Newing.create(self.screen)
        Mountainview.create(self.screen)
        Dickinson.create(self.screen)
        Hinman.create(self.screen)
        Union.create(self.screen)
        Library.create(self.screen)
        Admissions.create(self.screen)
        old_digman.create(self.screen)
        fine_arts.create(self.screen)
        west_gym.create(self.screen)
        
        #Lecture Hall.create(self.screen)
        #Science Building.create(self.screen) #placeholders  
        #B2beginnning.create(self.screen)
        
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            if quit1.is_clicked(event.pos):
              return "MENU"
            elif ciw.is_clicked(event.pos):
              place = "CIW"
              return self.places(place)
            elif Library.is_clicked(event.pos):
                place = "Library"
                return self.places(place)
            elif Admissions.is_clicked(event.pos):
                place = "Admissions"
                return self.places(place)
            elif Mountainview.is_clicked(event.pos):
                place = "Mountainview"
                return self.places(place)
            elif Dickinson.is_clicked(event.pos):
                place = "Dickinson"
                return self.places(place)
            elif Newing.is_clicked(event.pos):
                place = "Newing"
                return self.places(place)
            elif Union.is_clicked(event.pos):
                place = "Union"
                return self.places(place)
            elif Hinman.is_clicked(event.pos):
                place = "Hinman"
                return self.places(place)
            elif old_digman.is_clicked(event.pos):
              place = "Old Digman"
              return self.places(place)
            elif fine_arts.is_clicked(event.pos):
              place = "Fine Arts"
              return self.places(place)
            elif west_gym.is_clicked(event.pos):
              place = "West Gym"
              return self.places(place)
        pygame.display.update()
    
  def places(self, place):
    #Brings user to different places, with an info button
    running = True
    
    #Images
    ciw_pic = Images(r"assets\CIW community.png")
    hinman_pic = Images(r"assets\Hinman community.png")
    newing_pic = Images(r"assets\Newing community.png")
    dickinson_pic= Images(r"assets\Dickinson community.png")
    mountainview_pic = Images(r"assets\MountainView Community.png")
    oldD_pic = Images(r"assets\Old DIckinson Community.png")
    #fine_artspic = Images(r"")
    #west_gympic = Images(r"")
    #union_pic = Images(r"assets\inserthere")
    #library_pic = Images(r"assets\inserthere")
    #admissions_pic = Images(r"assets\inserthere")
    
    quit_places = Buttons(720, 20, 50, 25, 'azure4', 'Quit')
    
    while running:
        if place == "CIW":
            ciw_pic.blit(self.screen)
        elif place == "Hinman":
            hinman_pic.blit(self.screen)
        #elif place == "Admissions":
            #admissions_pic.blit(self.screen)
        #elif place == "Union":
            #union_pic.blit(self.screen)
        elif place == "Dickinson":
            dickinson_pic.blit(self.screen)
        elif place == "Newing":
            newing_pic.blit(self.screen)
        elif place == "Mountainview":
            mountainview_pic.blit(self.screen)
        #elif place == "Library":
            #library_pic.blit(self.screen)
        elif place == "Old Dickinson":
          oldD_pic.blit(self.screen)
        #elif place == "Fine Arts":
          #fine_artspic.blit(self.screen)
        #elif place == "West Gym":
          #west_gympic.blit(self.screen)
        quit_places.create(self.screen)
  
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_places.is_clicked(event.pos):
                    return "main"
        pygame.display.update()
      
