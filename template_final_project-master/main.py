import pygame
#import your controller
width = 900
height = 900
darkgreen = (34,139,34)
white = (255,255,255)
clock=pygame.time.Clock()
clock.tick(60)

def main():
    pygame.init()
    pygame.display.set_mode(width,height)
    #Create an instance on your controller object
    #Call your mainloop
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()


# needed: images, buttons, videos, info 
#buttons: start, stop, info, video, moving buttons(upstairs/downstairs?, or left/right?, both?)



pygame.display.set_mode(width,height)
class buttons:
    def __init__(self, shape, coords,type, font_size=12, t_color=white,):
        self.shape = shape
        self.coords = coords
        self.type = type
        self.color = color
        self.text = text
        return self.type, self.coords, self.shape
    def displayvid(self):
    def displayimg(self):
    def displayinfo(self):
