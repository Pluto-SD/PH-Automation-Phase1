# coding=UTF-8

import unittest
import HTMLTestRunner
import os
# from homepagetests import HomePageTest
from ph_online_deposit_mobile import MobileTests

'''Get the directory path to output report file'''
result_dir = os.getcwd()   # 取得目前工作目錄

'''Get all tests from SearchProductTest and HomePageTest class'''
# home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
test_page = unittest.TestLoader().loadTestsFromTestCase(MobileTests)

'''Create a test suite combining search_test and home_page_test'''
# smoke_tests = unittest.TestSuite([home_page_tests, search_tests])
# one_tests = unittest.TestSuite(test_Logout)

'''Open the report file'''
outfile = open(result_dir + "\\PH_Deposit_Mobile.html", "wb")       # 20191122: w -> wb, 解決TypeError: write() argument must be str, not bytes

# Configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='PH Deposit Mobile Test Report', description='PH online Deposit Mobile Test')

# Run the suite using HTMLTestRunner
runner.run(test_page)
