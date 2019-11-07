import unittest
import HTMLTestRunner
import os
import time
from ph_online_login import LoginTests

#from homepagetests import HomePageTest

# get the directory path to output report file
result_dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
test_page = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
#home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_test and home_page_test
#smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

#定義測試案例的目錄為當前的目錄
# test_dir = './'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='ph*.py') #pattern 表示撈資料夾內所有ph開頭的py都加入測試


#建置測試集
suite = unittest.TestSuite()
suite.addTest(LoginTests('test_00001_Login'))
suite.addTest(LoginTests('test_00002_Logout'))
# suite.addTest(LoginTests('test_Error_invalid'))
# suite.addTests([LoginTests('test_Login'), LoginTests('test_Error_invalid')])

#執行測試
# runner = unittest.TextTestRunner()
# runner.run(suite)

# open the report file
outfile = open(result_dir +'\phlogin' +  time.strftime('_%Y%m%d_%H%M%S') + '.html', 'w')
# outfile = open(result_dir + '\phlogin.html', 'w')


# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                       title='PH Online Login Test Report',
                                       description='PH Login/Logout Test')


runner.run(suite)

# run the suite using HTMLTestRunner
# runner.run(suite)
# runner.run(discover)