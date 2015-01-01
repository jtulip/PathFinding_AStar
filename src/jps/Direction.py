'''
Created on 19 Dec 2014

@author: jtulip
'''
class Direction:
    
    compass = { "O" :( 0, 0),
                "N" :( 0,-1), 
                "NE":( 1,-1), 
                "E" :( 1, 0), 
                "SE":( 1, 1), 
                "S" :( 0, 1), 
                "SW":(-1, 1), 
                "W" :(-1, 0), 
                "NW":(-1,-1)
              }
    
    inv_compass = { ( 0, 0):"O",
                    ( 0,-1):"N", 
                    ( 1,-1):"NE",
                    ( 1, 0):"E",
                    ( 1, 1):"SE",
                    ( 0, 1):"S",
                    (-1, 1):"SW",
                    (-1, 0):"W",
                    (-1,-1):"NW" 
                  }
    
    directions = ("N", "NE", "E", "SE", "S", "SW", "W", "NW")
    
    diagonals = ("NE", "SE", "SW", "NW")
    
    @staticmethod
    def get_direction(fromPos, toPos):
        x = -1 if toPos[0] - fromPos[0] < 0 else 0 if toPos[0] - fromPos[0] == 0 else 1
        y = -1 if toPos[1] - fromPos[1] < 0 else 0 if toPos[1] - fromPos[1] == 0 else 1
        
        return Direction.inv_compass[(x,y)] 
    
    
    @staticmethod
    def get_neighbours(pos):
        neighbours = {}
        for d in Direction.directions:
            neighbours[d] = (pos[0] + Direction.compass[d][0], pos[1] + Direction.compass[d][1])
        return neighbours
    
    @staticmethod
    def get_neighbour(pos, direction):
        dx = Direction.compass[direction][0]
        dy = Direction.compass[direction][1]
        x = pos[0] + dx
        y = pos[1] + dy
        return (x, y)
    
            
