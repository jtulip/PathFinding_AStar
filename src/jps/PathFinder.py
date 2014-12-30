'''
Created on 22 Dec 2014

@author: jtulip
'''
from jps.Node import Node

class PathFinder:
    
    @staticmethod 
    def findPath(startPos, endPos, grid, corner_cutting = True):
        
        #create th4e starting node
        startNode = Node(startPos, None, endPos, grid)
        
        #initialise OPEN with startNode
        openList = {}
        openList[startPos] = startNode
        
        #initialise empty CLOSED list 
        closedList = {}
        
        #find the path
        #while currentNode position not the ending position
        currentNode = startNode
        while currentNode.get_pos() != endPos:
            
            #remove current from OPEN
            openList.pop(currentNode.get_pos())
            
            #add current to ClOSED
            closedList[currentNode.get_pos()] = currentNode
            
            #for each of current's successors
        
        
