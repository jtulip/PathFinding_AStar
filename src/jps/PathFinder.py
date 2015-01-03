'''
Created on 22 Dec 2014

@author: jtulip
'''
from jps.BLNonCuttingFinder import Finder
from jps.Node import Node

class PathFinder:
    
    @staticmethod 
    def findPath(startPos, endPos, grid):
        
        finder = Finder(endPos, grid)
        
        #create the starting node
        startNode = Node(startPos, None, endPos, grid)
        
        #initialise OPEN with startNode
        openList = {}
        openList[startPos] = startNode
        currentNode = startNode
        
        #initialise empty CLOSED list 
        closedList = {}
        
        #find the path
        #while currentNode position not the ending position
        curPos = currentNode.get_pos() 
        while curPos != endPos:
            
            #remove current from OPEN
            openList.pop(curPos)
            
            #add current to ClOSED
            closedList[curPos] = currentNode
            
            #get current's successors
            successors = finder.get_successors(currentNode.get_pos(), currentNode.get_direction())
            #print(successors)
        
            #for each of current's successors
            for succ in successors:
                
                #calculate cost for successor
                cost = currentNode.get_cost() + currentNode.calc_cost(succ)
                
                #if successor in OPEN and cost lower than in OPEN
                if succ in openList.keys() and cost < openList[succ].get_cost():
                    #remove successor from OPEN because new path is better
                    openList.pop(succ)
                
                #if successor in CLOSED and cost lower than in CLOSED
                if succ in closedList.keys() and cost < closedList[succ].get_cost():
                    #remove successor from CLOSED
                    closedList.pop(succ)
                    
                #if successor not in OPEN and not in CLOSED
                if succ not in openList.keys() and succ not in closedList.keys():
                    #create a new node (calculating cost
                    successorNode = Node(succ, currentNode, endPos, grid)
                    openList[succ] = successorNode
                
            #print(openList.keys())
            
            currentNode = min(openList.values(), key=lambda node: node.get_rank())
            curPos = currentNode.get_pos()
            #print(curPos)
        
        #reconstruct path tracing backwards from endNode
        path = []
        while currentNode.parent != None:
            path.insert(0,currentNode.get_pos())
            currentNode = currentNode.parent

        return path
        
if __name__ == "__main__":
    
    from jps.Grid import Grid
    from jps.Direction import Direction
    
    grid = [[ 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0 ],
            [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0 ],
            [ 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0 ],
            [ 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0 ],
            [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0 ]]
    
    startPos = (0,10)
    endPos = (11,9)
    print(startPos, endPos)
        
    jumps = PathFinder.findPath(startPos, endPos, grid)
    print(jumps,'\n')
    
    path = []    
    for j in range(len(jumps)-1):
        pos = jumps[j]
        target = jumps[j+1]
        dirn = Direction.get_direction(pos, target)
        
        while pos != target:
            path.append(pos)
            pos = Direction.get_neighbour(pos, dirn)
    
    
    grid[startPos[1]][startPos[0]] = "S"    
    for p in path:
        grid[p[1]][p[0]] = '*'
    for j in jumps:
        grid[j[1]][j[0]] = 'j'
                
    grid[endPos[1]][endPos[0]] = "E"
    
    print(Grid.string(grid))


    