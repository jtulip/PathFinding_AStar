'''
Created on 19 Dec 2014

@author: jtulip
'''
import unittest
from jps.test.TestDirection import TestDirection
from jps.test.TestJPSUtil import TestJPSUtil
from jps.test.TestNode import TestNode

testList = [TestDirection, TestJPSUtil, TestNode]
testLoader = unittest.TestLoader()

caseList = []
for test in testList:
    testCase = testLoader.loadTestsFromTestCase(test)
    caseList.append(testCase)
    
testSuite = unittest.TestSuite(caseList)

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)