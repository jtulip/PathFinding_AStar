'''
Created on 19 Dec 2014

@author: jtulip
'''
import unittest
from jps.Direction import Direction



class TestDirection(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testGetDirection(self):
        '''check that get_direction gives back the right compass direction'''
        fromPos = (3,3)
        expected = {(3,2):"N", 
                      (4,2):"NE",
                      (4,3):"E",
                      (4,4):"SE",
                      (3,4):"S",
                      (2,4):"SW",
                      (2,3):"W",
                      (2,2):"NW"}
        for toPos in expected.keys():
            actual = Direction.get_direction(fromPos, toPos)
            self.assertEqual(actual, expected[toPos], "Expected {}, got {})".format(expected[toPos], actual))
 
        
    def testGetNeighbour(self):
        '''check that get_neighbour gives back the right coordinates given a compass direction'''
        fromPos = (3,3)
        expected = {"N":(3,2), 
                      "NE":(4,2),
                      "E":(4,3),
                      "SE":(4,4),
                      "S":(3,4),
                      "SW":(2,4),
                      "W":(2,3),
                      "NW":(2,2)}
        
        for dirn in expected.keys():
            actual = Direction.get_neighbour(fromPos, dirn)
            self.assertEqual(actual, expected[dirn], "Expected {}, got {})".format(expected[dirn], actual))

 
    def testGetNeighbours(self):
        '''check that get_neighbours gives back the right neighbour coordinates'''
        pos = (3,3)
        expected = [(2,2), (2,3), (2,4), (3,2), (3,4), (4,2), (4,3), (4,4)]
        
        actual = sorted(Direction.get_neighbours(pos).values())
        self.assertEqual(actual, expected)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDirection']
    unittest.main()