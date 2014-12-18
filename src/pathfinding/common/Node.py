'''
Created on 17 Dec 2014

@author: jtulip
'''

class Node:
    
    G = 0.6
    H = 0.4
    
    D1 = 1.0
    D2 = 1.4142
    
    def __init__(self, position, parentNode, endPosition):
        self.position = position
        self.endPosition = endPosition
        self.parentNode = parentNode
        if parentNode == None:
            self.cost = 0 
        else: 
            self.cost = parentNode.get_cost() + parentNode.calc_cost(self.position)
            
        self.prox = self.calc_cost(endPosition)
     
    def get_position(self):
        return self.position  
        
    def calc_cost(self, otherPosition):
        #cost is calculated as diagonal distance between nodes
        dx = abs(self.position[0] - otherPosition[0])
        dy = abs(self.position[1] - otherPosition[1])
        cost = Node.D1 * (dx + dy) + (Node.D2 - 2*Node.D1) * min(dx,dy)
        return cost
        
    def get_cost(self):
        return self.cost
    
    def get_prox(self):
        return self.prox

    def get_rank(self):
        return Node.G * self.cost + Node.H * self.prox
    
    def get_neighbours(self, grid):
        minX = self.position[0] - 1
        maxX = self.position[0] + 1
        minY = self.position[1] - 1
        maxY = self.position[1] + 1
        
        #print(self.get_position(),(minX,maxX,minY,maxY),len(grid[0]), len(grid))
        
        neighbours = []
        #top row of neighbours
        if minY >= 0:
            neighbours.append((self.position[0], minY))
            if minX >= 0:
                neighbours.append((minX,minY))
            if maxX < len(grid[0]):
                neighbours.append((maxX, minY))
        #middle row
        if minX >= 0:
            neighbours.append((minX, self.position[1]))
        if maxX < len(grid[0]):
            neighbours.append((maxX, self.position[1]))
        #bottom row
        if maxY < len(grid):
            neighbours.append((self.position[0], maxY))
            if minX >= 0:
                neighbours.append((minX, maxY))
            if maxX < len(grid[0]):
                neighbours.append((maxX, maxY))
        
        #print(neighbours,'\n')
        return sorted(neighbours, key=lambda x : (x[1],x[0]))
        