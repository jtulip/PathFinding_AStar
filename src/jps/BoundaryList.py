'''
Created on 17 Dec 2014

@author: jtulip
'''

class BoundaryList:
    
    def __init__(self, grid):
        self.hlist = []
        self.vlist = []
        
        # calculate the horizontal boundary lists
        for row in range(len(grid)):
            sense = 0                        #0 represents open on grid
            rlist = []
            for col in range(len(grid[0])):
                if grid[row][col] != sense:
                    rlist.append(col)
                    sense = grid[row][col]
            if sense == 0:
                rlist.append(len(grid[0]))
            self.hlist.append(rlist)
    
        # calculate the vertical boundary lists
        for col in range(len(grid[0])):
            sense = 0                        #0 represents open on grid
            clist = []
            for row in range(len(grid)):
                if grid[row][col] != sense:
                    clist.append(row)
                    sense = grid[row][col]
            if sense == 0:
                clist.append(len(grid))
            self.vlist.append(clist)
    
    def get_next_closed_boundary_pos(self, pos, direction):
        closed = False
        x, y = pos
        
        if direction == "E":
            for bx in self.hlist[y]:
                if bx > x and not closed:
                    break
                closed = not closed
            return (bx, y)
        
        elif direction == "W":
            for bx in reversed(self.hlist[y]):
                if bx < x and not closed:
                    break
                closed = not closed
            return (bx, y)
        
        elif direction == "S":
            for by in self.vlist[x]:
                if by > y and not closed:
                    break
                closed = not closed
            return (x, by)
        
        elif direction == "N":
            for by in reversed(self.vlist[y]):
                if by < y and not closed:
                    break
                closed = not closed
            return (x, by)
            
        else:
            raise RuntimeError("This method is only for cardinal directions")

    def get_next_open_boundary_pos(self, pos, direction):
        closed = False
        x, y = pos
        
        if direction == "E":
            for bx in self.hlist[y]:
                if bx > x and closed:
                    break
                closed = not closed
            return (bx, y)
        
        elif direction == "W":
            for bx in reversed(self.hlist[y]):
                if bx < x and closed:
                    break
                closed = not closed
            return (bx, y)
        
        elif direction == "S":
            for by in self.vlist[x]:
                if by > y and closed:
                    break
                closed = not closed
            return (x, by)
        
        elif direction == "N":
            for by in reversed(self.vlist[y]):
                if by < y and closed:
                    break
                closed = not closed
            return (x, by)
            
        else:
            raise RuntimeError("This method is only for cardinal directions")

if __name__ == "__main__":
        
    grid = [[ 0, 0, 0, 0, 0, 0, 1, 1, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1, 0, 0 ],
            [ 0, 1, 1, 1, 1, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1, 0, 0 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1, 0, 0 ],
            [ 1, 1, 1, 1, 0, 1, 0, 1, 0, 0 ],
            [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1, 0, 0 ]]
    
    startPos = (0,8)
    endPos = (9,6)
    print(startPos, endPos)
    
    blist = BoundaryList(grid)
    
    print("Hlist : ", blist.hlist,"/n")
    print("Vlist : ", blist.vlist)
    
    print(0, blist.getNextHorzOpenBoundary((0,0)))
    print(1, blist.getNextHorzOpenBoundary((0,1)))
    print(2, blist.getNextHorzOpenBoundary((0,2)))
    print(3, blist.getNextHorzOpenBoundary((0,3)))
    print(4, blist.getNextHorzOpenBoundary((0,4)))
    print(5, blist.getNextHorzOpenBoundary((0,5)))
    print(6, blist.getNextHorzOpenBoundary((0,6)))
    print(7, blist.getNextHorzOpenBoundary((0,7)))
    print(8, blist.getNextHorzOpenBoundary((0,8)))
    
    
            