'''
Created on 19 Dec 2014

@author: jtulip
'''
import unittest
from jps.Util import JPSUtil


class TestJPSUtil(unittest.TestCase):
    
    grid = []


    def setUp(self):
        #DON'T CHNGE THIS testCheckForced and testGetForced BOTH DEPEND ON IT
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
        params = JPSUtil.forced_params["N"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'NE':(2,2)},"get_forced returned the wrong dict")
                
        pos = (5,1)
        params = JPSUtil.forced_params["E"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'SE':(6,2)},"get_forced returned the wrong dict")

        pos = (1,3)
        params = JPSUtil.forced_params["S"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'SE':(2,4)},"get_forced returned the wrong dict")
        
        pos = (5,1)
        params = JPSUtil.forced_params["W"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'SW':(4,2)},"get_forced returned the wrong dict")

        pos = (5,1)
        params = JPSUtil.forced_params["NE"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'SE':(6,2)},"get_forced returned the wrong dict")

        pos = (7,6)
        params = JPSUtil.forced_params["SE"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'NE':(8,5)},"get_forced returned the wrong dict")

        pos = (7,6)
        params = JPSUtil.forced_params["SW"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'NW':(6,5)},"get_forced returned the wrong dict")

        pos = (5,1)
        params = JPSUtil.forced_params["NW"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPSUtil.grid)
        self.assertDictContainsSubset(actual, {'SW':(4,2)},"get_forced returned the wrong dict")

    def testPruneCutting(self):
        '''test that prune working properly when corner cutting allowed'''
        
        #test cardinal directions for no blocking neighbours
        pos = (1,1)
        (has_forced, pruned) = JPSUtil.prune(pos, "N", TestJPSUtil.grid, True)
        self.assertFalse(has_forced,"has_forced in error for N")
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N': (1, 0)},"pruned contains wrong neighbour for N")

        (has_forced, pruned) = JPSUtil.prune(pos, "E", TestJPSUtil.grid, True)
        self.assertFalse(has_forced,"has_forced in error for N")
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'E': (2, 1)},"pruned contains wrong neighbour for E")

        (has_forced, pruned) = JPSUtil.prune(pos, "S", TestJPSUtil.grid, True)
        self.assertFalse(has_forced,"has_forced in error for S")
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S': (1, 2)},"pruned contains wrong neighbour for S")

        (has_forced, pruned) = JPSUtil.prune(pos, "W", TestJPSUtil.grid, True)
        self.assertFalse(has_forced,"has_forced in error for W")
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'W': (0, 1)},"pruned contains wrong neighbour for W")

        #test diagonal directions for no blocking neighbours
        (has_forced, pruned) = JPSUtil.prune(pos, "NE", TestJPSUtil.grid, True)
        self.assertFalse(has_forced,"has_forced in error for NE")
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N':(1, 0), 'E':(2, 1), 'NE':(2,0)},"pruned contains wrong neighbours for NE")

        (has_forced, pruned) = JPSUtil.prune(pos, "SE", TestJPSUtil.grid, True)
        self.assertFalse(has_forced,"has_forced in error for SE")
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S':(1, 2), 'E':(2, 1), 'SE':(2,2)},"pruned contains wrong neighbours for NE")

        (has_forced, pruned) = JPSUtil.prune(pos, "SW", TestJPSUtil.grid, True)
        self.assertFalse(has_forced,"has_forced in error for SW")
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S':(1, 2), 'W':(0, 1), 'SW':(0,2)},"pruned contains wrong neighbours for SW")

        (has_forced, pruned) = JPSUtil.prune(pos, "NW", TestJPSUtil.grid, True)
        self.assertFalse(has_forced,"has_forced in error for WW")
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N':(1, 0), 'W':(0, 1), 'NW':(0,0)},"pruned contains wrong neighbours for SW")

        #now test cardinals with forced neighbours
        pos = (1,3)
        (has_forced, pruned) = JPSUtil.prune(pos, "N", TestJPSUtil.grid, True)
        self.assertTrue(has_forced,"has_forced in error for N with blocked E forced NE ")
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N': (1, 2), 'NE': (2, 2)},"pruned contains wrong forced neighbours for N blocked E")
                
        pos = (5,1)
        (has_forced, pruned) = JPSUtil.prune(pos, "E", TestJPSUtil.grid, True)
        self.assertTrue(has_forced,"has_forced in error for E with blocked S forced SE ")
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'SE': (6, 2), 'E': (6, 1)},"pruned contains wrong forced neighbours for E blocked S")

        pos = (1,3)
        (has_forced, pruned) = JPSUtil.prune(pos, "S", TestJPSUtil.grid, True)
        self.assertTrue(has_forced,"has_forced in error for S with blocked E forced SE ")
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S': (1, 4), 'SE': (2, 4)},"pruned contains wrong forced neighbours for S blocked E")

        pos = (5,1)
        (has_forced, pruned) = JPSUtil.prune(pos, "W", TestJPSUtil.grid, True)
        self.assertTrue(has_forced,"has_forced in error for W with blocked S forced SW ")
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'W': (4, 1), 'SW': (4, 2)},"pruned contains wrong forced neighbours for W blocked S")

        #now test diagonals with forced neighbours
        pos = (5,1)
        (has_forced, pruned) = JPSUtil.prune(pos, "NE", TestJPSUtil.grid, True)
        self.assertTrue(has_forced,"has_forced in error for NE with blocked S forced SE ")
        self .assertTrue(len(pruned) == 4,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'E': (6, 1), 'SE': (6, 2), 'N': (5, 0), 'NE': (6, 0)},"pruned contains wrong forced neighbours for N blocked E")

        pos = (7,6)
        (has_forced, pruned) = JPSUtil.prune(pos, "SE", TestJPSUtil.grid, True)
        self.assertTrue(has_forced,"has_forced in error for SE with blocked N forced NE ")
        self .assertTrue(len(pruned) == 4,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'SE': (8, 7), 'E': (8, 6), 'NE': (8, 5), 'S': (7, 7)},"pruned contains wrong forced neighbours for N blocked E")

        pos = (7,6)
        (has_forced, pruned) = JPSUtil.prune(pos, "SW", TestJPSUtil.grid, True)
        self.assertTrue(has_forced,"has_forced in error for SW with blocked N forced NW ")
        self .assertTrue(len(pruned) == 4,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'SW': (6, 7), 'NW': (6, 5), 'S': (7, 7), 'W': (6, 6)},"pruned contains wrong forced neighbours for N blocked E")

        pos = (5,1)
        (has_forced, pruned) = JPSUtil.prune(pos, "NW", TestJPSUtil.grid, True)
        self.assertTrue(has_forced,"has_forced in error for NW with blocked S forced SW ")
        self .assertTrue(len(pruned) == 4,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N': (5, 0), 'NW': (4, 0), 'SW': (4, 2), 'W': (4, 1)},"pruned contains wrong forced neighbours for N blocked E")

    def testPruneNonCutting(self):
        '''test that prune working properly when corner cutting allowed'''
        
        #test cardinal directions for no blocking neighbours
        pos = (1,1)
        (has_forced, pruned) = JPSUtil.prune(pos, "N", TestJPSUtil.grid, False)
        self.assertFalse(has_forced,"has_forced in error for N")
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N': (1, 0)},"pruned contains wrong neighbour for N")

        (has_forced, pruned) = JPSUtil.prune(pos, "E", TestJPSUtil.grid, False)
        self.assertFalse(has_forced,"has_forced in error for N")
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'E': (2, 1)},"pruned contains wrong neighbour for E")

        (has_forced, pruned) = JPSUtil.prune(pos, "S", TestJPSUtil.grid, False)
        self.assertFalse(has_forced,"has_forced in error for S")
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S': (1, 2)},"pruned contains wrong neighbour for S")

        (has_forced, pruned) = JPSUtil.prune(pos, "W", TestJPSUtil.grid, False)
        self.assertFalse(has_forced,"has_forced in error for W")
        self .assertTrue(len(pruned) == 1,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'W': (0, 1)},"pruned contains wrong neighbour for W")

        #test diagonal directions for no blocking neighbours
        (has_forced, pruned) = JPSUtil.prune(pos, "NE", TestJPSUtil.grid, False)
        self.assertFalse(has_forced,"has_forced in error for NE")
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N':(1, 0), 'E':(2, 1), 'NE':(2,0)},"pruned contains wrong neighbours for NE")

        (has_forced, pruned) = JPSUtil.prune(pos, "SE", TestJPSUtil.grid, False)
        self.assertFalse(has_forced,"has_forced in error for SE")
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S':(1, 2), 'E':(2, 1), 'SE':(2,2)},"pruned contains wrong neighbours for NE")

        (has_forced, pruned) = JPSUtil.prune(pos, "SW", TestJPSUtil.grid, False)
        self.assertFalse(has_forced,"has_forced in error for SW")
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S':(1, 2), 'W':(0, 1), 'SW':(0,2)},"pruned contains wrong neighbours for SW")

        (has_forced, pruned) = JPSUtil.prune(pos, "NW", TestJPSUtil.grid, False)
        self.assertFalse(has_forced,"has_forced in error for WW")
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N':(1, 0), 'W':(0, 1), 'NW':(0,0)},"pruned contains wrong neighbours for SW")

        #now test cardinals with forced neighbours
        pos = (1,3)
        (has_forced, pruned) = JPSUtil.prune(pos, "N", TestJPSUtil.grid, False)
        self.assertTrue(has_forced,"has_forced in error for N with blocked E forced NE ")
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N': (1, 2), 'NE': (2, 2)},"pruned contains wrong forced neighbours for N blocked E")
                
        pos = (5,1)
        (has_forced, pruned) = JPSUtil.prune(pos, "E", TestJPSUtil.grid, False)
        self.assertTrue(has_forced,"has_forced in error for E with blocked S forced SE ")
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'SE': (6, 2), 'E': (6, 1)},"pruned contains wrong forced neighbours for E blocked S")

        pos = (1,3)
        (has_forced, pruned) = JPSUtil.prune(pos, "S", TestJPSUtil.grid, False)
        self.assertTrue(has_forced,"has_forced in error for S with blocked E forced SE ")
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'S': (1, 4), 'SE': (2, 4)},"pruned contains wrong forced neighbours for S blocked E")

        pos = (5,1)
        (has_forced, pruned) = JPSUtil.prune(pos, "W", TestJPSUtil.grid, False)
        self.assertTrue(has_forced,"has_forced in error for W with blocked S forced SW ")
        self .assertTrue(len(pruned) == 2,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'W': (4, 1), 'SW': (4, 2)},"pruned contains wrong forced neighbours for W blocked S")

        #now test diagonals with forced neighbours
        pos = (5,1)
        (has_forced, pruned) = JPSUtil.prune(pos, "NE", TestJPSUtil.grid, False)
        self.assertFalse(has_forced,"has_forced in error for NE with blocked S forced SE ")
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'E': (6, 1), 'N': (5, 0), 'NE': (6, 0)},"pruned contains wrong forced neighbours for N blocked E")

        pos = (7,6)
        (has_forced, pruned) = JPSUtil.prune(pos, "SE", TestJPSUtil.grid, False)
        self.assertFalse(has_forced,"has_forced in error for SE with blocked N forced NE ")
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'SE': (8, 7), 'E': (8, 6), 'S': (7, 7)},"pruned contains wrong forced neighbours for N blocked E")

        pos = (7,6)
        (has_forced, pruned) = JPSUtil.prune(pos, "SW", TestJPSUtil.grid, False)
        self.assertFalse(has_forced,"has_forced in error for SW with blocked N forced NW ")
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'SW': (6, 7), 'S': (7, 7), 'W': (6, 6)},"pruned contains wrong forced neighbours for N blocked E")

        pos = (5,1)
        (has_forced, pruned) = JPSUtil.prune(pos, "NW", TestJPSUtil.grid, False)
        self.assertFalse(has_forced,"has_forced in error for NW with blocked S forced SW ")
        self .assertTrue(len(pruned) == 3,"pruned not the right length")
        self.assertDictContainsSubset(pruned, {'N': (5, 0), 'NW': (4, 0), 'W': (4, 1)},"pruned contains wrong forced neighbours for N blocked E")

                
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()