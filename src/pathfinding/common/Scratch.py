'''
Created on 18 Dec 2014

@author: jtulip
'''

from pathfinding.common.JPS_Node import JPS_Node
from pathfinding.common.JPS_PathFinder import findPath

def printGrid(grid):
    s = '[['
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            s = s + ' ' + str(grid[row][col]) + ' '
        s = s.rstrip(' ')
        s = s + ' ] \n ['
    s = s.rstrip(' \n [')
    s = s + ']\n'
    
    print(s)

grid = [[ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0 ],
        [ 0, 0, 1, 0, 0, 0, 1, 0, 0, 0 ],
        [ 0, 0, 1, 0, 0, 0, 1, 0, 0, 0 ],
        [ 0, 0, 1, 0, 0, 0, 1, 0, 0, 0 ],
        [ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 ]]


startPos = (0,8)
endPos = (9,0)
path = findPath(grid, startPos, endPos)
print(path)

grid[startPos[1]][startPos[0]] = 'S'

for j in path:
    grid[j[1]][j[0]] = 'j'
    
grid[endPos[1]][endPos[0]] = 'E'


printGrid(grid)
