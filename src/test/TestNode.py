'''
Created on 22 Dec 2014

@author: jtulip
'''
import unittest

from jps.Node import Node

class TestNode(unittest.TestCase):


    def testNodeConstructor(self):
        startPos = (0,0)
        endPos = (1,1)
        actual = Node(startPos, None)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()