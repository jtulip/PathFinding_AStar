'''
Created on 19 Dec 2014

@author: jtulip
'''

class Grid:
    
    @staticmethod
    def in_bounds(pos, grid):
        inX = 0 <= pos[0] < len(grid[0])
        inY = 0 <= pos[1] < len(grid)
        return inX and inY
    
    @staticmethod
    def is_passable(pos, grid):
        in_bounds = Grid.in_bounds(pos, grid) 
        is_open = False
        if in_bounds:
            x = grid[pos[1]][pos[0]]
            is_open = x == 0
        return in_bounds and is_open
    
    @staticmethod
    def string(grid):
        s = '[['
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                s = s + ' ' + str(grid[row][col]) + ' '
            s = s.rstrip(' ')
            s = s + ' ] \n ['
        s = s.rstrip(' \n [')
        s = s + ']\n'
    
        return s 


        