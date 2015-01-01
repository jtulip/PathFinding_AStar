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
    
    def getNextHorzCloseBoundary(self, pos):
        closed = False
        for b in self.hlist[pos[1]]:
            if b > pos[0] and not closed:
                break
            closed = not closed
        return b

    def getNextHorzOpenBoundary(self, pos):
        closed = False
        for b in self.hlist[pos[1]]:
            if b > pos[0] and closed:
                break
            closed = not closed
        return b

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
    
    
            