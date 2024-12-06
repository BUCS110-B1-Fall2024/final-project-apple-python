import pygame
from src.buttons import Buttons
from src.images import Images
from src.info import Info

class Controller:
  
  def __init__(self):
    """Sets up the intial pygame window, along with menu buttons, and background pictures for the menu and main map.
    """
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
    """Sets up the state loop for the menu, main map, and the different places
    """
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
    """Sets up the menu screen with a start and quit button

    Returns:
        "main" (str): Returns "main" to the main loop to change the state
    """
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
    """Creates the main map, along with all of the buttons

    Returns:
    self.places(place) (str): Changes the state to places, along with the place name
    """
    #Brings user to main map where they can pick where to start
    running = True
      
    ##Main Map Buttons
    quit1 = Buttons(720, 20, 50, 25, 'azure4', 'Quit')
    ciw = Buttons(250, 150, 50, 25, 'cornflowerblue', 'CIW')
    newing = Buttons(35, 380, 50, 25,'cornflowerblue','Newing')
    dickinson = Buttons(120, 240, 70, 25,'cornflowerblue','Dickinson')
    mountainview = Buttons(390, 60, 80, 25,'cornflowerblue', 'Mountainview')
    union = Buttons(270, 280, 50, 25, 'cornflowerblue', 'Union')
    library = Buttons(400, 300, 50, 25, 'cornflowerblue', 'Library')
    admissions = Buttons(210, 310, 70, 25, 'cornflowerblue', 'Admissions')
    hinman = Buttons(550, 220, 55, 25, 'cornflowerblue', 'Hinman')
    old_dickinson = Buttons(180, 415, 90, 25, 'cornflowerblue', 'Old Dickinson')
    fine_arts = Buttons(360, 420, 60, 25, 'cornflowerblue', 'Fine Arts')
    west_gym = Buttons(500, 700, 70, 25, 'cornflowerblue', 'West Gym')
    east_gym = Buttons(150, 650, 70, 25, 'cornflowerblue', 'East Gym')
    c4 = Buttons(60, 320, 50, 25, 'cornflowerblue', 'C4') 
    manage_school = Buttons(570, 350, 120, 25, 'cornflowerblue', 'School of Management')
    app = Buttons(390, 110, 90, 25, 'cornflowerblue', 'App Dinning Hall')
      
    place = None
      
    while running:
      self.backmain.blit(self.screen)
        
      #Creates Buttons
      quit1.create(self.screen)
      ciw.create(self.screen)
      newing.create(self.screen)
      mountainview.create(self.screen)
      dickinson.create(self.screen)
      hinman.create(self.screen)
      union.create(self.screen)
      library.create(self.screen)
      admissions.create(self.screen)
      old_dickinson.create(self.screen)
      fine_arts.create(self.screen)
      west_gym.create(self.screen)
      east_gym.create(self.screen)
      c4.create(self.screen)
      manage_school.create(self.screen)
      app.create(self.screen)
        
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
          elif library.is_clicked(event.pos):
            place = "Library"
            return self.places(place)
          elif admissions.is_clicked(event.pos):
            place = "Admissions"
            return self.places(place)
          elif mountainview.is_clicked(event.pos):
            place = "Mountain View"
            return self.places(place)
          elif dickinson.is_clicked(event.pos):
            place = "Dickinson"
            return self.places(place)
          elif newing.is_clicked(event.pos):
            place = "Newing"
            return self.places(place)
          elif union.is_clicked(event.pos):
            place = "Union"
            return self.places(place)
          elif hinman.is_clicked(event.pos):
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
    """Changes the background according to the place selected, also handles the information

    Args:
        place (str): Which place was picked on the main map

    Returns:
        "main" (str): Returns "main" to change the state back to the main loop
    """
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