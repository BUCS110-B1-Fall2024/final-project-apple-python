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
      Newing =Buttons(100,100,50,25,'chartreuse4','Newing')
      Dickinson =Buttons(200,200,50,25,'chartreuse4','Dickinson')
      Mountainview = Buttons(500,500,50,25,'chartreuse4', 'Mountainview')
      Union = Buttons(600,600,50,25, 'chartreuse4', 'Union')
      Library = Buttons(400,400,50,25, 'chartreuse4', 'Library')
      Admissions =Buttons(300,300,50,25, 'chartreuse4', 'Admissions')      
      Hinman = Buttons(700,700, 50,25, 'chartreuse4', 'Hinman')
      #B2Beginning = don't know yet 
      #Lecture Hall
      #Art Building  
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
        #Lecture Hall.create(self.screen)
        #Art Building.create(self.screen)
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
        pygame.display.update()
    
  def places(self, place):
    #Brings user to different places, with an info button
    running = True
    
    #Images
    ciw_pic = Images(r"assets\CIW community.png")
    #hinman_pic = Images(r"assets\ inserthere")
    #newing_pic = Images(r"assets\inserthere")
    #dickinson_pic= Images(r"assets\inserthere")
    #union_pic = Images(r"assets\inserthere")
    #mountainview_pic = Images(r"assets\inserthere")
    #library_pic = Images(r"assets\inserthere")
    #admissions_pic = Images(r"assets\inserthere")
    quit_places = Buttons(720, 20, 50, 25, 'azure4', 'Quit')
    
    while running:
        if place == "CIW":
            ciw_pic.blit(self.screen)
        elif place == "Hinman":
            hinman_pic.blit(self.screen)
        elif place == "Admissions":
            admissions_pic.blit(self.screen)
        elif place == "Union":
            union_pic.blit(self.screen)
        elif place == "Dickinson":
            dickinson_pic.blit(self.screen)
        elif place == "Newing":
            newing_pic.blit(self.screen)
        elif place == "Mountainview":
            mountainview_pic.blit(self.screen)
        elif place == "Library":
            library_pic.blit(self.screen)
        quit_places.create(self.screen)
            #elif other places same set up
  
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_places.is_clicked(event.pos):
                    return "main"
      pygame.display.update()
      
