'''
Created on 17 Dec 2014

@author: jtulip
'''

class BoundaryList:
    
    def __init__(self, grid):
        self.hlist = []
        self.vlist = []
        self.row = []
        self.col = []
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
    
        #          from index                to index                step         comparison                       xypos                     ypos
        '''
        self.params = {
            "E" : (lambda : 0,               lambda : len(self.row), lambda : 1,  lambda i,x,y : self.row[i] > x,  lambda i,x : self.row[i],   lambda j,y : y ),
            "W" : (lambda : len(self.row)-1, lambda : -1,            lambda : -1, lambda i,x,y : self.row[i] <= x, lambda i,x : self.row[i]-1, lambda j,y : y ),
            "S" : (lambda : 0,               lambda : len(self.col), lambda : 1,  lambda j,x,y : self.col[j] > y,  lambda i,x : x,             lambda j,y : self.col[j] ),
            "N" : (lambda : len(self.col)-1, lambda : -1,            lambda : -1, lambda j,x,y : self.col[j] <= y, lambda i,x : x,             lambda j,y : self.col[j]-1 ),
            }  
        '''      
        self.params = {
            "E" : (lambda : 0,               lambda : len(self.row), lambda : 1,  lambda i,x,y : self.row[i] > x,  lambda i,x,y : (self.row[i], y) ),
            "W" : (lambda : len(self.row)-1, lambda : -1,            lambda : -1, lambda i,x,y : self.row[i] <= x, lambda i,x,y : (self.row[i]-1, y) ),
            "S" : (lambda : 0,               lambda : len(self.col), lambda : 1,  lambda j,x,y : self.col[j] > y,  lambda j,x,y : (x, self.col[j]) ),
            "N" : (lambda : len(self.col)-1, lambda : -1,            lambda : -1, lambda j,x,y : self.col[j] <= y, lambda j,x,y : (x, self.col[j]-1) ),
            }  
        print(self.hlist)
        print(self.vlist)
        
    def in_bounds(self, pos):
        return pos[0] >= 0 and pos[0] <= self.maxX and pos[1] >= 0 and pos[1] <= self.maxY
            
    def get_next_closed_boundary_pos(self, pos, direction):
        '''return next closed boundary position''' 
        return self.get_next_sensed_boundary_pos(pos, direction, lambda x: not x)

    def get_next_open_boundary_pos(self, pos, direction):
        '''return next open boundary position''' 
        return self.get_next_sensed_boundary_pos(pos, direction, lambda x: x)
        
    def get_next_sensed_boundary_pos(self, pos, direction, sense):
        #deal with out of bounds pos
        if not self.in_bounds(pos):
            return None
        
        self.row = self.hlist[pos[1]]
        self.col = self.vlist[pos[0]]

        closed = True

        if direction in self.params.keys():
            from_index, to_index, step, cmp, xypos = self.params[direction]
            
            for i in range(from_index(), to_index(), step()):
                if cmp(i, pos[0], pos[1]) and sense(closed):
                    return xypos(i, pos[0], pos[1])
                closed = not closed
        
        else:
            raise RuntimeError("This method is only for cardinal directions")
        
        return None


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
    
    
            