import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from decimal import *

TC1 = []
TC2 = []

if os.path.isfile('switchpage.csv'):
    print('找到目標檔案 switchpage.csv')
    #讀取檔案
    with open('switchpage.csv', 'r',encoding = 'utf-8', errors = "ignore") as f:
        for line in f:
			# if 'login' in line: continue #繼續,跳到下一迴()
            s = line.strip().split(',') # split(',')就是遇到','就切一刀下去變成兩個欄位
            case = s[0]
            item = s[1]
            data = s[2]
            if case == 'login':
                TC1.append([item, data])

def settc1():
    global acct, pw, name
    acct     = TC1[0][1]
    pw       = TC1[1][1]
    name     = TC1[2][1]



class switchpage(unittest.TestCase):

    #initiation for the test
    @classmethod
    def setUpClass(cls):
        settc1()
        dir = os.getcwd()
        ie_driver_path = dir + '\IEDriverServer.exe'
        # create a new Internet Explorer session
        cls.driver = webdriver.Ie(ie_driver_path)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('https://phadminsd.pd.local/admin/auth/login')

        #For IE Only
        cls.driver.get("javascript:document.getElementById('overridelink').click();") 
        #Login
        cls.driver.find_element_by_id("UserLoginForm_username").clear()
        cls.driver.find_element_by_id("UserLoginForm_username").send_keys(acct)
        cls.driver.find_element_by_id("UserLoginForm_password").clear()
        cls.driver.find_element_by_id("UserLoginForm_password").send_keys(pw)
        cls.driver.find_element_by_name("yt0").click()

    #Swotch to Bank Statement - Detail time
    def test_00001_swmidpid(self):
        
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        self.driver.find_element_by_link_text("MID & PID Transaction History").click()
 

        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            total = eTime - sTime
            print("\n"+"Switch to Reports > MID & PID Transaction History cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds." )

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("txnHistory/index",url_now, msg="Wrong Page!")
        self.assertIn("MID & PID",path, msg="Display Error!")
        self.assertIn("MID & PID Transaction",title, msg="Display Error!")

    #Swotch to Bank Statement - Summary
    def test_00002_swdpsp(self):
        
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        self.driver.find_element_by_link_text("Deposit Performance").click()

        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            total = eTime - sTime
            print("\n"+"Switch to Reports > Deposit Performance cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds." )

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("depositPerf/summary",url_now, msg="Wrong Page!")
        self.assertIn("Deposit Performance",path, msg="Display Error!")
        self.assertIn("Deposit Performance",title, msg="Display Error!")

    #Swotch to Raw Bank Statement Ledger
    def test_00003_swrbsl(self):
        
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        self.driver.find_element_by_link_text("Payout Summary").click()

        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            total = eTime - sTime
            print("\n"+"Switch to Reports > Payout Summary Report cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds." )

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("payoutSummary/index",url_now, msg="Wrong Page!")
        self.assertIn("Payout Summary Report",path, msg="Display Error!")
        self.assertIn("Payout Summary",title, msg="Display Error!")

    
       
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
