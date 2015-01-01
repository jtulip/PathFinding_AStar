'''
Created on 19 Dec 2014

@author: jtulip
'''
from jps.Grid import Grid
from jps.Direction import Direction

class JPSUtil:
    
    forced_params = {
        "N" : ("SW", "W", "NW", "SE", "E", "NE"),
        "E" : ("NW", "N", "NE", "SW", "S", "SE"),
        "S" : ("NE", "E", "SE", "NW", "W", "SW"),
        "W" : ("SE", "S", "SW", "NE", "N", "NW"),
        "NE": (),
        "SE": (),
        "SW": (),
        "NW": () }  
    
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
    def is_reachable(pos, dirn, grid):
        npos = Direction.get_neighbour(pos, dirn)
        in_bounds = JPSUtil.in_bounds(npos, grid) 
        is_open = False
        if in_bounds:
            is_open = JPSUtil.is_passable(npos, grid)
            if dirn in Direction.diagonals:
                d1, d2 = dirn 
                p1 = Direction.get_neighbour(pos, d1)
                p2 = Direction.get_neighbour(pos, d2)
                is_open = is_open and (JPSUtil.is_passable(p1,grid) and JPSUtil.is_passable(p2,grid) )
                
        return in_bounds and is_open
    
    @staticmethod
    def check_forced(pos, blockdir, forcedir, grid):
        blocked = not JPSUtil.is_reachable(pos, blockdir, grid)
        
        forced = JPSUtil.is_reachable(pos, forcedir, grid)
        
        return blocked and forced

            
    @staticmethod
    def get_forced(pos, dirn, grid):
        pm = JPSUtil.forced_params[dirn]
        #b_left = pm[0], f_left_cardinal = pm[1], f_left_diagonal = pm[2], 
        #b_right = pm[3], f_right_cardinal = pm[4], f_right_diagonal = pm[5],

        forced = {}
        if len(pm) > 0:
            if JPSUtil.check_forced(pos, pm[0], pm[1], grid):
                forced[pm[1]] = Direction.get_neighbour(pos, pm[1])
                
            if JPSUtil.check_forced(pos, pm[0], pm[2], grid):
                forced[pm[2]] = Direction.get_neighbour(pos, pm[2])
                
            if JPSUtil.check_forced(pos, pm[3], pm[4], grid):
                forced[pm[4]]= Direction.get_neighbour(pos, pm[4])
                
            if JPSUtil.check_forced(pos, pm[3], pm[5], grid):
                forced[pm[5]]= Direction.get_neighbour(pos, pm[5])
                
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
        
      
