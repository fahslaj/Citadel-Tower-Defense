'''
Created on Jun 16, 2014

@author: fahslaj
'''
from Placeables import *
class Enemy(Placeable):
    
    def display(self, screen):
        if (self.facing == "LEFT"):
            r = 90
        elif (self.facing == "DOWN"):
            r = 180
        elif (self.facing == "RIGHT"):
            r = -90
        else:
            r = 0
        super(Enemy, self).display(screen, "resources/Knave.png", rotate = r)

    def __init__(self, xcoord, ycoord, facing = "UP"):
        super(Enemy, self).__init__(xcoord, ycoord)
        self.facing = facing
        