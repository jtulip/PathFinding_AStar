'''
Created on 18 Dec 2014

@author: jtulip
'''
from pathfinding.common.JPS_PathFinder import findPath


def printGrid(grid):
    s = '[['
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            s = s + ' ' + str(grid[row][col]) + ','
        s = s.rstrip(',')
        s = s + ' ],\n ['
    s = s.rstrip(',\n [')
    s = s + ']\n'
    
    print(s)


if __name__ == '__main__':
    
    grid = [[ 0, 0, 1, 0, 0, 0, 0, 1, 0, 0 ],
         [ 0, 0, 1, 0, 0, 0, 0, 1, 0, 0 ],
         [ 0, 0, 1, 0, 0, 0, 0, 1, 0, 0 ],
         [ 0, 0, 1, 0, 0, 1, 0, 1, 0, 0 ],
         [ 0, 0, 1, 0, 0, 1, 0, 1, 0, 0 ],
         [ 0, 0, 1, 0, 0, 1, 0, 1, 0, 0 ],
         [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
         [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
         [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ]]
    
    #printGrid(grid)
    
    startPosition = (9,0)
    endPosition = (0,0)
    
        
    path = findPath(grid, startPosition, endPosition)
    print(path,'\n')
    
    grid[startPosition[1]][startPosition[0]] = "S"    
    for p in path:
        grid[p[1]][p[0]] = '*'
        
    grid[endPosition[1]][endPosition[0]] = "E"
    
    printGrid(grid)
    
