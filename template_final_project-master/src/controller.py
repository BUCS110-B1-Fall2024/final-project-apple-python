import pygame
from src.buttons import Buttons
from src.images import Images
from src.info import Info

class Controller:
  
  def __init__(self):
    #sets up the initial pygame screen
    pygame.init()
    self.width = 800
    self.height = 750
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
        #Screen Set up
        self.screen.fill('aquamarine4') 
        text = self.font.render('Binghamton Tour', True, 'black', 'aquamarine4')
        trect = text.get_rect()
        trect.center = (self.width // 2, self.height // 4)
        self.screen.blit(text, trect)
        self.backmenu.blit(self.screen)
        
        #Buttons
        self.start.create(self.screen)
        self.quit.create(self.screen)
        
        #Event Loop
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
    #Brings user to main map where they can pick where to start
      running = True
      
      ##Main Map Buttons
      quit1 = Buttons(720, 20, 50, 25, 'azure4', 'Quit')
      ciw = Buttons(250, 150, 50, 25, 'cornflowerblue', 'CIW') #IP-
      Newing = Buttons(35, 380, 50, 25,'cornflowerblue','Newing') #IP-
      Dickinson = Buttons(120, 240, 70, 25,'cornflowerblue','Dickinson') #IP-
      Mountainview = Buttons(390, 60, 80, 25,'cornflowerblue', 'Mountainview') #IP-
      Union = Buttons(270, 280, 50, 25, 'cornflowerblue', 'Union') #IP-
      Library = Buttons(400, 300, 50, 25, 'cornflowerblue', 'Library') #IP-
      Admissions = Buttons(210, 310, 70, 25, 'cornflowerblue', 'Admissions')  #IP-
      Hinman = Buttons(550, 220, 55, 25, 'cornflowerblue', 'Hinman') #IP-
      old_dickinson = Buttons(180, 415, 90, 25, 'cornflowerblue', 'Old Dickinson') #IP-
      fine_arts = Buttons(360, 420, 60, 25, 'cornflowerblue', 'Fine Arts') #IP-
      west_gym = Buttons(500, 700, 70, 25, 'cornflowerblue', 'West Gym') #IP-
      east_gym = Buttons(150, 650, 70, 25, 'cornflowerblue', 'East Gym') #IP-
      c4 = Buttons(60, 320, 50, 25, 'cornflowerblue', 'C4') #IP-
      manage_school = Buttons(570, 350, 120, 25, 'cornflowerblue', 'School of Management')
      app = Buttons(390, 110, 90, 25, 'cornflowerblue', 'App Dinning Hall')
      
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
        old_dickinson.create(self.screen)
        fine_arts.create(self.screen)
        west_gym.create(self.screen)
        east_gym.create(self.screen)
        c4.create(self.screen)
        manage_school.create(self.screen)
        app.create(self.screen)
        
        #Lecture Hall.create(self.screen)
        #Science Building.create(self.screen) #placeholders  
        #B2beginnning.create(self.screen)
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            quit()
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
                place = "Mountain View"
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
            elif old_dickinson.is_clicked(event.pos):
              place = "Old Dickinson"
              return self.places(place)
            elif fine_arts.is_clicked(event.pos):
              place = "Fine Arts"
              return self.places(place)
            elif west_gym.is_clicked(event.pos):
              place = "West Gym"
              return self.places(place)
            elif east_gym.is_clicked(event.pos):
              place = "East Gym"
              return self.places(place)
            elif c4.is_clicked(event.pos):
              place = "C4"
              return self.places(place)
            elif manage_school.is_clicked(event.pos):
              place = "School of Management"
              return self.places(place)
            elif app.is_clicked(event.pos):
              place = "App"
              return self.places(place)
        pygame.display.update()
    
  def places(self, place):
    #Brings user to different places, with an info button
    running = True
    
    #Images
    ciw_pic = Images(r"assets\CIW community.png")
    hinman_pic = Images(r"assets\HInman community.png")
    newing_pic = Images(r"assets\Newing community.png")
    dickinson_pic= Images(r"assets\Dickinson community.png")
    mountainview_pic = Images(r"assets\MountainView Community.png")
    oldD_pic = Images(r"assets\Old DIckinson Community.png")
    fine_artspic = Images(r"assets\Fine Arts main.png")
    west_gympic = Images(r"assets\Screenshot 2024-12-05 184522.png")
    east_gympic = Images(r"assets\East_Gym.png")
    union_pic = Images(r"assets\Western Union.png")
    library_pic = Images(r"assets\Library1.png")
    admissions_pic = Images(r"assets\Admissions.png")
    c4_pic = Images(r"assets\C4.png")
    manage_schoolpic = Images(r"assets\ABA.png")
    app_pic = Images(r"assets\Appdininghall.png")
    
    quit_places = Buttons(720, 20, 50, 25, 'azure4', 'Quit')
    info = Buttons(15, 500, 80, 45, 'azure', 'Info')
    
    visible_info = False
    
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
        elif place == "Mountain View":
            mountainview_pic.blit(self.screen)
        elif place == "Library":
            library_pic.blit(self.screen)
        elif place == "Old Dickinson":
          oldD_pic.blit(self.screen)
        elif place == "Fine Arts":
          fine_artspic.blit(self.screen)
        elif place == "West Gym":
          west_gympic.blit(self.screen)
        elif place == "East Gym":
          east_gympic.blit(self.screen)
        elif place == "C4":
          c4_pic.blit(self.screen)
        elif place == "School of Management":
          manage_schoolpic.blit(self.screen)
        elif place == "App":
          app_pic.blit(self.screen)
          
        quit_places.create(self.screen)
        info.create(self.screen)
        
        if visible_info:
          place_info = Info(place)
          place_info.display(self.screen)
  
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            quit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if quit_places.is_clicked(event.pos):
                return "main"
              if info.is_clicked(event.pos):
                visible_info = not visible_info
        pygame.display.update()