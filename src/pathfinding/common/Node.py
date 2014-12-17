'''
Created on 17 Dec 2014

@author: jtulip
'''

from pathfinding.common.Coords import Coords

class Node:
    
    G = 0.5;
    H = 0.5;
    
    def __init__(self, selfCoords, parentNode, endCoords):
        self.coords = selfCoords
        self.parentNode = parentNode
        if parentNode == None:
            self.cost = 0 
        else: 
            self.cost = parentNode.get_cost() + parentNode.calc_cost_to_position(self.coords.get_position())
            
        self.prox = self.calc_cost(endCoords)
     
    def get_position(self):
        return self.coords.get_position()   
        
    def calc_cost(self, otherCoords):
        c = self.coords.diag_dist(otherCoords.get_position())
        return c
        
    def calc_cost_to_position(self, position):
        c = self.coords.diag_dist(position)
        return c
        
    def get_cost(self):
        return self.cost
    
    def get_prox(self):
        return self.prox

    def get_rank(self):
        return Node.G * self.cost + Node.H * self.prox
    
    def get_neighbours(self, grid):
        minX = self.coords.x - 1
        maxX = self.coords.x + 1
        minY = self.coords.y - 1
        maxY = self.coords.y + 1
        
        #print(self.get_position(),(minX,maxX,minY,maxY),grid.maxX, grid.maxY)
        
        neighbours = []
        #top row of neighbours
        if minY >= 0:
            if grid.grid[minY][self.coords.x] != 1:
                neighbours.append((self.coords.x, minY))
            if minX >= 0 and grid.grid[minY][minX] != 1:
                neighbours.append((minX,minY))
            if maxX <= grid.maxX and grid.grid[minY][maxX] != 1:
                neighbours.append((maxX, minY))
        #middle row
        if minX >= 0 and grid.grid[self.coords.y][minX] != 1:
                neighbours.append((minX, self.coords.y))
        if maxX <= grid.maxX and grid.grid[self.coords.y][maxX] != 1:
            neighbours.append((maxX, self.coords.y))
        #bottom row
        if maxY <= grid.maxY:
            if grid.grid[maxY][self.coords.x] != 1:
                neighbours.append((self.coords.x, maxY))
            if minX >= 0 and grid.grid[maxY][minX] != 1:
                neighbours.append((minX, maxY))
            if maxX <= grid.maxX and grid.grid[maxY][maxX] != 1:
                neighbours.append((maxX, maxY))
        
        #print(neighbours,'\n')
        return neighbours
        