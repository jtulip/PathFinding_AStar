'''
Created on 18 Dec 2014

@author: jtulip
'''
from pathfinding.common.JPS_PathFinder import findPath
from pathfinding.common.JPS_Node import JPS_Node


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
    
        
    jumps = findPath(grid, startPosition, endPosition)
    print(jumps,'\n')
    
    path = []    
    for j in range(len(jumps)-1):
        pos = jumps[j]
        target = jumps[j+1]
        dirn = JPS_Node.get_direction(pos, target)
        
        while pos != target:
            path.append(pos)
            pos = JPS_Node.get_neighbour(pos, dirn)
    
    
    grid[startPosition[1]][startPosition[0]] = "S"    
    for p in path:
        grid[p[1]][p[0]] = '*'
    for j in jumps:
        grid[j[1]][j[0]] = 'j'
        
        
    grid[endPosition[1]][endPosition[0]] = "E"
    
    printGrid(grid)
    
