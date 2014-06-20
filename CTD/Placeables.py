'''
Created on Jun 13, 2014

@author: fahslaj
'''
import pygame
from CTDSurface import *
''' The base class of anything that gets drawn on a grid location '''
class Placeable(object):
              
    def display(self, screen, imageString = "resources/Placeable.png", sizeFactor = 1, scalex = 1, scaley = 1, rotate = 0):
        if (self.surface == None and not (self.xcoord == None and self.ycoord == None)):
             self.img = pygame.image.load(imageString)
             self.img = pygame.transform.rotate(self.img, rotate)
             self.img = pygame.transform.scale(self.img, (CTDSurface.getFactor()*scalex*sizeFactor, CTDSurface.getFactor()*scaley*sizeFactor))
        self.surface = CTDSurface(self.img, self.xcoord, self.ycoord)
        if (not self.surface == None):
            self.surface.blit(screen)

    def __init__(self, xcoord, ycoord):
        '''
        Constructor
        '''
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.surface = None
        self.img = None
        
''' A tree is an immovable boundary object '''
class Tree(Placeable):
    
    @staticmethod
    def TreeBlock(x1, y1, x2, y2, toAppend={}):
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                t = Tree(i,j)
                toAppend[(i,j)]=t
                toAppend[(i+1,j)]=t
                toAppend[(i,j+1)]=t
                toAppend[(i+1,j+1)]=t
        return toAppend
    
    def display(self, screen):
        super(Tree, self).display(screen, "resources/Tree.png", 2)

    def __init__(self, xcoord, ycoord):
        super(Tree, self).__init__(xcoord, ycoord)
        
''' A field is an immovable, but overlayable, scenery object. '''
class Field(Placeable):
    
    @staticmethod
    def FieldBlock(x1, y1, x2, y2, toAppend={}):
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                toAppend[(i,j)]=Field(i,j)
        return toAppend
    
    def display(self, screen):
        super(Field, self).display(screen, "resources/Field.png")
        
    def __init__(self, xcoord, ycoord):
        super(Field, self).__init__(xcoord, ycoord)
       
''' A path defines where enemies can move '''
class Path(Placeable):

    @staticmethod
    def LayPathDown(location, length, toAppend={}):
        path = None
        if (location in toAppend):
            path = toAppend[location]
        if (not (type(path) is Path)):
            path = Path(location[0], location[1])
        for j in range(location[1], location[1]+length-1):
            next = Path(location[0], j+1)
            path.next = next
            toAppend[(location[0],j)]=path
            path = next
        toAppend[location[0], location[1]+length-1] = path
        return toAppend
    
    @staticmethod
    def LayPathUp(location, length, toAppend={}):
        path = None
        if (location in toAppend):
            path = toAppend[location]
        if (not (type(path) is Path)):
            path = Path(location[0], location[1])
        for j in range(location[1], location[1]-length+1, -1):
            next = Path(location[0], j-1)
            path.next = next
            toAppend[(location[0], j)] = path
            path = next
        toAppend[location[0], location[1]-length+1] = path
        return toAppend
    
    @staticmethod
    def LayPathRight(location, length, toAppend={}):
        path = None
        if (location in toAppend):
            path = toAppend[location]
        if (not (type(path) is Path)):
            path = Path(location[0], location[1])
        for j in range(location[0], location[0]+length-1):
            next = Path(j+1, location[1])
            path.next = next
            toAppend[(j,location[1])]=path
            path = next
        toAppend[location[0]+length-1, location[1]] = path
        return toAppend
    
    @staticmethod
    def LayPathLeft(location, length, toAppend={}):
        path = None
        if (location in toAppend):
            path = toAppend[location]
        if (not (type(path) is Path)):
            path = Path(location[0], location[1])
        for j in range(location[0], location[0]-length+1, -1):
            next = Path(j-1, location[1])
            path.next = next
            toAppend[(j, location[1])]=path
            path = next
        toAppend[location[0]-length+1, location[1]] = path
        return toAppend
    
    @staticmethod
    def TraversePath(path):
        strings = []
        while (not path == None):
            strings.append((path.xcoord, path.ycoord))
            path = path.next
        print(str(strings))
    
    def display(self, screen):
        super(Path, self).display(screen, "resources/Path.png")
        
    def __init__(self, xcoord, ycoord, next = None):
        super(Path, self).__init__(xcoord, ycoord)
        self.next = next
    

''' A spawn is where the enemies are generated '''
class Spawn(Placeable):
    
    def display(self, screen):
        if (self.vertical):
            x = 1
            y = self.length
            r = -90
        else:
            y = 1
            x = self.length
            r = 0
        super(Spawn, self).display(screen, "resources/Spawn.png", scalex = x, scaley = y, rotate = r) 
        
    def setSpawn(self, num = 20, toAppend = {}):
        self.spawncount = num
        toAppend[(self.xcoord, self.ycoord)] = self
        if (self.vertical):
            toAppend[(self.xcoord, self.ycoord+1)] = self
        else:
            toAppend[(self.xcoord+1, self.ycoord)] = self
    
    def __init__(self, xcoord, ycoord, vertical = False, length = 2):
        super(Spawn, self).__init__(xcoord, ycoord)
        self.vertical = vertical    
        self.length = length
        
''' A cave is the place where the enemies will escape to '''
class Cave(Placeable):
    
    def display(self, screen):
        if (self.facing == "LEFT"):
            r = -90
        elif (self.facing == "DOWN"):
            r = 180
        elif (self.facing == "RIGHT"):
            r = 90
        else:
            r = 0
        super(Cave, self).display(screen, "resources/Cave.png", scalex = 2, scaley = 2, rotate = r)
        
    def setCave(self, toAppend = {}):
        toAppend[(self.xcoord, self.ycoord)] = self
        toAppend[(self.xcoord+1, self.ycoord)] = self
        toAppend[(self.xcoord, self.ycoord+1)] = self
        toAppend[(self.xcoord+1, self.ycoord+1)] = self
        
    def __init__(self, xcoord, ycoord, facing = "LEFT"):
        super(Cave, self).__init__(xcoord, ycoord)
        self.facing = facing
        
        
        
        
        
        
        
        
        
        
        