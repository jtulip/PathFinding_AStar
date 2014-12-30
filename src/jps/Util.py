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
        "NW": ("N", "NW", "W") }  
        
    diagonals = ("NE", "SE", "SW", "NW")
    
    @staticmethod
    def check_forced(pos, blockdir, forcedir, grid):
        bPos = Direction.get_neighbour(pos, blockdir)
        blocked = not Grid.is_passable(bPos, grid)
        
        fPos = Direction.get_neighbour(pos, forcedir)
        forced = Grid.is_passable(fPos, grid)
        
        return blocked and forced

            
    @staticmethod
    def get_forced(pos, dirn, grid, cutting = True):
        pm = JPSUtil.forced_params[dirn]
        #b_left = pm[0], f_left = pm[1], b_right = pm[2], f_right = pm[3]

        forced = {}
        if not (dirn in JPSUtil.diagonals and cutting == False):
            if JPSUtil.check_forced(pos, pm[0], pm[1], grid):
                forced[pm[1]] = Direction.get_neighbour(pos, pm[1])
                
            if JPSUtil.check_forced(pos, pm[2], pm[3], grid):
                forced[pm[3]]= Direction.get_neighbour(pos, pm[3])
            
        return forced
    
    @staticmethod
    def has_forced(pos, direction, grid, cutting = True):
        pm = JPSUtil.forced_params[direction]
        forced = JPSUtil.get_forced(pos, direction, grid, cutting)
        hasforced = len(forced) > 0
        return hasforced
       
    @staticmethod
    def prune(pos, dirn, grid, cutting = True):
        #first - deal with starting node (no direction)
        has_forced = False
        if dirn == "O":
            return (has_forced, Direction.get_neighbours(pos))
        
        #otherwise generate the pruned neighbours
        pruned = {}
        #get natural neighbours
        for nat in JPSUtil.naturals[dirn]:
            pruned[nat] = Direction.get_neighbour(pos, nat)
            
        #get forced neighbours
        forced = JPSUtil.get_forced(pos, dirn, grid, cutting)
        for fn in forced:
            pruned[fn] = forced[fn]
                        
        return pruned

        
      
