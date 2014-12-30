'''
Created on 22 Dec 2014

@author: jtulip
'''
import unittest

from jps.Node import Node

class TestNode(unittest.TestCase):
    
    grid = []

    def setUp(self):
        #DON'T CHANGE THIS 
        TestNode.grid = [[ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ],
                         [ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ],
                         [ 0, 0, 0, 0, 0, 1, 0, 1, 0, 0 ],
                         [ 0, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
                         [ 0, 0, 0, 0, 0, 1, 0, 1, 0, 0 ],
                         [ 0, 0, 0, 0, 0, 1, 0, 1, 0, 0 ],
                         [ 1, 1, 1, 0, 0, 1, 0, 0, 0, 0 ],
                         [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
                         [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ]]
    


    def tearDown(self):
        pass

    def testNode(self):
        startPos = (0,0)
        endPos = (1,1)
        actual = Node(startPos, None, endPos, TestNode.grid)
        
        self.assertTrue(actual.get_pos() == (0,0))
        self.assertTrue(actual.endPos == (1,1))
        self.assertEqual(actual.get_direction(), "O")
        self.assertAlmostEqual(actual.get_cost(), 0.0, places = 4)
        self.assertAlmostEqual(actual.get_prox(), 1.4142, places = 4)
        self.assertAlmostEqual(actual.get_rank(), 1.4142*0.4, places = 4)
        
    def testJump(self):
        startPos = (0,0)
        endPos = (9,2)
        startNode = Node(startPos, None, endPos, TestNode.grid)
        curPos = (1,1)
        curNode = Node(curPos, startNode, endPos, TestNode.grid)
        jumpPos = curNode.jump(curPos, curNode.get_direction(), endPos, True)
        print(jumpPos)
        startNode = Node(startPos, None, endPos, TestNode.grid)
        
           
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()