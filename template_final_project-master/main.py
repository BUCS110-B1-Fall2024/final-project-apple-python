import pygame
from src.controller import Controller


def main():
    controller = Controller()
    controller.mainloop()
    #Create an instance on your controller object
    #Call your mainloop
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()


# needed: images, buttons, videos, info 
#buttons: start, stop, info, video, moving buttons(upstairs/downstairs?, or left/right?, both?)



