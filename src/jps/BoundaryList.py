'''
Created on 17 Dec 2014

@author: jtulip
'''

class BoundaryList:
    
    def __init__(self, grid):
        self.hlist = []
        self.vlist = []
        self.maxX = len(grid[0])-1
        self.maxY = len(grid)-1
        
        # calculate the horizontal boundary lists
        for row in range(len(grid)):
            sense = 0                        #0 represents open on grid
            rlist = [0]
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
            clist = [0]
            for row in range(len(grid)):
                if grid[row][col] != sense:
                    clist.append(row)
                    sense = grid[row][col]
            if sense == 0:
                clist.append(len(grid))
            self.vlist.append(clist)
    
        print(self.hlist)
        print(self.vlist)
        
        
    def get_next_closed_boundary_pos(self, pos, direction):
        x, y = pos
        #deal with out of bounds x indices
        if x < 0 or x > self.maxX:
            return None
        
        #deal with out of bounds y indices
        if y < 0 or y >= self.maxY:
            return None
        
        hl = self.hlist[y]
        vl = self.vlist[x]

        closed = True
        if direction == "E":
            for bx in hl:
                if bx > x and not closed:
                    break
                closed = not closed
            return (bx, y)
        
        elif direction == "W":
            for bx in reversed(hl):
                if bx <= x and not closed:
                    break
                closed = not closed
            return (bx-1, y)
        
        elif direction == "S":
            for by in vl:
                if by > y and not closed:
                    break
                closed = not closed
            return (x, by)
        
        elif direction == "N":
            for by in reversed(vl):
                if by <= y and not closed:
                    break
                closed = not closed
            return (x, by-1)
            
        else:
            raise RuntimeError("This method is only for cardinal directions")


    def get_next_open_boundary_pos(self, pos, direction):
        x, y = pos
        #deal with out of bounds x indices
        if x < 0 or x > self.maxX:
            return None
        
        #deal with out of bounds y indices
        if y < 0 or y >= self.maxY:
            return None
                
        hl = self.hlist[y]
        vl = self.vlist[x]
        
        closed = True
        if direction == "E":
            for bx in hl:
                if bx > x and closed:
                    break
                closed = not closed
            return (bx, y)
        
        elif direction == "W":
            for bx in reversed(hl):
                if bx <= x and closed:
                    break
                closed = not closed
            return (bx-1, y)
        
        elif direction == "S":
            for by in vl:
                if by > y and closed:
                    break
                closed = not closed
            return (x, by)
        
        elif direction == "N":
            for by in reversed(vl):
                if by <= y and closed:
                    break
                closed = not closed
            return (x, by-1)
            
        else:
            raise RuntimeError("This method is only for cardinal directions")


if __name__ == "__main__":
        
    grid = [[ 0, 0, 0, 0, 0, 0, 1, 1, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
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
    
    '''
    for y in range(len(grid)):
        print(y, blist.get_next_closed_boundary_pos((0, y),"E"))

    for y in range(len(grid)):
        print(y, blist.get_next_closed_boundary_pos((9, y),"W"))

    for x in range(len(grid[0])):
        print(x, blist.get_next_closed_boundary_pos((x, 0),"S"))

    for x in range(len(grid[0])):
        print(x, blist.get_next_closed_boundary_pos((x, 8),"N"))
    
    for y in range(len(grid)):
        print(y, blist.get_next_open_boundary_pos((0, y),"E"))

    for y in range(len(grid)):
        print(y, blist.get_next_open_boundary_pos((9, y),"W"))

    for x in range(len(grid[0])):
        print(x, blist.get_next_open_boundary_pos((x, 0),"S"))
    '''
    for x in range(len(grid[0])):
        print(x, blist.get_next_open_boundary_pos((x, 8),"N"))
    
    
            