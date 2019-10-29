import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from decimal import *

TC1 = []
TC2 = []

if os.path.isfile('caltime.csv'):
    print('找到目標檔案 caltime.csv')
    #讀取檔案
    with open('caltime.csv', 'r',encoding = 'utf-8', errors = "ignore") as f:
        for line in f:
			# if 'login' in line: continue #繼續,跳到下一迴()
            s = line.strip().split(',') # split(',')就是遇到','就切一刀下去變成兩個欄位
            case = s[0]
            item = s[1]
            data = s[2]
            if case == 'login':
                TC1.append([item, data])
            elif case == 'time':
                TC2.append([item, data])


def settc1():
    global acct, pw, name
    acct     = TC1[0][1]
    pw       = TC1[1][1]
    name     = TC1[2][1]
   

def settc2():
    global sdate, provider,edate
    sdate     = TC2[0][1]
    edate     = TC2[1][1]
    provider  = TC2[2][1]


class TimeTests(unittest.TestCase):

    #initiation for the test
    @classmethod
    def setUp(self):
        settc1()
        dir = os.getcwd()
        ie_driver_path = dir + '\IEDriverServer.exe'
        # create a new Internet Explorer session
        self.driver = webdriver.Ie(ie_driver_path)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://pholadminsd.pd.local/admin/auth/login')

        #For IE Only
        self.driver.get("javascript:document.getElementById('overridelink').click();") 
        #Login
        self.driver.find_element_by_id("UserLoginForm_username").clear()
        self.driver.find_element_by_id("UserLoginForm_username").send_keys(acct)
        self.driver.find_element_by_id("UserLoginForm_password").clear()
        self.driver.find_element_by_id("UserLoginForm_password").send_keys(pw)
        self.driver.find_element_by_name("yt0").click()

    #Bank Statement - Detail Performance
    def test_00001_bsdetail(self):
        settc1()
        settc2()
        self.driver.find_element_by_link_text("Reports").click()
        #Bank Statement
        bs = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/ul/li[5]/ul/li[1]/a/span[2]")
        bs.click()
        #ActionChains(self.driver).move_to_element(bs).click()
        #Bank Statement - Detail
        bsd = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/ul/li[5]/ul/li[1]/ul/li[1]/a/span")
        bsd.click()
        #ActionChains(self.driver).move_to_element(bsd).perform()
        self.driver.find_element_by_id("START_DATE").clear()
        self.driver.find_element_by_id("START_DATE").send_keys(sdate)
        self.driver.find_element_by_id("END_DATE").clear()
        self.driver.find_element_by_id("END_DATE").send_keys(edate)
        select = Select(self.driver.find_element_by_name('BANK_ACCT_PROVIDER_ID'))
        select.select_by_visible_text(provider)
        #time.sleep(5)
        self.driver.find_element_by_id("btn_Search").click()
        #Search前 先記錄時間
        sTime = time.time()

        #有找到Table中的元素(view圖示),table出來才算搜尋結束        
        if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[22]/a/img"):
            #Search後找到element,記錄時間
            eTime = time.time()
            print("Search Condition: \n Start Date: "+ sdate + "\n" + "End Date: "+ edate + "\n" + "Provider: "+provider)
            print("*** Bank Statement - Detail search cost " + str(Decimal(eTime - sTime).quantize(Decimal('0.00'))) + "seconds.***")
        time.sleep(1)
    
    #Deposit Bank Statement Performance
    def test_00002_bsmana(self):
        settc1()
        settc2()
        self.driver.find_element_by_link_text("Transactions").click()
        #Bank Statement
        dbs = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/ul/li[6]/ul/li[2]/a/span[2]")
        dbs.click()
        #Deposit Bank Statement
        dsm = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/ul/li[6]/ul/li[2]/ul/li[2]/a/span")    
        dsm.click()
        self.driver.find_element_by_xpath("//*[@id='content']/a[1]").click()
        self.driver.find_element_by_id("START_DATE").clear()
        self.driver.find_element_by_id("START_DATE").send_keys(sdate)
        self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div[3]/button[2]").click()
        self.driver.find_element_by_id("END_DATE").clear()
        self.driver.find_element_by_id("END_DATE").send_keys(edate)
        self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div[3]/button[2]").click()
        self.driver.find_element_by_id("btn_Search").click()
        #Search前 先記錄時間
        sTime = time.time()

        #有找到Table中的元素(view圖示),table出來才算搜尋結束       
        if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[18]/a/img"):
            #Search後找到element,記錄時間
            eTime = time.time()
            print("Search Condition: \n" + "Start Date: "+ sdate + "\n" + "End Date: "+ edate)
            print("*** Deposit Bank Statement search cost " + str(Decimal(eTime - sTime).quantize(Decimal('0.00'))) + "seconds.***")
        time.sleep(1)
    
    def test_00003_deposittran(self):
        settc1()
        settc2()
        self.driver.find_element_by_link_text("Reports").click()
        self.driver.find_element_by_link_text("Deposit Transaction").click()
        self.driver.find_element_by_id("START_DATE").clear()
        self.driver.find_element_by_id("START_DATE").send_keys(sdate)
        self.driver.find_element_by_id("END_DATE").clear()
        self.driver.find_element_by_id("END_DATE").send_keys(edate)
        self.driver.find_element_by_id("btn_Search").click()

        sTime = time.time()

        if self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/table/tbody/tr[1]/td[25]/a/img"):
            eTime = time.time()
            print("Search Condition: \n" + "Start Date: "+ sdate+ "\n" +"End Date: "+ edate)
            print("*** Deposit Transation search cost " + str(Decimal(eTime - sTime).quantize(Decimal('0.00'))) + "seconds.***")
        time.sleep(1)
        
    #End the test, close the browser window
    @classmethod
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)
