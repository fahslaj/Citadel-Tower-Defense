'''
Created on Jun 12, 2014

@author: fahslaj
'''

import pygame

''' A surface that keeps track of its coordinate location '''
class CTDSurface(object):

    @staticmethod
    def setFactor(factor = 32):
        global FACTOR
        FACTOR = factor
        
    @staticmethod
    def getFactor():
        return FACTOR

    def blit(self, screen):
        screen.blit(self.surface, (self.xpix, self.ypix))

    def __init__(self, surface, xcoord, ycoord):
        '''
        Constructor
        '''
        self.surface = surface
        self.xpix = (xcoord-1) * FACTOR
        self.ypix = (ycoord-1) * FACTOR
        
        
