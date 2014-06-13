'''
Created on Jun 12, 2014

@author: fahslaj
'''
import pygame
from CTDSurface import *
from Placeables import *
''' The base class for a Citadel tower '''
class Citadel(Placeable):
        
    def display(self, screen):
        super(Citadel, self).display(screen, "resources/Castle Icon.png", size=2)

    def __init__(self, cost = 0, power = 5, range = 5, xcoord = None, ycoord = None):
        '''
        Constructor
        '''
        super(Citadel, self).__init__(xcoord, ycoord)
        self.cost = cost
        self.power = power
        self.range = range
        self.level = 0