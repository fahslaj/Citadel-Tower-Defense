'''
Created on Jun 12, 2014

@author: fahslaj
'''
import pygame
from CTDSurface import *
''' The base class for a Citadel tower '''
class Citadel(object):

    def place(self, xcoord, ycoord):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.surface = CTDSurface(pygame.image.load("resources/Castle Icon.png"), xcoord, ycoord)
        
    def display(self, screen):
        if (self.surface == None and not (self.xcoord == None and self.ycoord == None)):
            self.surface = CTDSurface(pygame.image.load("resources/Castle Icon.png"), self.xcoord, self.ycoord)
        if (not self.surface == None):
            self.surface.blit(screen)

    def __init__(self, cost = 0, power = 5, xcoord = None, ycoord = None):
        '''
        Constructor
        '''
        self.cost = cost
        self.power = power
        self.level = 0
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.surface = None
        if ((not xcoord == None) and (not ycoord == None)):
            self.place(xcoord, ycoord)