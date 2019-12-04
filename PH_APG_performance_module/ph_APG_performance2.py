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

class APGTimeTests(unittest.TestCase):

    #initiation for the test
    @classmethod
    def setUpClass(cls):
       
        
        cls.driver = read.webd()
        #self.read.driver = read.webd()
       

        # data = read.login()
        
        # dir = os.getcwd()
        # ie_driver_path = dir + '\IEDriverServer.exe'
        # # create a new Internet Explorer session
        # cls.driver = webdriver.Ie(ie_driver_path)
        # cls.driver.implicitly_wait(360)
        # cls.driver.maximize_window()
        # cls.driver.get('https://tadmin.xx217569.com/admin/auth/login')

        # #For IE Only
        #cls.driver.get("javascript:document.getElementById('overridelink').click();") 
        #Login
        # cls.driver.find_element_by_id("UserLoginForm_username").clear()
        # cls.driver.find_element_by_id("UserLoginForm_username").send_keys(data[0][1])
        # cls.driver.find_element_by_id("UserLoginForm_password").clear()
        # cls.driver.find_element_by_id("UserLoginForm_password").send_keys(data[1][1])
        # cls.driver.find_element_by_name("yt0").click()

    # #Deposit Bank Statement - Detail
    def test_00001_bsdetail(self):
        
        date_a = read.date_a()
        sd = date_a[0][1]
        ed = date_a[1][1]
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        bs = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[1]/ul/li[5]/ul/li[1]/a/span[2]")
        bs.click()
        #Bank Statement - Detail
        bsd = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[1]/ul/li[5]/ul/li[1]/ul/li[1]/a/span")
        bsd.click()

        self.driver.find_element_by_id("START_DATE").clear()
        self.driver.find_element_by_id("START_DATE").send_keys(sd)
        self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div[3]/button[2]").click()
        self.driver.find_element_by_id("END_DATE").clear()
        self.driver.find_element_by_id("END_DATE").send_keys(ed)
        self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div[3]/button[2]").click()
        #Search前 先記錄時間
        sTime = time.time()
        self.driver.find_element_by_id("btn_Search").click()     
        show = self.driver.find_element_by_css_selector("#statement-detail-grid > div.summary").text
        url_now = self.driver.current_url
        title = self.driver.find_element_by_css_selector("#content > h1").text

        #有找到Table中的元素(view圖示),table出來才算搜尋結束
        try: 
            if self.driver.find_element_by_css_selector("#statement-detail-grid > table > tbody > tr:nth-child(1) > td:nth-child(22) > a > img"):      
            #if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[22]/a/img"):
                #Search後找到element,記錄時間
                eTime = time.time()
                total = eTime - sTime
                if total > 120.00:
                    self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
                    print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                    print("Reports > Deposit Bank Statement - Detail search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
                else:
                    print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                    print("Reports > Deposit Bank Statement - Detail search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
        except:
            print("Time out!")
        self.assertIn("report/bankStatement",url_now, msg="Wrong Page!")
        self.assertIn("Displaying",show, msg="Display Error!")
        self.assertIn("Detail",title, msg="Display Error!")
        time.sleep(3)

    #Bank Statement - Summary Performance
    def test_00002_bssummary(self):
        date_a = read.date_a()
        sd = date_a[0][1]
        ed = date_a[1][1]
        t = True
        f = False
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        bs = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[1]/ul/li[5]/ul/li[1]/a/span[2]")
        bs.click()
        #Bank Statement - Summary
        bsd = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/ul/li[5]/ul/li[1]/ul/li[2]/a/span")
        bsd.click()
        self.driver.find_element_by_id("START_DATE").clear()
        self.driver.find_element_by_id("START_DATE").send_keys(sd)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
        self.driver.find_element_by_id("END_DATE").clear()
        self.driver.find_element_by_id("END_DATE").send_keys(ed)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
        #Search前 先記錄時間
        sTime = time.time()
        self.driver.find_element_by_id("btn_Search").click()

        show = self.driver.find_element_by_css_selector("#statement-detail-baid-grid > div.summary").text
        url_now = self.driver.current_url
        title = self.driver.find_element_by_css_selector("#content > h1").text
        
        
        #有找到Table中的元素,table出來才算搜尋結束,搜尋超過120秒即failed
        if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/table/thead/tr/th[1]/a"):
            eTime = time.time()
            total = eTime - sTime
            if total > 120.00:
                self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
                print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                print("Reports > Bank Statement - Summary search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
            else:
                print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                print("Reports > Bank Statement - Summary search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
                
        self.assertIn("bankStatement/summary",url_now, msg="Wrong Page!")
        self.assertIn("Displaying",show, msg="Display Error!")
        self.assertIn("Summary",title, msg="Display Error!")
        time.sleep(3)

    #Raw Bank Statement Ledger
    def test_00003_rawbsledger(self):
        date_a = read.date_a()
        sd = date_a[0][1]
        ed = date_a[1][1]
        t = True
        f = False
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        self.driver.find_element_by_link_text("Raw Bank Statement Ledger").click()
                
        self.driver.find_element_by_id("START_DATE").clear()
        self.driver.find_element_by_id("START_DATE").send_keys(sd)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
        self.driver.find_element_by_id("END_DATE").clear()
        self.driver.find_element_by_id("END_DATE").send_keys(ed)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
        #Search前 先記錄時間
        sTime = time.time()
        self.driver.find_element_by_id("btn_Search").click() 
        show = self.driver.find_element_by_css_selector("#statement-ledger-grid > div.summary").text
        url_now = self.driver.current_url
        title = self.driver.find_element_by_css_selector("#content > h1").text
        
        #有找到Table中的元素(view圖示),table出來才算搜尋結束,搜尋超過120秒即failed

        if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[9]"):
            eTime = time.time()
            total = eTime - sTime
            if total > 120.00:
                self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
                print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                print("Reports > Raw Bank Statement Ledger search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
            else:
                print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                print("Reports > Raw Bank Statement Ledger search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
        self.assertIn("/rawBankStatement/index",url_now, msg="Wrong Page!")
        self.assertIn("Displaying",show, msg="Display Error!")
        self.assertIn("Ledger",title, msg="Display Error!") 
        time.sleep(3)
        
    #Expire and Manual Accept Bank Record
    def test_00004_expirerrecord(self):
        date_a = read.date_a()
        sd = date_a[0][1]
        ed = date_a[1][1]
        t = True
        f = False
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        self.driver.find_element_by_link_text("Expire and Manual Accept Bank Record").click()
                
        self.driver.find_element_by_id("START_DATE").clear()
        self.driver.find_element_by_id("START_DATE").send_keys(sd)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
        self.driver.find_element_by_id("END_DATE").clear()
        self.driver.find_element_by_id("END_DATE").send_keys(ed)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
        #Search前 先記錄時間
        sTime = time.time()
        self.driver.find_element_by_id("btn_Search").click() 
        show = self.driver.find_element_by_css_selector("#statement-detail-grid > div.summary").text
        url_now = self.driver.current_url
        title = self.driver.find_element_by_css_selector("#content > h1").text
        
        #有找到Table中的元素(view圖示),table出來才算搜尋結束,搜尋超過120秒即failed

        if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[18]/a/img"):
            eTime = time.time()
            total = eTime - sTime
            if total > 120.00:
                self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
                print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                print("Reports > Expire and Manual Accept Bank Record search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
            else:
                print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                print("Reports > Expire and Manual Accept Bank Record search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
        self.assertIn("expiredStmtDetail/index",url_now, msg="Wrong Page!")
        self.assertIn("Displaying",show, msg="Display Error!")
        self.assertIn("Expire and Manual",title, msg="Display Error!") 

    # # #Unknown Bank Statement Detail
    # # # def test_00005_ unknowbs(self):
    # # #     settc1()
    # # #     settc2()
    # # #     t = True
    # # #     f = False
    # # #     self.driver.find_element_by_link_text("Reports").click()
    # # #     #Bank Statement
    # # #     self.driver.find_element_by_link_text("Unknown Bank Statement Detail").click()
                
    # # #     self.driver.find_element_by_id("START_DATE").clear()
    # # #     self.driver.find_element_by_id("START_DATE").send_keys(sdate)
    # # #     self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
    # # #     self.driver.find_element_by_id("END_DATE").clear()
    # # #     self.driver.find_element_by_id("END_DATE").send_keys(edate)
    # # #     self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
    # # #     #Search前 先記錄時間
    # # #     sTime = time.time()
    # # #     self.driver.find_element_by_id("btn_Search").click() 
    # # #     show = self.driver.find_element_by_css_selector("#statement-detail-grid > div.summary").text
    # # #     url_now = self.driver.current_url
    # # #     title = self.driver.find_element_by_css_selector("#content > h1").text
        
    # # #     #有找到Table中的元素(view圖示),table出來才算搜尋結束,搜尋超過120秒即failed

    # # #     if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[18]/a/img"):
    # # #         eTime = time.time()
    # # #         total = eTime - sTime
    # # #         if total > 120.00:
    # # #             self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
    # # #             print("Search Condition: \nStart Date: "+ sdate + "\n" + "End Date: "+ edate)
    # # #             print("Reports > Expire and Manual Accept Bank Record search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
    # # #         else:
    # # #             print("Search Condition: \nStart Date: "+ sdate + "\n" + "End Date: "+ edate)
    # # #             print("Reports > Expire and Manual Accept Bank Record search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
    # # #     self.assertIn("expiredStmtDetail/index",url_now, msg="Wrong Page!")
    # # #     self.assertIn("Displaying",show, msg="Display Error!")
    # # #     self.assertIn("Ledger",title, msg="Display Error!") 

    #Bank Statement - Detail Performance
    def test_00006_dpstran(self):
        date_a = read.date_a()
        sd = date_a[0][1]
        ed = date_a[1][1]
        t = True
        f = False
        self.driver.find_element_by_link_text("Reports").click()
        #Deposit Transaction
        self.driver.find_element_by_link_text("Deposit Transaction").click()
        self.driver.find_element_by_id("START_DATE").clear()
        self.driver.find_element_by_id("START_DATE").send_keys(sd)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
        self.driver.find_element_by_id("END_DATE").clear()
        self.driver.find_element_by_id("END_DATE").send_keys(ed)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
        #Search前 先記錄時間
        sTime = time.time()
        self.driver.find_element_by_id("btn_Search").click() 
        show = self.driver.find_element_by_css_selector("#statement-detail-grid > div.summary").text
        url_now = self.driver.current_url

        #有找到Table中的元素(view圖示),table出來才算搜尋結束,搜尋超過120秒即failed

        if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/table/tbody/tr[1]/td[25]/a[1]/img"):
            eTime = time.time()
            total = eTime - sTime
            if total > 120.00:
                self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
                print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                print("Reports > Deposit Transactions search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
            else:
                print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                print("Reports > Deposit Transactions search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
        self.assertIn("report/requestDetail",url_now, msg="Wrong Page!")
        self.assertIn("Displaying",show, msg="Display Error!")

    #MID & BAID Transaction History
    def test_00007_dpstranh(self):
        date_a = read.date_a()
        sd = date_a[0][1]
        ed = date_a[1][1]
        t = True
        f = False
        self.driver.find_element_by_link_text("Reports").click()
        #Deposit Transaction
        self.driver.find_element_by_link_text("MID & BAID Transaction History").click()
        self.driver.find_element_by_id("START_DATE").clear()
        self.driver.find_element_by_id("START_DATE").send_keys(sd)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
        self.driver.find_element_by_id("END_DATE").clear()
        self.driver.find_element_by_id("END_DATE").send_keys(ed)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
        #Search前 先記錄時間
        sTime = time.time()
        self.driver.find_element_by_id("btn_Search").click() 
        show = self.driver.find_element_by_css_selector("#txn-header-grid > div.summary").text
        url_now = self.driver.current_url
        title = self.driver.find_element_by_css_selector("#content > h1").text

        #有找到Table中的元素(view圖示),table出來才算搜尋結束,搜尋超過120秒即failed
        if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[18]/a/img"):
            eTime = time.time()
            total = eTime - sTime
            if total > 120.00:
                self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
                print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                print("Reports > MID & BAID Transaction History search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
            else:
                print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                print("Reports > MID & BAID Transaction History search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
        self.assertIn("txnHistory/index",url_now, msg="Wrong Page!")
        self.assertIn("Displaying",show, msg="Display Error!")
        self.assertIn("MID & BAID",title, msg="Display Error!")
    
    #Deposit Transaction Performance
    def test_00008_dpstranper(self):
        date_a = read.date_a()
        sd = date_a[0][1]
        ed = date_a[1][1]
        t = True
        f = False
        self.driver.find_element_by_link_text("Reports").click()
        #Deposit Transaction
        self.driver.find_element_by_link_text("Deposit Transaction Performance").click()
        self.driver.find_element_by_id("START_DATE").clear()
        self.driver.find_element_by_id("START_DATE").send_keys(sd)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
        self.driver.find_element_by_id("END_DATE").clear()
        self.driver.find_element_by_id("END_DATE").send_keys(ed)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
        #Search前 先記錄時間
        sTime = time.time()
        self.driver.find_element_by_id("btn_Search").click() 
        show = self.driver.find_element_by_css_selector("#txn-perform-grid > div.summary").text
        url_now = self.driver.current_url
        title = self.driver.find_element_by_css_selector("#content > h1").text
        #有找到Table中的元素(view圖示),table出來才算搜尋結束,搜尋超過120秒即failed
        try:
            if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/table/thead/tr/th[17]/a"):
                eTime = time.time()
                total = eTime - sTime
                if total > 120.00:
                    self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
                    print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                    print("Reports > Deposit Transaction Performance search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
                else:
                    print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                    print("Reports > Deposit Transaction Performance search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
        except:
            print("Time Out!")
        self.assertIn("txnPerform/index",url_now, msg="Wrong Page!")
        self.assertIn("Displaying",show, msg="Display Error!")
        self.assertIn("Deposit Transaction",title, msg="Display Error!")

    #Payout Summary
    def test_00009_payoutSummary(self):
        date_b = read.date_b()
        sd2 = date_b[0][1]
        ed2 = date_b[1][1]
        t = True
        f = False
        self.driver.find_element_by_link_text("Reports").click()
        #Deposit Transaction
        self.driver.find_element_by_link_text("Payout Summary").click()
        self.driver.find_element_by_id("OfflinePayoutSummaryReportDetail_FM_TXN_DATE").clear()
        self.driver.find_element_by_id("OfflinePayoutSummaryReportDetail_FM_TXN_DATE").send_keys(sd2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/h1").click()
        self.driver.find_element_by_id("OfflinePayoutSummaryReportDetail_TO_TXN_DATE").clear()
        self.driver.find_element_by_id("OfflinePayoutSummaryReportDetail_TO_TXN_DATE").send_keys(ed2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/h1").click()
        #Search前 先記錄時間
        sTime = time.time()
        self.driver.find_element_by_id("btn_search").click() 
        show = self.driver.find_element_by_css_selector("#payoutSummary-grid > div.summary").text
        url_now = self.driver.current_url
        title = self.driver.find_element_by_css_selector("#content > h1").text
        #有找到Table中的元素(view圖示),table出來才算搜尋結束,搜尋超過120秒即failed
        try:
            if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[1]"):
                eTime = time.time()
                total = eTime - sTime
                if total > 120.00:
                    self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
                    print("Search Condition: \nStart Date: "+ sd2 + "\n" + "End Date: "+ ed2)
                    print("Reports > Payout Summary search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
                else:
                    print("Search Condition: \nStart Date: "+ sd2 + "\n" + "End Date: "+ ed2)
                    print("Reports > Payout Summary search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
        except:
            print("Time Out!")
        self.assertIn("payoutSummary/index",url_now, msg="Wrong Page!")
        self.assertIn("Displaying",show, msg="Display Error!")
        self.assertIn("Payout Summary",title, msg="Display Error!")
    
    # #Payout Reconciliation Summary
    # # def test_00010_payoutRecon(self):
    # #     settc1()
    # #     settc3()
    # #     t = True
    # #     f = False
    # #     self.driver.find_element_by_link_text("Reports").click()
    # #     #Deposit Transaction
    # #     self.driver.find_element_by_link_text("Payout Reconciliation Summary").click()
    # #     self.driver.find_element_by_id("START_DATE").clear()
    # #     self.driver.find_element_by_id("START_DATE").send_keys(sdate2)
    # #     self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
    # #     self.driver.find_element_by_id("END_DATE").clear()
    # #     self.driver.find_element_by_id("END_DATE").send_keys(edate2)
    # #     self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
    # #     #Search前 先記錄時間
    # #     sTime = time.time()
    # #     self.driver.find_element_by_id("btn_Search").click() 
    # #     show = self.driver.find_element_by_css_selector("#payout-recon-summary-grid > div.summary").text
    # #     url_now = self.driver.current_url
    # #     title = self.driver.find_element_by_css_selector("#content > h1").text
    # #     #有找到Table中的元素(view圖示),table出來才算搜尋結束,搜尋超過120秒即failed

    # #     if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[1]"):
    # #         eTime = time.time()
    # #         total = eTime - sTime
    # #         if total > 120.00:
    # #             self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
    # #             print("Search Condition: \nStart Date: "+ sdate2 + "\n" + "End Date: "+ edate2)
    # #             print("Reports > Payout Reconciliation Summary search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
    # #         else:
    # #             print("Search Condition: \nStart Date: "+ sdate2 + "\n" + "End Date: "+ edate2)
    # #             print("Reports > Payout Reconciliation Summary search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
    # #     self.assertIn("/payoutReconSummary/index",url_now, msg="Wrong Page!")
    # #     self.assertIn("Displaying",show, msg="Display Error!")
    # #     self.assertIn("Payout Reconciliation",title, msg="Display Error!")

    # #Fx MarkUp
    def test_00011_fxmarkup(self):
        date_a = read.date_a()
        sd = date_a[0][1]
        ed = date_a[1][1]
        prov1 = read.provider()
        pro = prov1[0][1]
        
        t = True
        f = False
        self.driver.find_element_by_link_text("Reports").click()
        self.driver.find_element_by_link_text("FX Markup").click()
        
        self.driver.find_element_by_id("START_DATE").clear()
        self.driver.find_element_by_id("START_DATE").send_keys(sd)
        self.driver.find_element_by_xpath("//*[@id='content']/h1").click()
        self.driver.find_element_by_id("END_DATE").clear()
        self.driver.find_element_by_id("END_DATE").send_keys(ed)
        self.driver.find_element_by_xpath("//*[@id='content']/h1").click()
		#Search前 先記錄時間
        sTime = time.time()
        self.driver.find_element_by_id("btn_search").click()
        #show = self.driver.find_element_by_css_selector("#detail-grid > div.summary").text
        url_now = self.driver.current_url
        title = self.driver.find_element_by_css_selector("#content > h1").text
        #有找到Table中的元素(view圖示),table出來才算搜尋結束,搜尋超過120秒即failed

        if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/table/thead/tr/th[1]/a"):
            eTime = time.time()
            total = eTime - sTime
            if total > 120.00:
                self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
                print("Search Condition: \nProvider: "+ pro)
                print("Reports > FX Markup Report search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
            else:
                print("Search Condition: \nProvider: "+ pro)
                print("Reports > FX Markup Report search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
        self.assertIn("fxMarkup/index",url_now, msg="Wrong Page!")
        #self.assertIn("Displaying",show, msg="Display Error!")
        self.assertIn("FX Markup Report",title, msg="Display Error!")

    # #Pending Fund Balance
    def test_00012_PFbalance(self):
        prov1 = read.provider()
        pro = prov1[0][1]
        t = True
        f = False
        self.driver.find_element_by_link_text("Reports").click()
        self.driver.find_element_by_link_text("Pending Fund Balance").click()
        select = Select(self.driver.find_element_by_name('CLIENT_ID'))
        select.select_by_visible_text(pro)
		
		#Search前 先記錄時間
        sTime = time.time()
        self.driver.find_element_by_id("btn_Search").click() 
        show = self.driver.find_element_by_css_selector("#detail-grid > div.summary").text
        url_now = self.driver.current_url
        title = self.driver.find_element_by_css_selector("#content > h1").text
        #有找到Table中的元素(view圖示),table出來才算搜尋結束,搜尋超過120秒即failed

        if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/table/tbody/tr/td[2]"):
            eTime = time.time()
            total = eTime - sTime
            if total > 120.00:
                self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
                print("Search Condition: \nProvider: "+ pro)
                print("Reports > Pending Fund Balance search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
            else:
                print("Search Condition: \nProvider: "+ pro)
                print("Reports > Pending Fund Balance search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
        self.assertIn("pendingFundBal/index",url_now, msg="Wrong Page!")
        self.assertIn("Displaying",show, msg="Display Error!")
        self.assertIn("Pending Fund Balance",title, msg="Display Error!")
    
    #Cost fee Summary
    def test_00013_feeSum(self):
        date_a = read.date_a()
        sd = date_a[0][1]
        ed = date_a[1][1]
        t = True
        f = False
        self.driver.find_element_by_link_text("Reports").click()
        #Deposit Transaction
        self.driver.find_element_by_link_text("Fee Summary").click()
        self.driver.find_element_by_id("START_DATE").clear()
        self.driver.find_element_by_id("START_DATE").send_keys(sd)
        self.driver.find_element_by_xpath("//*[@id='content']/h1").click()
        self.driver.find_element_by_id("END_DATE").clear()
        self.driver.find_element_by_id("END_DATE").send_keys(ed)
        self.driver.find_element_by_xpath("//*[@id='content']/h1").click()
        #Search前 先記錄時間
        sTime = time.time()
        self.driver.find_element_by_id("btn_search").click() 
        #show = self.driver.find_element_by_css_selector("#total-amt-grid > div.summary").text
        url_now = self.driver.current_url
        title = self.driver.find_element_by_css_selector("#content > h1").text
        #有找到Table中的元素(view圖示),table出來才算搜尋結束,搜尋超過120秒即failed

        if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/table/thead/tr/th[1]/a"):
            eTime = time.time()
            total = eTime - sTime
            if total > 120.00:
                self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
                print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                print("Reports > Fee Summary cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
            else:
                print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                print("Reports > Fee Summary search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
        self.assertIn("feeSummary/index",url_now, msg="Wrong Page!")
        #self.assertIn("Displaying",show, msg="Display Error!")
        self.assertIn("Fee Summary",title, msg="Display Error!")

    #Total Cost fee
    def test_00014_totalfeeSum(self):

        t = True
        f = False
        self.driver.find_element_by_link_text("Reports").click()
        #Deposit Transaction
        self.driver.find_element_by_link_text("Total Fee Summary").click()
        
        #Search前 先記錄時間
        sTime = time.time()
        self.driver.find_element_by_id("btn_search").click() 
        show = self.driver.find_element_by_css_selector("#total-amt-grid > div.summary").text
        url_now = self.driver.current_url
        title = self.driver.find_element_by_css_selector("#content > h1").text
        #有找到Table中的元素(view圖示),table出來才算搜尋結束,搜尋超過120秒即failed

        if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/table/tbody/tr[1]/td[1]"):
            eTime = time.time()
            total = eTime - sTime
            if total > 120.00:
                self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
                #print("Search Condition: \nStart Date: "+ sdate2 + "\n" + "End Date: "+ edate2)
                print("Reports > Total Fee Summary cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
            else:
                #print("Search Condition: \nStart Date: "+ sdate2 + "\n" + "End Date: "+ edate2)
                print("Reports > Total Fee Summary search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
        self.assertIn("totalFeeSummary/index",url_now, msg="Wrong Page!")
        self.assertIn("Displaying",show, msg="Display Error!")
        self.assertIn("Total Fee Summary",title, msg="Display Error!")

    #Cost Summary
    def test_00015_costsum(self):
        date_a = read.date_a()
        sd = date_a[0][1]
        ed = date_a[1][1]
        t = True
        f = False
        self.driver.find_element_by_link_text("Reports").click()
        #Deposit Transaction
        self.driver.find_element_by_link_text("Cost Summary").click()
        self.driver.find_element_by_id("sDate").clear()
        self.driver.find_element_by_id("sDate").send_keys(sd)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
        self.driver.find_element_by_id("eDate").clear()
        self.driver.find_element_by_id("eDate").send_keys(ed)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
        #Search前 先記錄時間
        sTime = time.time()
        self.driver.find_element_by_id("btn_Search").click() 
        show = self.driver.find_element_by_css_selector("#psp-cost-summary-grid > div.summary").text
        url_now = self.driver.current_url
        title = self.driver.find_element_by_css_selector("#content > h1").text
        #有找到Table中的元素(view圖示),table出來才算搜尋結束,搜尋超過120秒即failed

        if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/table/tbody/tr[1]/td[1]"):
            eTime = time.time()
            total = eTime - sTime
            if total > 120.00:
                self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
                print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                print("Reports > Cost Summary search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
            else:
                print("Search Condition: \nStart Date: "+ sd + "\n" + "End Date: "+ ed)
                print("Reports > Cost Summary search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
        self.assertIn("costSummary/index",url_now, msg="Wrong Page!")
        self.assertIn("Displaying",show, msg="Display Error!")
        self.assertIn("Cost Summary",title, msg="Display Error!")
    
    #Total Cost Summary
    def test_00016_totalcostsum(self):
        t = True
        f = False
        self.driver.find_element_by_link_text("Reports").click()
        #Deposit Transaction
        self.driver.find_element_by_link_text("Total Cost Summary").click()
        
        #Search前 先記錄時間
        sTime = time.time()
        self.driver.find_element_by_id("btn_Search").click() 
        show = self.driver.find_element_by_css_selector("#psp-cost-summary-grid > div.summary").text
        url_now = self.driver.current_url
        title = self.driver.find_element_by_css_selector("#content > h1").text
        #有找到Table中的元素(view圖示),table出來才算搜尋結束,搜尋超過120秒即failed

        if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/table/tbody/tr[1]/td[1]"):
            eTime = time.time()
            total = eTime - sTime
            if total > 120.00:
                self.assertTrue(f,msg='Warring!!! Loading cost over 120 seconds!')
                #print("Search Condition: \nStart Date: "+ sdate + "\n" + "End Date: "+ edate)
                print("Reports > Total Cost Summary search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
            else:
                #print("Search Condition: \nStart Date: "+ sdate + "\n" + "End Date: "+ edate)
                print("Reports > Total Cost Summary search cost " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
        self.assertIn("totalCostSummary/index",url_now, msg="Wrong Page!")
        self.assertIn("Displaying",show, msg="Display Error!")
        self.assertIn("Total Cost Summary",title, msg="Display Error!")

    #End the test, close the browser window
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)
