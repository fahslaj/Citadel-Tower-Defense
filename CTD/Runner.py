'''
Created on Jun 12, 2014

@author: fahslaj
'''
from Battleground import *
from CTDSurface import *
''' Run the Citadel Tower Defense game '''
def run():
    # Add main menu
    pygame.display.set_icon(pygame.image.load("resources/Castle Icon.png"))
    pygame.display.set_caption("Citadel Tower Defense")
    CTDSurface.setFactor(32)
    bg = Battleground()

if __name__ == '__main__':
    run()