'''
Created on Jun 12, 2014

@author: fahslaj
'''

import pygame
import math
import sys

from CTDSurface import *
from Placeables import *
from Citadel import *
from Enemies import *

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
            self.handle()
            self.trymove()
            self.tryspawn()
            self.refresh()        
            self.highlightMouse()
            self.clock.tick(60)
            
    def trymove(self):
        self.movecounter+=1
        if (self.movecounter % 4 == 0):
            temp = []
            for enemy in self.enemies:
                temp.append(self.enemies[enemy])
            for enemy in temp:
                enemyx = enemy.xcoord
                enemyy = enemy.ycoord
                path = self.scenery[(enemyx, enemyy)]
                next = path.next
                if (not next == None):
                    enemy.xcoord = next.xcoord
                    enemy.ycoord = next.ycoord
                    self.enemies.pop((enemyx, enemyy))
                    self.enemies[(enemy.xcoord, enemy.ycoord)] = enemy
                else:
                    self.enemies.pop((enemyx, enemyy))
            
    def tryspawn(self):
        if (self.movecounter % 6 == 0 and self.spawn.spawncount > 0):
            self.spawn.spawncount-=1
            x = self.spawn.xcoord
            y = self.spawn.ycoord
            enemy = Enemy(x, y, "UP")
            self.enemies[(x,y)] = enemy
            if (self.spawn.vertical):
                self.enemies[(x, y+1)] = Enemy(x, y+1, "UP")
            else:
                self.enemies[(x+1, y)] = Enemy(x+1, y, "UP")
    
    def handle(self):    
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()
                
    def highlightMouse(self):
        location = pygame.mouse.get_pos()
        fact = CTDSurface.getFactor()
        x = math.floor(location[0]/fact)
        y = math.floor(location[1]/fact)
        x1 = x*fact
        y1 = y*fact
        x2 = fact
        y2 = fact
        #print("X1: "+str(x1)+" Y1: "+str(y1)+" X2: "+str(x2)+" Y2: "+str(y2))
        color = (0, 150, 0)
        if ((x+1,y+1) in self.boundaries.keys()):
            color = (150, 0, 0)
        pygame.draw.rect(self.screen, color, pygame.Rect((x1,y1),(x2,y2)))
        self.screen.blit(self.font.render("("+str(x+1)+", "+str(y+1)+")", 1, (0,0,0)), (x1, y1))
        pygame.display.update()
            
    def refresh(self):
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
        self.font = pygame.font.SysFont("Arial", 12)
        for i in range(self.width+1):
            label = self.font.render(str(i), True, (0,0,0))
            self.labels[(i,1)]=CTDSurface(label, i, 1)
        for i in range(self.height-1):
            label = self.font.render(str(i), True, (0,0,0))
            self.labels[(1,i)]=CTDSurface(label, 1, i)
            
    def level1(self):
        Field.FieldBlock(1, 1, self.width, self.height-2, self.scenery)
        Tree.TreeBlock(3,1,self.width-1,1,self.boundaries)
        Tree.TreeBlock(1,5,2,self.height-3,self.boundaries)
        Tree.TreeBlock(29,2,self.width-1,4,self.boundaries)
        Tree.TreeBlock(3, 20, 13, self.height-3, self.boundaries)
        Tree.TreeBlock(26, 10, 29, 17, self.boundaries)
        
        Path.LayPathDown((1, 1), 4, self.scenery)
        Path.LayPathRight((1, 4), 8, self.scenery)
        Path.LayPathDown((8,4), 8, self.scenery)
        Path.LayPathLeft((8,11), 4, self.scenery)
        Path.LayPathDown((5,11), 7, self.scenery)
        Path.LayPathRight((5,17), 9, self.scenery)
        Path.LayPathUp((13,17), 12, self.scenery)
        Path.LayPathRight((13, 6), 5, self.scenery)
        Path.LayPathDown((17,6), 16, self.scenery)
        Path.LayPathRight((17,21), 15, self.scenery)
        Path.LayPathUp((31, 21), 16, self.scenery)
        Path.LayPathLeft((31, 6), 4, self.scenery)
        Path.LayPathDown((28, 6), 2, self.scenery)
        Path.LayPathLeft((28, 7), 5, self.scenery)
        Path.TraversePath(self.scenery[(1,1)])
        
        Path.LayPathDown((2, 1), 3, self.scenery)
        Path.LayPathRight((2, 3), 17, self.scenery)
        Path.LayPathDown((18,3), 18, self.scenery)
        Path.LayPathRight((18,20), 6, self.scenery)
        Path.LayPathUp((23, 20), 8, self.scenery)
        Path.LayPathLeft((23, 13), 3, self.scenery)
        Path.LayPathUp((21,13), 10, self.scenery)
        Path.LayPathRight((21, 4), 6, self.scenery)
        Path.LayPathDown((26, 4), 3, self.scenery)
        Path.LayPathLeft((26,6), 3, self.scenery)
        Path.TraversePath(self.scenery[(2,1)])
        
        self.spawn = Spawn(1,1)
        self.spawn.setSpawn(20, self.boundaries)
        self.cave = Cave(23,6, "RIGHT")
        self.cave.setCave(self.boundaries)

    def __init__(self, scrwidth = 1280, scrheight = 720):
        self.width = int(scrwidth/CTDSurface.getFactor())
        self.height = int(scrheight/CTDSurface.getFactor())
        self.movecounter = 0
        self.start()