'''
Created on 19 Dec 2014

@author: jtulip
'''
from jps.Direction import Direction

class Finder:
    
    forced_params = {
        "N" : ("W", "NW", "E", "NE"),
        "E" : ("N", "NE", "S", "SE"),
        "S" : ("E", "SE", "W", "SW"),
        "W" : ("S", "SW", "N", "NW"),
        "NE": ("W", "NW", "S", "SE"),
        "SE": ("N", "NE", "W", "SW"),
        "SW": ("E", "SE", "N", "NW"),
        "NW": ("S", "SW", "E", "NE") }  
    
    naturals = {
        "N" : ("N"),
        "E" : ("E"),
        "S" : ("S"),
        "W" : ("W"),
        "NE": ("N", "NE", "E"),
        "SE": ("S", "SE", "E"),
        "SW": ("S", "SW", "W"),
        "NW": ("N", "NW", "W"),
        "O" : ("N", "NE", "E", "SE", "S", "SW", "W", "NW" )}  
    
    def __init__(self, endPos, grid):
        self.endPos = endPos
        self.grid = grid
            
    def in_bounds(self, pos):
        inX = 0 <= pos[0] < len(self.grid[0])
        inY = 0 <= pos[1] < len(self.grid)
        return inX and inY
    
    def is_passable(self, pos):
        in_bounds = self.in_bounds(pos) 
        is_open = False
        if in_bounds:
            is_open = self.grid[pos[1]][pos[0]] == 0
        return in_bounds and is_open
    
    def check_forced(self, pos, blockdir, forcedir):
        bPos = Direction.get_neighbour(pos, blockdir)
        blocked = not self.is_passable(bPos)
        
        fPos = Direction.get_neighbour(pos, forcedir)
        forced = self.is_passable(fPos)
        
        return blocked and forced

            
    def get_forced(self, pos, dirn):
        pm = self.forced_params[dirn]
        #b_left = pm[0], f_left = pm[1], b_right = pm[2], f_right = pm[3]

        forced = {}
        if self.check_forced(pos, pm[0], pm[1]):
            forced[pm[1]] = Direction.get_neighbour(pos, pm[1])
            
        if self.check_forced(pos, pm[2], pm[3]):
            forced[pm[3]]= Direction.get_neighbour(pos, pm[3])
            
        return forced
    
    def has_forced(self, pos, direction):
        forced = self.get_forced(pos, direction)
        hasforced = len(forced) > 0
        return hasforced
       
    def prune(self, pos, dirn):
        #first - deal with starting node (no direction)
        if dirn == "O":
            return Direction.get_neighbours(pos)
        
        #otherwise generate the pruned neighbours
        pruned = {}
        #get natural neighbours
        for nat in self.naturals[dirn]:
            pruned[nat] = Direction.get_neighbour(pos, nat)
            
        #get forced neighbours
        forced = self.get_forced(pos, dirn)
        for fn in forced:
            pruned[fn] = forced[fn]
                        
        return pruned

    def jump(self, lastPos, direction):
        curPos = Direction.get_neighbour(lastPos, direction)
    
        if not self.is_passable(curPos) :
            return None
        
        if curPos == self.endPos:
            return curPos
        
        has_forced= self.has_forced(curPos, direction) 
        if has_forced:
            return curPos
        
        if direction in Direction.diagonals:
            for cardinal in direction:
                nextPos = self.jump(curPos, cardinal)
                if nextPos != None:
                    return curPos
                
        return self.jump(curPos, direction)

    def get_successors(self, pos, dirn):
        ''' returns a list of successor jump point position tuples (x, y)
        cutting is a boolean that indicates whether corner cutting is allowed'''
        successors = []
        pruned = self.prune(pos, dirn)
        
        for direction in pruned.keys():
            nextPos = self.jump(pos, direction)
            if nextPos != None:
                successors.append(nextPos)
                
        return successors
        
      
