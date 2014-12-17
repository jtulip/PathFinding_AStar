'''
Created on 17 Dec 2014

@author: jtulip
'''
from pathfinding.common.Node import Node
from pathfinding.common.Coords import Coords

def findPath(grid, startCoords, endCoords):
    
    #initialise OPEN with startNode
    startNode = Node(startCoords, None, endCoords)    
    openList = {}    
    openList[startNode.get_position()] = startNode
    
    #initialise CLOSED list as empty
    closedList = {}
    
    currentNode = startNode
    #while current Node not at end coords
    while currentNode.coords != endCoords:
        #remove current from OPEN
        openList.pop(currentNode.get_position())
        #add current to CLOSED
        closedList[currentNode.get_position()] = currentNode
        
        #get current's neighbours
        neighbours = currentNode.get_neighbours(grid)
        
        #for each neighbour of current
        for neighbour in neighbours:
            cost = currentNode.get_cost() + currentNode.calc_cost_to_position(neighbour)
            #if neighbour in OPEN and cost lower than in OPEN
            if neighbour in openList.keys() and cost < openList[neighbour].get_cost():
                #remove neighbour from OPEN because new path is better
                openList.pop(neighbour)
            #if neighbour in CLOSED and cost lower than in CLOSED
            if neighbour in closedList.keys() and cost < closedList[neighbour].get_cost():
                #remove neighbour from CLOSED
                closedList.pop(neighbour)
            #if neighbour not in OPEN and not in CLOSED
            if neighbour not in openList.keys() and neighbour not in closedList.keys():
                #create a new node (calculating cost
                neighbourNode = Node(Coords(neighbour[0], neighbour[1]), currentNode, endCoords)
                openList[neighbour] = neighbourNode
            
        currentNode = min(openList.values(), key=lambda x: x.get_rank())
        
    path = []
    while currentNode.parentNode != None:
        path.insert(0,currentNode.get_position())
        currentNode = currentNode.parentNode
        
    return path
        