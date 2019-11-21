import unittest
import HTMLTestRunner
import os
import time
from ph_APG_performance2 import APGTimeTests

#from homepagetests import HomePageTest

# get the directory path to output report file
result_dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
test_page = unittest.TestLoader().loadTestsFromTestCase(APGTimeTests)
#home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_test and home_page_test
#smoke_tests = unittest.TestSuite([home_page_tests, search_tests])
#one_tests = unittest.TestSuite(test_Logout)

# open the report file
outfile = open(result_dir + '\PH_Performance2_APG' + time.strftime('-%Y%m%d-%H%M') +'.html', 'w')

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                       title='PH APG Performance Test Report',
                                       description='PH APG Performance Test')

# run the suite using HTMLTestRunner
runner.run(test_page)