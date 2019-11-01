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
        cls.driver.get('https://pholadminsd.pd.local/admin/auth/login')

        #For IE Only
        cls.driver.get("javascript:document.getElementById('overridelink').click();") 
        #Login
        cls.driver.find_element_by_id("UserLoginForm_username").clear()
        cls.driver.find_element_by_id("UserLoginForm_username").send_keys(acct)
        cls.driver.find_element_by_id("UserLoginForm_password").clear()
        cls.driver.find_element_by_id("UserLoginForm_password").send_keys(pw)
        cls.driver.find_element_by_name("yt0").click()

    #Swotch to Bank Statement - Detail time
    def test_00001_swbsdetail(self):
        
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        bs = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[1]/ul/li[5]/ul/li[1]/a/span[2]")
        bs.click()
        #Bank Statement - Detail
        bsd = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[1]/ul/li[5]/ul/li[1]/ul/li[1]/a/span")
        bsd.click()

        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            total = eTime - sTime
            print("\n"+"Switch to Reports > Bank Statement > Bank Statement - Detail cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds." )

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(4)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("report/bankStatement/index",url_now, msg="Wrong Page!")
        self.assertIn("Bank Statement - Detail",path, msg="Display Error!")
        self.assertIn("Detail",title, msg="Display Error!")

    #Swotch to Bank Statement - Summary
    def test_00002_swbssum(self):
        
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        bs = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[1]/ul/li[5]/ul/li[1]/a/span[2]")
        bs.click()
        #Bank Statement - Summary
        bsd = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/ul/li[5]/ul/li[1]/ul/li[2]/a/span")
        bsd.click()

        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            total = eTime - sTime
            print("\n"+"Switch to Reports > Bank Statement > Bank Statement - Summary cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds." )

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(4)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("report/bankStatement/summary",url_now, msg="Wrong Page!")
        self.assertIn("Bank Statement - Summary",path, msg="Display Error!")
        self.assertIn("Summary",title, msg="Display Error!")

    #Swotch to Raw Bank Statement Ledger
    def test_00003_swrbsl(self):
        
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        bs = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/ul/li[5]/ul/li[2]/a/span")
        bs.click()

        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            total = eTime - sTime
            print("\n"+"Switch to Reports > Raw Bank Statement Ledger cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds." )

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(3)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("rawBankStatement/index",url_now, msg="Wrong Page!")
        self.assertIn("Raw Bank Statement Ledger",path, msg="Display Error!")
        self.assertIn("Raw Bank Statement Ledger",title, msg="Display Error!")

    #Expire and Manual Accept Bank Record
    def test_00004_swemabr(self):   
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        bs = self.driver.find_element_by_xpath("//html/body/div[1]/div[1]/div[2]/div/div[1]/ul/li[5]/ul/li[3]/a/span")
        bs.click()

        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            total = eTime - sTime
            print("\n"+"Switch to Reports > Expire and Manual Accept Bank Record cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds." )

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(3)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("expiredStmtDetail/index",url_now, msg="Wrong Page!")
        self.assertIn("Expire and Manual Accept Bank Record",path, msg="Display Error!")
        self.assertIn("Expire and Manual",title, msg="Display Error!")

    #Unknown Bank Statement Detail
    def test_00005_swunbs(self):   
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        self.driver.find_element_by_link_text("Unknown Bank Statement Detail").click()
       
        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            total = eTime - sTime
            print("\n"+ "Switch to Reports > Unknown Bank Statement Detail cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds." )

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(3)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("unknownBankStatement/index",url_now, msg="Wrong Page!")
        self.assertIn("Unknown Bank Statement Detail",path, msg="Display Error!")
        self.assertIn("Unknown Bank",title, msg="Display Error!")
    #End the test, close the browser window
       
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
