'''
Created on 17 Dec 2014

@author: jtulip
'''
class Grid:
    
    def __init__(self, grid):
        self.grid = grid
        self.maxY = len(grid)-1
        self.maxX = len(grid[0])-1
        
        if self.maxY == 0 or self.maxX == 0:
            raise RuntimeError("grid must be 2D")
        
    def __str__(self): 
        s = '[['
        for row in range(self.maxY+1):
            for col in range(self.maxX+1):
                s = s + ' ' + str(self.grid[row][col]) + ','
            s = s.rstrip(',')
            s = s + ' ],\n ['
        s = s.rstrip(',\n [')
        s = s + ']\n'
        return s   
