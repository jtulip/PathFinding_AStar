'''
Created on 22 Dec 2014

@author: jtulip
'''

class Node:

    G = 0.6
    H = 0.4
    
    D1 = 1.0
    D2 = 1.4142
    
    
    def __init__(self, selfPos, parent, endPos, grid):
        
        self.pos = selfPos
        self.endPos = endPos 
        self.parent = parent
        self.grid = grid
        
        if parent == None:
            self.cost = 0.0
        else:
            self.cost = parent.get_cost() + parent.calc_cost(selfPos)
            
        self.prox = self.calc_cost(endPos)
        
    def get_pos(self):
        return self.pos
    
    def get_cost(self):
        return self.cost
    
    def get_prox(self):
        return self.prox

    def get_rank(self):
        return Node.G * self.cost + Node.H * self.prox
    
    def calc_cost(self, otherPos):
        #cost is calculated as diagonal distance between nodes
        dx = abs(self.pos[0] - otherPos[0])
        dy = abs(self.pos[1] - otherPos[1])
        cost = Node.D1 * (dx + dy) + (Node.D2 - 2*Node.D1) * min(dx,dy)
        return cost
               
