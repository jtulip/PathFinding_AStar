'''
Created on 17 Dec 2014

@author: jtulip
'''
from pathfinding.common.Grid import Grid
from pathfinding.common.Coords import Coords
from pathfinding.common.Node import Node
from pathfinding.common.PathFinder import findPath

if __name__ == '__main__':
    
    g = [[ 0, 0, 1, 0, 0, 0, 0, 1, 0, 0 ],
         [ 0, 0, 1, 0, 0, 0, 0, 1, 0, 0 ],
         [ 0, 0, 1, 0, 0, 0, 0, 1, 0, 0 ],
         [ 0, 0, 1, 0, 0, 1, 0, 1, 0, 0 ],
         [ 0, 0, 1, 0, 0, 1, 0, 1, 0, 0 ],
         [ 0, 0, 1, 0, 0, 1, 0, 1, 0, 0 ],
         [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
         [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
         [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ]]
    
    grid = Grid(g);
    # print(grid)
    
    startPosition = (9,0)
    endPosition = (0,0)
        
    path = findPath(grid, startPosition, endPosition)
    print(path,'\n')
    
    grid.grid[startPosition[1]][startPosition[0]] = "S"    
    for p in path:
        grid.grid[p[1]][p[0]] = '*'
        
    grid.grid[endPosition[1]][endPosition[0]] = "E"
    
    print(grid)