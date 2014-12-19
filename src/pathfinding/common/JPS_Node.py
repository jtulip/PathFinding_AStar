'''
Created on 18 Dec 2014

@author: jtulip
'''

from pathfinding.common.Node import Node

class JPS_Node(Node):
    
    compass = { "N" :( 0,-1), 
                "NE":( 1,-1), 
                "E" :( 1, 0), 
                "SE":( 1, 1), 
                "S" :( 0, 1), 
                "SW":(-1, 1), 
                "W" :(-1, 0), 
                "NW":(-1,-1)}
    
    def __init__(self, position, parentNode, endPosition, grid):
        super().__init__(position, parentNode, endPosition)
        self.grid = grid
        if parentNode != None:
            self.direction = self.get_direction(parentNode.get_position(),self.get_position())
        else:
            self.direction = ""
        
    def get_direction(self, p1, p2): 
        '''get the direction from p1 to p2'''
        if  p1[1] > p2[1] and p1[0] == p2[0]:
            direction = "N"
        elif  p1[1] > p2[1] and p1[0] < p2[0]:
            direction = "NE"
        elif  p1[1] == p2[1] and p1[0] < p2[0]:
            direction = "E"
        elif  p1[1] < p2[1] and p1[0] < p2[0]:
            direction = "SE"
        elif  p1[1] < p2[1] and p1[0] == p2[0]:
            direction = "S"
        elif  p1[1] < p2[1] and p1[0] > p2[0]:
            direction = "SW"
        elif  p1[1] == p2[1] and p1[0] > p2[0]:
            direction = "W"
        elif  p1[1] > p2[1] and p1[0] > p2[0]:
            direction = "NW"
        else:
            direction = ""
            
        return direction

    def get_neighbours(self, pos):
        neighbours = {}
        for i in JPS_Node.compass.keys():
            neighbours[i] = (pos[0]+JPS_Node.compass[i][0], pos[1]+JPS_Node.compass[i][1])
                
        return neighbours
            
    def prune_neighbours(self, neighbours, direction):        
        #first - deal with starting node (no direction)
        if direction == "":
            return neighbours
        
        #otherwise generate the pruned neighbours
        pruned_neighbours = {}
        #get natural neighbours
        if direction in neighbours.keys():
            pruned_neighbours[direction] = (neighbours[direction],"N")
            #add the cardinal directions for diagonal directions
            if len(direction) > 1:
                for cardinal in direction:
                    pruned_neighbours[cardinal] = (neighbours[cardinal],"N")
                
        #now get the forced neighbours
        #first the cardinal directions
        if direction == "N":
            if self.checkForced("W", "NW", neighbours):
                pruned_neighbours["NW"] = (neighbours["NW"],"F")
            if self.checkForced("E", "NE", neighbours):
                pruned_neighbours["NE"] = (neighbours["NE"], "F")
                
        elif direction == "E":
            if self.checkForced("N", "NE", neighbours):
                pruned_neighbours["NE"] = (neighbours["NE"], "F")
            if self.checkForced("S","SE", neighbours):
                pruned_neighbours["SE"] = (neighbours["SE"], "F")
                
        elif direction == "S":
            if self.checkForced("E", "SE", neighbours):
                pruned_neighbours["SE"] = (neighbours["SE"], "F")
            if self.checkForced("W","SW", neighbours):
                pruned_neighbours["SW"] = (neighbours["SW"], "F")
                
        elif direction == "W":
            if self.checkForced("S", "SW", neighbours):
                pruned_neighbours["SW"] = (neighbours["SW"], "F")
            if self.checkForced("N", "NW", neighbours):
                pruned_neighbours["NW"] = (neighbours["NW"], "F")
                
        #now the diagonal directions
        elif direction == "NE":
            if self.checkForced("W", "NW", neighbours):
                pruned_neighbours["NW"] = (neighbours["NW"],"F")
            if self.checkForced("S","SE", neighbours):
                pruned_neighbours["SE"] = (neighbours["SE"], "F")
                
        elif direction == "SE":
            if self.checkForced("N","NE", neighbours):
                pruned_neighbours["NE"] = (neighbours["NE"],"F")
            if self.checkForced("W","SW", neighbours):
                pruned_neighbours["SW"] = (neighbours["SW"], "F")
                
        elif direction == "SW":
            if self.checkForced("N","NW", neighbours):
                pruned_neighbours["NW"] = (neighbours["NW"],"F")
            if self.checkForced("E","SE", neighbours):
                pruned_neighbours["SE"] = (neighbours["SE"], "F")
                
        elif direction == "NW":
            if self.checkForced("E","NE", neighbours):
                pruned_neighbours["NE"] = (neighbours["NE"],"F")
            if self.checkForced("S","SW", neighbours):
                pruned_neighbours["SW"] = (neighbours["SW"], "F")
                
        oob = []
        for p in pruned_neighbours:
            if not self.inBounds(pruned_neighbours[p][0]):
                oob.append(p)
                
        for o in oob:
            pruned_neighbours.pop(o)

        return pruned_neighbours
    
    def isPassable(self, pos):
        if self.inBounds(pos):
            v = self.grid[pos[1]][pos[0]]
            if v == 0:
                return True
        return False 

    def checkForced(self, blocking, forcedir, neighbours):
        b = blocking in neighbours.keys() and not self.isPassable(neighbours[blocking])
        f = forcedir in neighbours.keys() and  self.isPassable(neighbours[forcedir])
        return b and f
    
    def inBounds(self, pos):
        inX = 0 <= pos[1] < len(self.grid)
        inY = 0 <= pos[0] < len(self.grid[0])
        return inX and inY
    
    def jump(self, lastPos, direction, endPos):
        curPos = (lastPos[0] + JPS_Node.compass[direction][0], \
                  lastPos[1] + JPS_Node.compass[direction][1])
        
        if not self.isPassable(curPos) :
            return None
        
        if curPos == endPos:
            return curPos
        
        neighbours = self.get_neighbours(curPos)
        pruned = self.prune_neighbours(neighbours, direction)
        for entry in pruned.values():
            if entry[1] == "F":
                return curPos
        
        if direction in ("NE", "SE", "SW", "NW"):
            for cardinal in direction:
                nextPos = self.jump(curPos, cardinal, endPos)
                if nextPos != None:
                    return curPos
                
        return self.jump(curPos, direction, endPos)
    
    def get_successors(self):
        ''' returns a list of successor tuples (x, y)'''
        successors = []
        neighbours = self.get_neighbours(self.position)
        pruned = self.prune_neighbours(neighbours, self.direction)
        
        for direction in pruned.keys():
            nextPos = self.jump(self.position, direction, self.endPosition)
            if nextPos != None:
                successors.append(nextPos)
                
        return successors
