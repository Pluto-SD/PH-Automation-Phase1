import unittest
import HTMLTestRunner
import os
from ph_online_switchpage import switchpage

#from homepagetests import HomePageTest

# get the directory path to output report file
result_dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
test_page = unittest.TestLoader().loadTestsFromTestCase(switchpage)
#home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_test and home_page_test
#smoke_tests = unittest.TestSuite([home_page_tests, search_tests])
#one_tests = unittest.TestSuite(test_Logout)

# open the report file
outfile = open(result_dir + '\PH_online_Swtich_Page_Test.html', 'w')

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                       title='PH online Swtich Page Test Report',
                                       description='PH online Swtich Page time Test.')
# run the suite using HTMLTestRunner
runner.run(test_page)