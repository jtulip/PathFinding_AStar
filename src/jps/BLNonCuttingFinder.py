'''
Created on 19 Dec 2014

@author: jtulip
'''
from jps.Direction import Direction
from jps.BoundaryList import BoundaryList
from math import sqrt


class Finder:
    
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
    
    leftDict = { "N":"W", "E":"N", "S":"E", "W":"S" }
    
    rightDict = { "N":"E", "E":"S", "S":"W", "W":"N" }

            
    def __init__(self, endPos, grid):
        self.endPos = endPos
        self.grid = grid
        self.blist = BoundaryList(grid)
        
        #print(self.blist.hlist)
        #print(self.blist.vlist)

            
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

    
    def is_reachable(self, pos, dirn):
        npos = Direction.get_neighbour(pos, dirn)
        in_bounds = self.in_bounds(npos) 
        is_open = False
        if in_bounds:
            is_open = self.is_passable(npos)
            if dirn in Direction.diagonals:
                d1, d2 = dirn 
                p1 = Direction.get_neighbour(pos, d1)
                p2 = Direction.get_neighbour(pos, d2)
                is_open = is_open and (self.is_passable(p1) and self.is_passable(p2) )
                
        return in_bounds and is_open

    
    def check_forced(self, pos, blockdir, forcedir):
        blocked = not self.is_reachable(pos, blockdir)
        
        forced = self.is_reachable(pos, forcedir)
        
        return blocked and forced

            
    def get_forced(self, pos, dirn):
        pm = self.forced_params[dirn]
        #b_left = pm[0], f_left_cardinal = pm[1], f_left_diagonal = pm[2], 
        #b_right = pm[3], f_right_cardinal = pm[4], f_right_diagonal = pm[5],

        forced = {}
        if len(pm) > 0:
            if self.check_forced(pos, pm[0], pm[1]):
                forced[pm[1]] = Direction.get_neighbour(pos, pm[1])
                
            if self.check_forced(pos, pm[0], pm[2]):
                forced[pm[2]] = Direction.get_neighbour(pos, pm[2])
                
            if self.check_forced(pos, pm[3], pm[4]):
                forced[pm[4]]= Direction.get_neighbour(pos, pm[4])
                
            if self.check_forced(pos, pm[3], pm[5]):
                forced[pm[5]]= Direction.get_neighbour(pos, pm[5])
                
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

    
    def distance(self, fromPos, toPos, direction):
        if direction in ("E", "W"):
            return abs(fromPos[0] - toPos[0])
        elif direction in ("N", "S"):
            return abs(fromPos[1] - toPos[1])
        else:
            return abs(sqrt((fromPos[0]-toPos[0])*(fromPos[0]-toPos[0])+(fromPos[1]-toPos[1])*(fromPos[1]-toPos[1])))

        
    def getNextJump(self, center, direction):
        
        center_boundary_pos = self.blist.get_next_closed_boundary_pos(center, direction)
        
        left_neighbour = Direction.get_neighbour(center, self.leftDict[direction])
        left_open_pos = self.blist.get_next_open_boundary_pos(left_neighbour, direction)        
        if left_open_pos != None:
            if self.distance(center, center_boundary_pos, direction) > self.distance(left_neighbour, left_open_pos, direction):
                return Direction.get_position(center, direction, self.distance(left_neighbour, left_open_pos, direction))
        
        right_neighbour = Direction.get_neighbour(center, self.rightDict[direction])
        right_open_pos = self.blist.get_next_open_boundary_pos(right_neighbour, direction)
        if right_open_pos != None:
            if self.distance(center, center_boundary_pos, direction) > self.distance(right_neighbour, right_open_pos, direction):
                return Direction.get_position(center, direction, self.distance(right_neighbour, right_open_pos, direction))
        
        return None
        
        
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
                nextPosBL = self.getNextJump(curPos, cardinal)
                print(nextPos, nextPosBL)
                
                if nextPos != None:
                    return curPos
                
        nextPos = self.jump(curPos, direction)
        nextPosBL = self.getNextJump(curPos, direction)
        print(nextPos, nextPosBL)
        
        return self.jump(curPos, direction)


    def get_successors(self, pos, dirn):
        ''' returns a list of successor jump point position tuples (x, y)'''
        successors = []
        pruned = self.prune(pos, dirn)
        
        for direction in pruned.keys():
            nextPos = self.jump(pos, direction)
            if nextPos != None:
                successors.append(nextPos)
                
        return successors
        
      
