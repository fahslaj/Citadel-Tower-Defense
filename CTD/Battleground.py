'''
Created on Jun 12, 2014

@author: fahslaj
'''

import pygame
import sys

from CTDSurface import *
from Placeables import *
from Citadel import *

''' The battlefield that represents a level in CTD '''
class Battleground(object):
    
    ''' Initialize the battleground '''
    def start(self, level = 1):
        # do initialization stuff
        self.screen = pygame.display.set_mode((self.width*CTDSurface.getFactor(), self.height*CTDSurface.getFactor()))
        self.surfaces = {(0,0):CTDSurface(pygame.image.load("resources/Backdrop.png"), 1,1)}
        self.surfaces[(0,0)].surface.set_alpha(100)
        self.labels = {}
        self.assignLabels()
        self.scenery = {}
        self.boundaries = {}
        self.citadels = {}
        self.enemies = {}
        self.clock = pygame.time.Clock()
        
        if (level == 1):
            self.level1()
        
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
                self.surfaces[surface].blit(self.screen)
                
            it = iter(sorted(self.scenery.items()))    
            for value in it:
                value[1].display(self.screen)
                
            it = iter(sorted(self.boundaries.items()))    
            for value in it:
                value[1].display(self.screen)
                
            it = iter(sorted(self.citadels.items())) 
            for citadel in it:
                citadel[1].display(self.screen)
                
            it = iter(sorted(self.enemies.items())) 
            for enemy in it:
                enemy[1].display(self.screen)
                
            it = iter(sorted(self.labels.items()))
            for label in it:
                label[1].blit(self.screen)
                
            pygame.display.update()
            
    def assignLabels(self):
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 12)
        for i in range(self.width+1):
            label = font.render(str(i), True, (0,0,0))
            self.labels[(i,1)]=CTDSurface(label, i, 1)
        for i in range(self.height-1):
            label = font.render(str(i), True, (0,0,0))
            self.labels[(1,i)]=CTDSurface(label, 1, i)
            
    def level1(self):
        self.scenery[(1,1)] = Spawn(1,1)
        Tree.TreeBlock(1, 5, 2, 20, self.boundaries)
        Tree.TreeBlock(3, 1, 40, 2, self.boundaries)
        Field.FieldBlock(5, 3, 5, 7, self.scenery)

    def __init__(self, scrwidth = 1280, scrheight = 720):
        self.width = int(scrwidth/CTDSurface.getFactor())
        self.height = int(scrheight/CTDSurface.getFactor())
        self.start()