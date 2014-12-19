'''
Created on 19 Dec 2014

@author: jtulip
'''
import unittest
from jps.JPSUtil import JPSUtil


class TestJPS(unittest.TestCase):
    
    grid = []


    def setUp(self):
        #DON'T CHNGE THIS testCheckForced and testGetForced BOTH DEPEND ON IT
        TestJPS.grid = [[ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ],
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
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPS.grid)
        self.assertFalse(actual,"check_forced returned True in error going N for W")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPS.grid)
        self.assertTrue(actual,"check_forced returned False in error going N for E")
        
        pos = (5,1)
        params = JPSUtil.forced_params["E"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPS.grid)
        self.assertFalse(actual,"check_forced returned True in error going E for N")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPS.grid)
        self.assertTrue(actual,"check_forced returned False in error going E for S")
        
        pos = (1,3)
        params = JPSUtil.forced_params["S"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPS.grid)
        self.assertTrue(actual,"check_forced returned False in error going S for E")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPS.grid)
        self.assertFalse(actual,"check_forced returned True in error going W for W")
        
        pos = (5,1)
        params = JPSUtil.forced_params["W"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPS.grid)
        self.assertTrue(actual,"check_forced returned False in error going W for S")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPS.grid)
        self.assertFalse(actual,"check_forced returned Tue in error going W for N")

        pos = (5,1)
        params = JPSUtil.forced_params["NE"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPS.grid)
        self.assertFalse(actual,"check_forced returned True in error going NE for W")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPS.grid)
        self.assertTrue(actual,"check_forced returned False in error going NE for S")

        pos = (7,6)
        params = JPSUtil.forced_params["SE"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPS.grid)
        self.assertTrue(actual,"check_forced returned False in error going SW for N")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPS.grid)
        self.assertFalse(actual,"check_forced returned True in error going SE for W")
        
        pos = (7,6)
        params = JPSUtil.forced_params["SW"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPS.grid)
        self.assertFalse(actual,"check_forced returned True in error going SW for E")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPS.grid)
        self.assertTrue(actual,"check_forced returned False in error going SE for N")
        
        pos = (5,1)
        params = JPSUtil.forced_params["NW"]
        actual = JPSUtil.check_forced(pos, params[0], params[1], TestJPS.grid)
        self.assertTrue(actual,"check_forced returned False in error going NW for S")
        actual = JPSUtil.check_forced(pos, params[2], params[3], TestJPS.grid)
        self.assertFalse(actual,"check_forced returned True in error going NW for E")

    def testGetForced(self):
        '''test that get_forced working properly'''
        pos = (1,3)
        params = JPSUtil.forced_params["N"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPS.grid)
        self.assertDictContainsSubset(actual, {'NE':(2,2)},"get_forced returned the wrong dict")
                
        pos = (5,1)
        params = JPSUtil.forced_params["E"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPS.grid)
        self.assertDictContainsSubset(actual, {'SE':(6,2)},"get_forced returned the wrong dict")

        pos = (1,3)
        params = JPSUtil.forced_params["S"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPS.grid)
        self.assertDictContainsSubset(actual, {'SE':(2,4)},"get_forced returned the wrong dict")
        
        pos = (5,1)
        params = JPSUtil.forced_params["W"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPS.grid)
        self.assertDictContainsSubset(actual, {'SW':(4,2)},"get_forced returned the wrong dict")

        pos = (5,1)
        params = JPSUtil.forced_params["NE"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPS.grid)
        self.assertDictContainsSubset(actual, {'SE':(6,2)},"get_forced returned the wrong dict")

        pos = (7,6)
        params = JPSUtil.forced_params["SE"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPS.grid)
        self.assertDictContainsSubset(actual, {'NE':(8,5)},"get_forced returned the wrong dict")

        pos = (7,6)
        params = JPSUtil.forced_params["SW"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPS.grid)
        self.assertDictContainsSubset(actual, {'NW':(6,5)},"get_forced returned the wrong dict")

        pos = (5,1)
        params = JPSUtil.forced_params["NW"]
        actual = JPSUtil.get_forced(pos, params[0], params[1], params[2], params[3], TestJPS.grid)
        self.assertDictContainsSubset(actual, {'SW':(4,2)},"get_forced returned the wrong dict")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()