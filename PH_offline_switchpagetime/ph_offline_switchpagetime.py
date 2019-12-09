import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from decimal import *
from common import ph

read = ph()
read.readfile()

unittest.total = 0

class switchpage(unittest.TestCase):

    #initiation for the test
    @classmethod
    def setUpClass(cls):
        
        cls.driver = read.webd()
        
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
            t01 = eTime - sTime
            print("\n"+"Switch to Reports > Bank Statement > Bank Statement - Detail cost " + str(Decimal(t01).quantize(Decimal('0.00'))) + " seconds." )

        unittest.total = unittest.total + t01

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
            t02 = eTime - sTime
            print("\n"+"Switch to Reports > Bank Statement > Bank Statement - Summary cost " + str(Decimal(t02).quantize(Decimal('0.00'))) + " seconds." )

        unittest.total = unittest.total + t02

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
            t03 = eTime - sTime
            print("\n"+"Switch to Reports > Raw Bank Statement Ledger cost " + str(Decimal(t03).quantize(Decimal('0.00'))) + " seconds." )

        unittest.total = unittest.total + t03

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
            t04 = eTime - sTime
            print("\n"+"Switch to Reports > Expire and Manual Accept Bank Record cost " + str(Decimal(t04).quantize(Decimal('0.00'))) + " seconds." )

        unittest.total = unittest.total + t04

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
            t05 = eTime - sTime
            print("\n"+ "Switch to Reports > Unknown Bank Statement Detail cost " + str(Decimal(t05).quantize(Decimal('0.00'))) + " seconds." )

        unittest.total = unittest.total + t05

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(3)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("unknownBankStatement/index",url_now, msg="Wrong Page!")
        self.assertIn("Unknown Bank Statement Detail",path, msg="Display Error!")
        self.assertIn("Unknown Bank",title, msg="Display Error!")
    
    #Deposit Transaction
    def test_00006_swdepost(self):   
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        self.driver.find_element_by_link_text("Deposit Transaction").click()
       
        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            t06 = eTime - sTime
            print("\n"+ "Switch to Reports > Deposit Transaction " + str(Decimal(t06).quantize(Decimal('0.00'))) + " seconds." )

        unittest.total = unittest.total + t06

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(3)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("/report/requestDetail",url_now, msg="Wrong Page!")
        self.assertIn("Deposit Transaction",path, msg="Display Error!")
        self.assertIn("Deposit Transaction",title, msg="Display Error!")

    #Payout Summary
    def test_00007_swpayout(self):   
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        self.driver.find_element_by_link_text("Payout Summary").click()
       
        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            t07 = eTime - sTime
            print("\n"+ "Switch to Reports > Payout Summary " + str(Decimal(t07).quantize(Decimal('0.00'))) + " seconds." )
        
        unittest.total = unittest.total + t07
        
        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(3)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("report/payoutSummary",url_now, msg="Wrong Page!")
        self.assertIn("Payout Summary",path, msg="Display Error!")
        self.assertIn("Payout Summary",title, msg="Display Error!")   

    #Payout Reconciliation Summary
    def test_00008_swpayoutrecon(self):   
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        self.driver.find_element_by_link_text("Payout Reconciliation Summary").click()
       
        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            t08 = eTime - sTime
            print("\n"+ "Switch to Reports > Payout Reconciliation Summary " + str(Decimal(t08).quantize(Decimal('0.00'))) + " seconds." )

        unittest.total = unittest.total + t08

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(3)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("report/payoutReconSummary",url_now, msg="Wrong Page!")
        self.assertIn("Payout Reconciliation",path, msg="Display Error!")
        self.assertIn("Payout Reconciliation Summary",title, msg="Display Error!")       
    
    #FxMark
    def test_00009_swFxMark(self):   
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        self.driver.find_element_by_link_text("FX Markup").click()
       
        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            t09 = eTime - sTime
            print("\n"+ "Switch to Reports > FX Markup " + str(Decimal(t09).quantize(Decimal('0.00'))) + " seconds." )

        unittest.total = unittest.total + t09

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(3)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("/report/fxMarkup",url_now, msg="Wrong Page!")
        self.assertIn("FX Markup",path, msg="Display Error!")
        self.assertIn("FX Markup Report",title, msg="Display Error!")

    #Pending Fund Balance
    def test_00010_swPendingFund(self):   
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        self.driver.find_element_by_link_text("Pending Fund Balance").click()
       
        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            t10 = eTime - sTime
            print("\n"+ "Switch to Reports > Pending Fund Balance " + str(Decimal(t10).quantize(Decimal('0.00'))) + " seconds." )

        unittest.total = unittest.total + t10

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(3)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("/report/pendingFundBal",url_now, msg="Wrong Page!")
        self.assertIn("Pending Fund Balance",path, msg="Display Error!")
        self.assertIn("Pending Fund Balance",title, msg="Display Error!")
    
    #Fee Summary
    def test_00011_swFeeSummary(self):   
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        self.driver.find_element_by_link_text("Fee Summary").click()
       
        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            t11 = eTime - sTime
            print("\n"+ "Switch to Reports > Fee Summary " + str(Decimal(t11).quantize(Decimal('0.00'))) + " seconds." )

        unittest.total = unittest.total + t11

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(3)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("/report/feeSummary",url_now, msg="Wrong Page!")
        self.assertIn("Fee Summary",path, msg="Display Error!")
        self.assertIn("Fee Summary",title, msg="Display Error!")        

    #Total Fee Summary
    def test_00012_swTotalFeeSummary(self):   
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        self.driver.find_element_by_link_text("Total Fee Summary").click()
       
        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            t12 = eTime - sTime
            print("\n"+ "Switch to Reports > Total Fee Summary " + str(Decimal(t12).quantize(Decimal('0.00'))) + " seconds." )

        unittest.total = unittest.total + t12

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(3)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("/report/totalFeeSummary",url_now, msg="Wrong Page!")
        self.assertIn("Total Fee Summary",path, msg="Display Error!")
        self.assertIn("Total Fee Summary",title, msg="Display Error!")  

    #Cost Summary
    def test_00013_swCostSummary(self):   
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        self.driver.find_element_by_link_text("Cost Summary").click()
       
        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            t13 = eTime - sTime
            print("\n"+ "Switch to Reports > Cost Summary " + str(Decimal(t13).quantize(Decimal('0.00'))) + " seconds." )

        unittest.total = unittest.total + t13

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(3)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("/report/costSummary",url_now, msg="Wrong Page!")
        self.assertIn("Cost Summary",path, msg="Display Error!")
        self.assertIn("Cost Summary",title, msg="Display Error!")
    
    #Total Cost Summary
    def test_00014_swTotalCostSummary(self):   
        #換頁前,先記錄時間
        sTime = time.time()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        self.driver.find_element_by_link_text("Total Cost Summary").click()
       
        if self.driver.find_element_by_css_selector("#content > h1"):
            eTime = time.time()
            t14 = eTime - sTime
            print("\n"+ "Switch to Reports > Total Cost Summary " + str(Decimal(t14).quantize(Decimal('0.00'))) + " seconds." )

        unittest.total = unittest.total + t14

        url_now = self.driver.current_url
        path = self.driver.find_element_by_css_selector("#page > div.breadcrumbs > span:nth-child(3)").text
        title = self.driver.find_element_by_css_selector("#content > h1").text      
        self.assertIn("/report/totalCostSummary",url_now, msg="Wrong Page!")
        self.assertIn("Total Cost Summary",path, msg="Display Error!")
        self.assertIn("Total Cost Summary",title, msg="Display Error!")

    def test_00020_TotalTime(self):   
        print("\n"+ "All case cost " + str(Decimal(unittest.total).quantize(Decimal('0.00'))) + " seconds." )

    #End the test, close the browser window
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
