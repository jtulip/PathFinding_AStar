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
        

    @staticmethod
    def check_forced(pos, blockdir, forcedir, grid):
        bPos = Direction.get_neighbour(pos, blockdir)
        blocked = not Grid.is_passable(bPos, grid)
        
        fPos = Direction.get_neighbour(pos, forcedir)
        forced = Grid.is_passable(fPos, grid)
        
        return blocked and forced

            
    @staticmethod
    def get_forced(pos, b_left, f_left, b_right, f_right, grid):
        forced = {}
        if JPSUtil.check_forced(pos, b_left, f_left, grid):
            forced[f_left] = Direction.get_neighbour(pos, f_left)
            
        if JPSUtil.check_forced(pos, b_right, f_right, grid):
            forced[f_right]= Direction.get_neighbour(pos, f_right)
            
        return forced
       
    @staticmethod
    def prune(pos, dirn, grid, cut):
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
        if dirn in ("NE", "SE", "SW", "NW" ) and cut == False:
            forced = {}            
        else:
            pm = JPSUtil.forced_params[dirn]
            forced = JPSUtil.get_forced(pos, pm[0], pm[1], pm[2], pm[3], grid)
            for fn in forced:
                pruned[fn] = forced[fn]
                
        if len(forced) > 0:
            has_forced = True
        
        return (has_forced, pruned)

        
      
