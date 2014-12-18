'''
Created on 18 Dec 2014

@author: jtulip
'''

from pathfinding.common.JPS_Node import JPS_Node

grid = [[ 0, 0, 1, 0, 0, 0, 0, 1, 0, 0 ],
     [ 0, 0, 1, 0, 0, 0, 0, 1, 0, 0 ],
     [ 0, 0, 1, 0, 0, 0, 0, 1, 0, 0 ],
     [ 0, 0, 1, 0, 0, 1, 0, 1, 0, 0 ],
     [ 0, 0, 1, 0, 0, 1, 0, 1, 0, 0 ],
     [ 0, 0, 1, 0, 0, 1, 0, 1, 0, 0 ],
     [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
     [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
     [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ]]


n1 = JPS_Node((3,3), None, (8,8), grid)
n2 = JPS_Node((3,2), n1, (8,8), grid) #N
n3 = JPS_Node((4,2), n1, (8,8), grid) #NE
n4 = JPS_Node((4,3), n1, (8,8), grid) #E
n5 = JPS_Node((4,4), n1, (8,8), grid) #SE
n6 = JPS_Node((3,4), n1, (8,8), grid) #S
n7 = JPS_Node((2,4), n1, (8,8), grid) #SW
n8 = JPS_Node((2,3), n1, (8,8), grid) #W
n9 = JPS_Node((2,2), n1, (8,8), grid) #NW
   
nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9]

for n in nodes:
    print(n.direction)
