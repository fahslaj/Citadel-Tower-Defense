'''
Created on Jun 12, 2014

@author: fahslaj
'''

''' The base class for a Citadel tower '''
class Citadel(object):
    
    def initialize(self):
        pass


    def __init__(self, cost = 0, power = 5):
        '''
        Constructor
        '''
        self.initialize()
        self.cost = cost
        self.power = power
        self.level = 0