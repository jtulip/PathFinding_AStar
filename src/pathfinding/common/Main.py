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
    
    startCoords = Coords(9,0)
    endCoords = Coords(0,0)
        
    path = findPath(grid, startCoords, endCoords)
    print(path,'\n')
    
    grid.grid[startCoords.y][startCoords.x] = "S"    
    for p in path:
        grid.grid[p[1]][p[0]] = '*'
        
    grid.grid[endCoords.y][endCoords.x] = "E"
    
    print(grid)