import unittest
import HTMLTestRunner
import os
from ph_offline_bankacct import bankacct

#from homepagetests import HomePageTest

# get the directory path to output report file
result_dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
test = unittest.TestLoader().loadTestsFromTestCase(bankacct)
#home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_test and home_page_test
#smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# open the report file
outfile = open(result_dir + '\ph_create_bankacct' + time.strftime('-%Y%m%d-%H%M') + '.html', 'w')

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                       title='PH Create Bank Account Test Report',
                                       description='***** Auto Create Bank Account *****')

# run the suite using HTMLTestRunner
runner.run(test)
