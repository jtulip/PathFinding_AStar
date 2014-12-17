'''
Created on 17 Dec 2014

@author: jtulip
'''
class Coords:
    
    D1 = 1.0
    D2 = 1.4142

    def __init__(self, x, y):
        """ create a Coords

      x - the x coordinate
      y - the y coordinate"""

        self.x = x;
        self.y = y;
    
        
    def get_position(self):
        return (self.x, self.y)

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def diag_dist(self, otherCoordTuple):
        dx = abs(self.x - otherCoordTuple[0])
        dy = abs(self.y - otherCoordTuple[1])
        di = Coords.D1 * (dx + dy) + (Coords.D2 - 2*Coords.D1) * min(dx,dy)
        return di

