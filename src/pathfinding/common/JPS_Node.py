'''
Created on 18 Dec 2014

@author: jtulip
'''

from pathfinding.common.Node import Node

class JPS_Node(Node):
    
    def __init__(self, position, parentNode, endPosition, grid):
        super().__init__(position, parentNode, endPosition)
        self.grid = grid
        if parentNode != None:
            self.direction = self.get_direction(parentNode.get_position(),self.get_position())
        else:
            self.direction = ""

    def get_direction(self,p1,p2): 
        '''get the direction from p1 to p2'''
        if  p1[1] > p2[1] and p1[0] == p2[0]:
            direction = "N"
        elif  p1[1] > p2[1] and p1[0] < p2[0]:
            direction = "NE"
        elif  p1[1] == p2[1] and p1[0] < p2[0]:
            direction = "E"
        elif  p1[1] < p2[1] and p1[0] < p2[0]:
            direction = "SE"
        elif  p1[1] < p2[1] and p1[0] == p2[0]:
            direction = "S"
        elif  p1[1] < p2[1] and p1[0] > p2[0]:
            direction = "SW"
        elif  p1[1] == p2[1] and p1[0] > p2[0]:
            direction = "W"
        elif  p1[1] > p2[1] and p1[0] > p2[0]:
            direction = "NW"
        else:
            direction = ""
            
        return direction

    def get_successors(self):
        neighbours = super().get_neighbours(self.grid)
        
        return neighbours
    
