'''
Created on 19 Dec 2014

@author: jtulip
'''
from jps.Grid import Grid
from jps.Direction import Direction

class JPSUtil:
    
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
            
    @staticmethod
    def in_bounds(pos, grid):
        inX = 0 <= pos[0] < len(grid[0])
        inY = 0 <= pos[1] < len(grid)
        return inX and inY
    
    @staticmethod
    def is_passable(pos, grid):
        in_bounds = JPSUtil.in_bounds(pos, grid) 
        is_open = False
        if in_bounds:
            x = grid[pos[1]][pos[0]]
            is_open = x == 0
        return in_bounds and is_open
    
    @staticmethod
    def check_forced(pos, blockdir, forcedir, grid):
        bPos = Direction.get_neighbour(pos, blockdir)
        blocked = not JPSUtil.is_passable(bPos, grid)
        
        fPos = Direction.get_neighbour(pos, forcedir)
        forced = JPSUtil.is_passable(fPos, grid)
        
        return blocked and forced

            
    @staticmethod
    def get_forced(pos, dirn, grid):
        pm = JPSUtil.forced_params[dirn]
        #b_left = pm[0], f_left = pm[1], b_right = pm[2], f_right = pm[3]

        forced = {}
        if JPSUtil.check_forced(pos, pm[0], pm[1], grid):
            forced[pm[1]] = Direction.get_neighbour(pos, pm[1])
            
        if JPSUtil.check_forced(pos, pm[2], pm[3], grid):
            forced[pm[3]]= Direction.get_neighbour(pos, pm[3])
            
        return forced
    
    @staticmethod
    def has_forced(pos, direction, grid):
        forced = JPSUtil.get_forced(pos, direction, grid)
        hasforced = len(forced) > 0
        return hasforced
       
    @staticmethod
    def prune(pos, dirn, grid):
        #first - deal with starting node (no direction)
        if dirn == "O":
            return Direction.get_neighbours(pos)
        
        #otherwise generate the pruned neighbours
        pruned = {}
        #get natural neighbours
        for nat in JPSUtil.naturals[dirn]:
            pruned[nat] = Direction.get_neighbour(pos, nat)
            
        #get forced neighbours
        forced = JPSUtil.get_forced(pos, dirn, grid)
        for fn in forced:
            pruned[fn] = forced[fn]
                        
        return pruned

    @staticmethod
    def jump(lastPos, direction, endPos, grid):
        curPos = Direction.get_neighbour(lastPos, direction)
    
        if not JPSUtil.is_passable(curPos, grid) :
            return None
        
        if curPos == endPos:
            return curPos
        
        has_forced= JPSUtil.has_forced(curPos, direction, grid) 
        if has_forced:
            return curPos
        
        if direction in Direction.diagonals:
            for cardinal in direction:
                nextPos = JPSUtil.jump(curPos, cardinal, endPos, grid)
                if nextPos != None:
                    return curPos
                
        return JPSUtil.jump(curPos, direction, endPos, grid)

    @staticmethod
    def get_successors(pos, dirn, endPos, grid):
        ''' returns a list of successor jump point position tuples (x, y)
        cutting is a boolean that indicates whether corner cutting is allowed'''
        successors = []
        pruned = JPSUtil.prune(pos, dirn, grid)
        
        for direction in pruned.keys():
            nextPos = JPSUtil.jump(pos, direction, endPos, grid)
            if nextPos != None:
                successors.append(nextPos)
                
        return successors
        
      
