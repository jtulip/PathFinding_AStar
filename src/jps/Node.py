'''
Created on 22 Dec 2014

@author: jtulip
'''
from jps.Direction import Direction
from jps.Grid import Grid
from jps.Util import JPSUtil

class Node:

    G = 0.6
    H = 0.4
    
    D1 = 1.0
    D2 = 1.4142
    
    
    def __init__(self, selfPos, parent, endPos, grid, cutting = True):
        
        self.pos = selfPos
        self.endPos = endPos 
        self.parent = parent
        self.grid = grid
        
        if parent == None:
            self.cost = 0.0
            self.dirn = Direction.get_direction(self.pos, self.pos)
        else:
            self.cost = parent.get_cost() + parent.calc_cost(selfPos)
            self.dirn = Direction.get_direction(self.parent.get_pos(), self.pos)
            
        self.prox = self.calc_cost(endPos)
        
    def get_pos(self):
        return self.pos
    
    def get_cost(self):
        return self.cost
    
    def get_prox(self):
        return self.prox

    def get_rank(self):
        return Node.G * self.cost + Node.H * self.prox
    
    def get_direction(self):
        return self.dirn
    
    def calc_cost(self, otherPos):
        #cost is calculated as diagonal distance between nodes
        dx = abs(self.pos[0] - otherPos[0])
        dy = abs(self.pos[1] - otherPos[1])
        cost = Node.D1 * (dx + dy) + (Node.D2 - 2*Node.D1) * min(dx,dy)
        return cost
               
    def jump(self, lastPos, direction, endPos, cutting):
        curPos = Direction.get_neighbour(lastPos, direction)
    
        if not Grid.is_passable(curPos, self.grid) :
            return None
        
        if curPos == endPos:
            return curPos
        
        has_forced= JPSUtil.has_forced(curPos, direction, self.grid, cutting) 
        if has_forced:
            return curPos
        
        if direction in JPSUtil.diagonals:
            for cardinal in direction:
                nextPos = self.jump(curPos, cardinal, endPos, cutting)
                if nextPos != None:
                    return curPos
                
        return self.jump(curPos, direction, endPos, cutting)

    def get_successors(self, cutting = True):
        ''' returns a list of successor jump point position tuples (x, y)
        cutting is a boolean that indicates whether corner cutting is allowed'''
        successors = []
        pruned = JPSUtil.prune(self.pos, self.get_direction, self.grid, cutting)
        
        for direction in pruned.keys():
            nextPos = self.jump(self.position, direction, self.endPos, cutting)
            if nextPos != None:
                successors.append(nextPos)
                
        return successors
    
    
