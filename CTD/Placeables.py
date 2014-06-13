'''
Created on Jun 13, 2014

@author: fahslaj
'''
import pygame
from CTDSurface import *
''' The base class of anything that gets drawn on a grid location '''
class Placeable(object):
              
    def display(self, screen, imageString = "resources/Placeable.png", sizeFactor = 1, scalex = 1, scaley = 1):
        if (self.surface == None and not (self.xcoord == None and self.ycoord == None)):
            img = pygame.image.load(imageString)
            img = pygame.transform.scale(img, (CTDSurface.getFactor()*scalex*sizeFactor, CTDSurface.getFactor()*scaley*sizeFactor))
            self.surface = CTDSurface(img, self.xcoord, self.ycoord)
        if (not self.surface == None):
            self.surface.blit(screen)

    def __init__(self, xcoord, ycoord):
        '''
        Constructor
        '''
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.surface = None
        
''' A tree is an immovable boundary object '''
class Tree(Placeable):
    
    @staticmethod
    def TreeBlock(x1, y1, x2, y2, toAppend={}):
        for i in range(x1, x2):
            for j in range(y1, y2):
                toAppend[(i,j)]=Tree(i,j)
        return list
    
    def display(self, screen):
        super(Tree, self).display(screen, "resources/Tree.png", 2)

    def __init__(self, xcoord, ycoord):
        super(Tree, self).__init__(xcoord, ycoord)
        
''' A field is an immovable, but overlayable, scenery object. '''
class Field(Placeable):
    
    @staticmethod
    def FieldBlock(x1, y1, x2, y2, toAppend={}):
        for i in range(x1, x2):
            for j in range(y1, y2):
                toAppend[(i,j)]=Field(i,j)
        return list
    
    def display(self, screen):
        super(Field, self).display(screen, "resources/Field.png")
        
    def __init__(self, xcoord, ycoord):
        super(Field, self).__init__(xcoord, ycoord)
       
''' A spawn is where the enemies are generated '''
class Spawn(Placeable):
    
    def display(self, screen):
        if (self.vertical):
            x = 1
            y = 2
        else:
            y = 1
            x = 2
        super(Spawn, self).display(screen, "resources/Spawn.png", scalex = x, scaley = y) 
        
    def __init__(self, xcoord, ycoord, vertical = False):
        super(Spawn, self).__init__(xcoord, ycoord)
        self.vertical = vertical    
        
        
        
        
        
        
        
        
        
        
        
        