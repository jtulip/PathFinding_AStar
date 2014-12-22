'''
Created on 19 Dec 2014

@author: jtulip
'''
import unittest
from jps.TestDirection import TestDirection
from jps.TestJPSUtil import TestJPSUtil

testList = [TestDirection, TestJPSUtil]
testLoader = unittest.TestLoader()

caseList = []
for test in testList:
    testCase = testLoader.loadTestsFromTestCase(test)
    caseList.append(testCase)
    
    #testSuite.addTest(unittest.makeSuite(test))

testSuite = unittest.TestSuite(caseList)

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)