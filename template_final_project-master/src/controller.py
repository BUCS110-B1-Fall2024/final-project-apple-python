import pygame
from buttons import Buttons
from images import Images

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    self.width = 900
    self.height = 900
    self.screen = pygame.display.set_mode(self.width, self.height)
    
    #Colors
    self.darkgreen = (34,139,34)
    self.white = (255,255,255)
    
    # We can use a dictionary of place_name: file_name
    
    #Create start and quit buttons
    
    clock = pygame.time.Clock()
    clock.tick(60)
    
  def mainloop(self):
    #select state loop
      
  
  ### below are some sample loop states ###

  def menuloop(self):
    # Brings up the menu with start and quit buttons
      #event loop

      #update data

      #redraw
      
  def mainmap(self):
    #Brings user to main map where they can pick were to start
      #event loop

      #update data

      #redraw
    
  def places(self):
    #Brings user to different places, with an info button
      #event loop

      #update data

      #redraw
