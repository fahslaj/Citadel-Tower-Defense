'''
Created on Jun 12, 2014

@author: fahslaj
'''

import pygame
import sys

from CTDSurface import *
from Citadel import *

''' The battlefield that represents a level in CTD '''
class Battleground(object):
    
    ''' Initialize the battleground '''
    def start(self):
        # do initialization stuff
        self.screen = pygame.display.set_mode((self.width*CTDSurface.getFactor(), self.height*CTDSurface.getFactor()))
        self.surfaces = [CTDSurface(pygame.image.load("resources/Backdrop.png"), 1,1)]
        self.surfaces[0].surface.set_alpha(100)
        self.citadels = [Citadel(xcoord=2, ycoord=2)]
        self.enemies = []
        self.clock = pygame.time.Clock()
        self.mainloop()
        pygame.quit()

    ''' The main loop of the game that handles events '''
    def mainloop(self):
        while (True):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit()
                    
            self.screen.fill((255,255,255))
            for surface in self.surfaces:
                surface.blit(self.screen)
            for citadel in self.citadels:
                citadel.display(self.screen)
            pygame.display.update()

    def __init__(self, scrwidth = 1280, scrheight = 720):
        self.width = int(scrwidth/CTDSurface.getFactor())
        self.height = int(scrheight/CTDSurface.getFactor())
        self.start()