'''
Created on 18 Dec 2014

@author: jtulip
'''
from pathfinding.common.JPS_Node import JPS_Node

def findPath(grid, startPosition, endPosition):
    
    #initialise OPEN with startNode
    startNode = JPS_Node(startPosition, None, endPosition, grid)    
    openList = {}    
    openList[startNode.get_position()] = startNode
    
    #initialise CLOSED list as empty
    closedList = {}
    
    #while current Node not at end coords
    currentNode = startNode
    while currentNode.position != endPosition:
        
        #remove current from OPEN
        openList.pop(currentNode.get_position())
        
        #add current to CLOSED
        closedList[currentNode.get_position()] = currentNode
        
        #get current's successors
        successors = currentNode.get_successors()
        
        #for each successor of current
        for successor in successors:
            
            #calculate cost for successor
            cost = currentNode.get_cost() + currentNode.calc_cost(successor)
            
            #if successor in OPEN and cost lower than in OPEN
            if successor in openList.keys() and cost < openList[successor].get_cost():
                #remove successor from OPEN because new path is better
                openList.pop(successor)
                
            #if successor in CLOSED and cost lower than in CLOSED
            if successor in closedList.keys() and cost < closedList[successor].get_cost():
                #remove successor from CLOSED
                closedList.pop(successor)
                
            #if successor not in OPEN and not in CLOSED
            if successor not in openList.keys() and successor not in closedList.keys():
                #create a new node (calculating cost
                successorNode = JPS_Node(successor, currentNode, endPosition)
                openList[successor] = successorNode
            
        currentNode = min(openList.values(), key=lambda node: node.get_rank())
        
    path = []
    while currentNode.parentNode != None:
        path.insert(0,currentNode.get_position())
        currentNode = currentNode.parentNode
    
    for pos in closedList.keys():
        grid[pos[1]][pos[0]] = 'c'
        
    return path
        