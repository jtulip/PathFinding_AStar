'''
Created on 19 Dec 2014

@author: jtulip
'''
import unittest
from jps.Util import JPSUtil


class TestJPSUtil(unittest.TestCase):
    
    grid = []


    def setUp(self):
        #DON'T CHANGE THIS testCheckForced and testGetForced BOTH DEPEND ON IT
        TestJPSUtil.grid = [[ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ],
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


    def testCheckForced(self):
        '''test that check forced working properly'''
        pos = (1,3)
        params = JPSUtil.forced_params["N"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPSUtil.grid)
        self.assertFalse(actual,"check_forced returned True in error going N for W")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPSUtil.grid)
        self.assertTrue(actual,"check_forced returned False in error going N for E")
        
        pos = (5,1)
        params = JPSUtil.forced_params["E"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPSUtil.grid)
        self.assertFalse(actual,"check_forced returned True in error going E for N")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPSUtil.grid)
        self.assertTrue(actual,"check_forced returned False in error going E for S")
        
        pos = (1,3)
        params = JPSUtil.forced_params["S"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPSUtil.grid)
        self.assertTrue(actual,"check_forced returned False in error going S for E")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPSUtil.grid)
        self.assertFalse(actual,"check_forced returned True in error going W for W")
        
        pos = (5,1)
        params = JPSUtil.forced_params["W"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPSUtil.grid)
        self.assertTrue(actual,"check_forced returned False in error going W for S")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPSUtil.grid)
        self.assertFalse(actual,"check_forced returned Tue in error going W for N")

        pos = (5,1)
        params = JPSUtil.forced_params["NE"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPSUtil.grid)
        self.assertFalse(actual,"check_forced returned True in error going NE for W")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPSUtil.grid)
        self.assertTrue(actual,"check_forced returned False in error going NE for S")

        pos = (7,6)
        params = JPSUtil.forced_params["SE"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPSUtil.grid)
        self.assertTrue(actual,"check_forced returned False in error going SW for N")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPSUtil.grid)
        self.assertFalse(actual,"check_forced returned True in error going SE for W")
        
        pos = (7,6)
        params = JPSUtil.forced_params["SW"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPSUtil.grid)
        self.assertFalse(actual,"check_forced returned True in error going SW for E")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPSUtil.grid)
        self.assertTrue(actual,"check_forced returned False in error going SE for N")
        
        pos = (5,1)
        params = JPSUtil.forced_params["NW"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPSUtil.grid)
        self.assertTrue(actual,"check_forced returned False in error going NW for S")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPSUtil.grid)
        self.assertFalse(actual,"check_forced returned True in error going NW for E")

    def testGetForced(self):
        '''test that get_forced working properly'''
        pos = (1,3)
        actual = JPSUtil.get_forced(pos, "N", TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'NE':(2,2)},"get_forced returned the wrong dict")
                
        pos = (5,1)
        actual = JPSUtil.get_forced(pos, "E", TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'SE':(6,2)},"get_forced returned the wrong dict")

        pos = (1,3)
        actual = JPSUtil.get_forced(pos, "S", TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'SE':(2,4)},"get_forced returned the wrong dict")
        
        pos = (5,1)
        actual = JPSUtil.get_forced(pos, "W", TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'SW':(4,2)},"get_forced returned the wrong dict")

        pos = (5,1)
        actual = JPSUtil.get_forced(pos, "NE", TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'SE':(6,2)},"get_forced returned the wrong dict")

        pos = (7,6)
        actual = JPSUtil.get_forced(pos, "SE", TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'NE':(8,5)},"get_forced returned the wrong dict")

        pos = (7,6)
        actual = JPSUtil.get_forced(pos, "SW", TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'NW':(6,5)},"get_forced returned the wrong dict")

        pos = (5,1)
        actual = JPSUtil.get_forced(pos, "NW", TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'SW':(4,2)},"get_forced returned the wrong dict")

    def testHasForced(self):
        '''test that has_forced working properly'''
        pos = (1,1)
        actual = JPSUtil.has_forced(pos, "N", TestJPSUtil.grid)
        self.assertFalse(actual)

        pos = (1,3)
        actual = JPSUtil.has_forced(pos, "N", TestJPSUtil.grid)
        self.assertTrue(actual)
                
        pos = (5,1)
        actual = JPSUtil.has_forced(pos, "E", TestJPSUtil.grid)
        self.assertTrue(actual)

        pos = (1,3)
        actual = JPSUtil.has_forced(pos, "S", TestJPSUtil.grid)
        self.assertTrue(actual)
        
        pos = (5,1)
        actual = JPSUtil.has_forced(pos, "W", TestJPSUtil.grid)
        self.assertTrue(actual)

        pos = (5,1)
        actual = JPSUtil.has_forced(pos,"NE", TestJPSUtil.grid)
        self.assertTrue(actual)

        pos = (7,6)
        actual = JPSUtil.has_forced(pos, "SE", TestJPSUtil.grid)
        self.assertTrue(actual)

        pos = (7,6)
        actual = JPSUtil.has_forced(pos, "SW", TestJPSUtil.grid)
        self.assertTrue(actual)

        pos = (5,1)
        actual = JPSUtil.has_forced(pos, "NW", TestJPSUtil.grid)
        self.assertTrue(actual)

    def testPruneCutting(self):
        '''test that prune working properly when corner cutting allowed'''
        
        #test cardinal directions for no blocking neighbours
        pos = (1,1)
        pruned = JPSUtil.prune(pos, "N", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N': (1, 0)},"pruned contains wrong neighbour for N")

        pruned = JPSUtil.prune(pos, "E", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'E': (2, 1)},"pruned contains wrong neighbour for E")

        pruned = JPSUtil.prune(pos, "S", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S': (1, 2)},"pruned contains wrong neighbour for S")

        pruned = JPSUtil.prune(pos, "W", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'W': (0, 1)},"pruned contains wrong neighbour for W")

        #test diagonal directions for no blocking neighbours
        pruned = JPSUtil.prune(pos, "NE", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N':(1, 0), 'E':(2, 1), 'NE':(2,0)},"pruned contains wrong neighbours for NE")

        pruned = JPSUtil.prune(pos, "SE", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S':(1, 2), 'E':(2, 1), 'SE':(2,2)},"pruned contains wrong neighbours for NE")

        pruned = JPSUtil.prune(pos, "SW", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S':(1, 2), 'W':(0, 1), 'SW':(0,2)},"pruned contains wrong neighbours for SW")

        pruned = JPSUtil.prune(pos, "NW", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N':(1, 0), 'W':(0, 1), 'NW':(0,0)},"pruned contains wrong neighbours for SW")

        #now test cardinals with forced neighbours
        pos = (1,3)
        pruned = JPSUtil.prune(pos, "N", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N': (1, 2), 'NE': (2, 2)},"pruned contains wrong forced neighbours for N blocked E")
                
        pos = (5,1)
        pruned = JPSUtil.prune(pos, "E", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'SE': (6, 2), 'E': (6, 1)},"pruned contains wrong forced neighbours for E blocked S")

        pos = (1,3)
        pruned = JPSUtil.prune(pos, "S", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S': (1, 4), 'SE': (2, 4)},"pruned contains wrong forced neighbours for S blocked E")

        pos = (5,1)
        pruned = JPSUtil.prune(pos, "W", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'W': (4, 1), 'SW': (4, 2)},"pruned contains wrong forced neighbours for W blocked S")

        #now test diagonals with forced neighbours
        pos = (5,1)
        pruned = JPSUtil.prune(pos, "NE", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 4,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'E': (6, 1), 'SE': (6, 2), 'N': (5, 0), 'NE': (6, 0)},"pruned contains wrong forced neighbours for N blocked E")

        pos = (7,6)
        pruned = JPSUtil.prune(pos, "SE", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 4,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'SE': (8, 7), 'E': (8, 6), 'NE': (8, 5), 'S': (7, 7)},"pruned contains wrong forced neighbours for N blocked E")

        pos = (7,6)
        pruned = JPSUtil.prune(pos, "SW", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 4,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'SW': (6, 7), 'NW': (6, 5), 'S': (7, 7), 'W': (6, 6)},"pruned contains wrong forced neighbours for N blocked E")

        pos = (5,1)
        pruned = JPSUtil.prune(pos, "NW", TestJPSUtil.grid, True)
        self .assertTrue(len(pruned) == 4,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N': (5, 0), 'NW': (4, 0), 'SW': (4, 2), 'W': (4, 1)},"pruned contains wrong forced neighbours for N blocked E")

    def testPruneNonCutting(self):
        '''test that prune working properly when corner cutting allowed'''
        
        #test cardinal directions for no blocking neighbours
        pos = (1,1)
        pruned = JPSUtil.prune(pos, "N", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N': (1, 0)},"pruned contains wrong neighbour for N")

        pruned = JPSUtil.prune(pos, "E", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'E': (2, 1)},"pruned contains wrong neighbour for E")

        pruned = JPSUtil.prune(pos, "S", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S': (1, 2)},"pruned contains wrong neighbour for S")

        pruned = JPSUtil.prune(pos, "W", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'W': (0, 1)},"pruned contains wrong neighbour for W")

        #test diagonal directions for no blocking neighbours
        pruned = JPSUtil.prune(pos, "NE", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N':(1, 0), 'E':(2, 1), 'NE':(2,0)},"pruned contains wrong neighbours for NE")

        pruned = JPSUtil.prune(pos, "SE", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S':(1, 2), 'E':(2, 1), 'SE':(2,2)},"pruned contains wrong neighbours for NE")

        pruned = JPSUtil.prune(pos, "SW", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S':(1, 2), 'W':(0, 1), 'SW':(0,2)},"pruned contains wrong neighbours for SW")

        pruned = JPSUtil.prune(pos, "NW", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N':(1, 0), 'W':(0, 1), 'NW':(0,0)},"pruned contains wrong neighbours for SW")

        #now test cardinals with forced neighbours
        pos = (1,3)
        pruned = JPSUtil.prune(pos, "N", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N': (1, 2), 'NE': (2, 2)},"pruned contains wrong forced neighbours for N blocked E")
                
        pos = (5,1)
        pruned = JPSUtil.prune(pos, "E", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'SE': (6, 2), 'E': (6, 1)},"pruned contains wrong forced neighbours for E blocked S")

        pos = (1,3)
        pruned = JPSUtil.prune(pos, "S", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S': (1, 4), 'SE': (2, 4)},"pruned contains wrong forced neighbours for S blocked E")

        pos = (5,1)
        pruned = JPSUtil.prune(pos, "W", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'W': (4, 1), 'SW': (4, 2)},"pruned contains wrong forced neighbours for W blocked S")

        #now test diagonals with forced neighbours
        pos = (5,1)
        pruned = JPSUtil.prune(pos, "NE", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'E': (6, 1), 'N': (5, 0), 'NE': (6, 0)},"pruned contains wrong forced neighbours for N blocked E")

        pos = (7,6)
        pruned = JPSUtil.prune(pos, "SE", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'SE': (8, 7), 'E': (8, 6), 'S': (7, 7)},"pruned contains wrong forced neighbours for N blocked E")

        pos = (7,6)
        pruned = JPSUtil.prune(pos, "SW", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'SW': (6, 7), 'S': (7, 7), 'W': (6, 6)},"pruned contains wrong forced neighbours for N blocked E")

        pos = (5,1)
        pruned = JPSUtil.prune(pos, "NW", TestJPSUtil.grid, False)
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N': (5, 0), 'NW': (4, 0), 'W': (4, 1)},"pruned contains wrong forced neighbours for N blocked E")

                
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()