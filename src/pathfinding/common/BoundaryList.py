'''
Created on 17 Dec 2014

@author: jtulip
'''
from pathfinding.common.Grid import Grid

class BoundaryList:
    
    def __init__(self, grid):
        if not isinstance(grid, Grid):
            raise RuntimeError("invalid grid")
        
        self.hlist = []
        self.vlist = []
        
        # calculate the horizontal boundary lists
        for row in range(grid.maxY):
            sense = 0                        #0 represents open on grid
            rlist = []
            for col in range(grid.maxX):
                if grid.grid[row][col] != sense:
                    rlist.append(col)
                    sense = grid.grid[row][col]
            if sense == 0:
                rlist.append(grid.maxX)
            self.hlist.append(rlist)
    
        # calculate the vertical boundary lists
        for col in range(grid.maxX):
            sense = 0                        #0 represents open on grid
            clist = []
            for row in range(grid.maxY):
                if grid.grid[row][col] != sense:
                    clist.append(row)
                    sense = grid.grid[row][col]
            if sense == 0:
                clist.append(grid.maxY)
            self.vlist.append(clist)
    
