'''
Created on 19 Dec 2014

@author: jtulip
'''

class Grid:
    
    @staticmethod
    def in_bounds(pos, grid):
        return 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid)
    
    @staticmethod
    def is_passable(pos, grid):
        return Grid.in_bounds(pos, grid) and grid[pos[1]][pos[0]] == 0
        