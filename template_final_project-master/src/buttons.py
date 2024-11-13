import pygame

class Buttons:
    def __init__(self, x, y, width, height, color = '', display = ''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.display = display

    def create(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def is_clicked(self, mouse_pos):
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height