import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

TC1 = []
TC2 = []
if os.path.isfile('bank.csv'):
    print('找到目標檔案')
    #讀取檔案
    with open('bank.csv', 'r',encoding = 'utf-8', errors = "ignore") as f:
        for line in f:
            s = line.strip().split(',')
            case = s[0]
            item = s[1]
            data = s[2]
            if case == 'bankacct':
                TC1.append([item, data])
            elif case == 'login':
                TC2.append([item, data])
else:
    print('找不到檔案...')


def setting(i):
    global bap, bn, ban, cur, bana,owner, prov, city, branch, sswitch, sms, remark, date
    print("Bank Account:")
    bap     = TC1[i][1]
    bn      = TC1[i+1][1]
    ban     = TC1[i+2][1]
    cur     = TC1[i+3][1]
    bana    = TC1[i+4][1]
    owner   = TC1[i+5][1]
    prov    = TC1[i+6][1]
    city    = TC1[i+7][1]
    branch  = TC1[i+8][1]
    sswitch = TC1[i+9][1]
    sms     = TC1[i+10][1]         
    remark  = TC1[i+11][1]
    date    = TC1[i+12][1]

class bankacct(unittest.TestCase):

    #initiation for the test
    def setUp(self):
        dir = os.getcwd()
        ie_driver_path = dir +'\IEDriverServer.exe'
        # create a new Internet Explorer session
        self.driver = webdriver.Ie(ie_driver_path)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://pholadminsd.pd.local/admin/auth/login')

        #For IE Only
        #self.driver.find_element_by_xpath("//*[@id='moreInfoContainer']/A").click()
        #self.driver.find_element_by_xpath("//*[@id='overridelink']").click()
        self.driver.get("javascript:document.getElementById('overridelink').click();") 
        self.driver.find_element_by_id("UserLoginForm_username").clear()
        self.driver.find_element_by_id("UserLoginForm_username").send_keys(TC2[0][1])
        self.driver.find_element_by_id("UserLoginForm_password").clear()
        self.driver.find_element_by_id("UserLoginForm_password").send_keys(TC2[1][1])
        self.driver.find_element_by_name("yt0").click()
        
  
    def test_bankaccount(self):
               
        for i in range(0,len(TC1)-3,13):
            tStart = time.time()
            # pass_1 = False
            setting(i)
            
            self.driver.find_element_by_link_text("Provider").click()
            self.driver.find_element_by_link_text("Bank Account Management").click()
            self.driver.find_element_by_link_text("Create").click()

        #Fill in the data for account
            select = Select(self.driver.find_element_by_name('OfflineBankAccount[OB_INIT_PROVIDER_ID]'))
            select.select_by_visible_text(bap)
            select = Select(self.driver.find_element_by_name('OfflineBankAccount[OB_INT_BANK_CODE]'))        
            select.select_by_value(bn)
            self.driver.find_element_by_id("OfflineBankAccount_OB_BANK_ACCT_NUM").send_keys(ban.strip(' '))
            select = Select(self.driver.find_element_by_name('OfflineBankAccount[OB_ACCT_CCY]'))  
            select.select_by_visible_text(cur)
            select = Select(self.driver.find_element_by_name('OfflineBankAccount[OB_ACCT_TYPE]'))
            select.select_by_visible_text(bana)
            self.driver.find_element_by_name("OfflineBankAccount[OB_OWNER_NAME]").send_keys(owner)
            self.driver.find_element_by_name("OfflineBankAccount[OB_PROVINCE]").send_keys(prov)
            self.driver.find_element_by_name("OfflineBankAccount[OB_CITY]").send_keys(city)
            self.driver.find_element_by_name("OfflineBankAccount[OB_BRANCH_NAME]").send_keys(branch)
            select = Select(self.driver.find_element_by_name('OfflineBankAccount[OB_SYS_SWITCH_ENABLED]'))
            select.select_by_visible_text(sswitch)
            select = Select(self.driver.find_element_by_name('OfflineBankAccount[OB_SUPPORT_SMS_STMT]'))        
            select.select_by_visible_text(sms)
            self.driver.find_element_by_name("OfflineBankAccount[OB_REMARK]").send_keys(remark)
            self.driver.find_element_by_id("OfflineBankAccount_OB_RECEIVED_DATETIME").click()
            self.driver.find_element_by_id("OfflineBankAccount_OB_RECEIVED_DATETIME").click()
            self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div[2]/button[1]").click()
            #self.driver.find_element_by_id("OfflineBankAccount_OB_RECEIVED_DATETIME").send_keys(date)
            self.driver.find_element_by_name("yt0").click()
            time.sleep(2)
        
        #Switch to pop out window
            self.yes = self.driver.switch_to.alert
            self.yes.accept()
            time.sleep(3)
            
        
        # 檢查建立帳號時是否有出現錯誤;
        # 出現錯誤:  終止測試並印出錯誤訊息,出現錯誤前建立的帳號都算完成!
        # 無出現錯誤:繼續測試至帳號都建立完成
               
            # try:
            #     self.driver.find_element_by_class_name("errorSummary")
            # except:
            #     pass_1 = True
            
            # if pass_1 == True:
            #     print("Bank Account Created Successful!")
            #     self.assertIsNone(None, 'Fail')
            # else:
            #     print("\n"+self.driver.find_element_by_class_name("errorSummary").text)
            #     self.assertIsNone(not None, 'Fail')
                

        #Back to Bank Account Management page
            self.driver.find_element_by_link_text("Provider").click()
            self.driver.find_element_by_link_text("Bank Account Management").click()

        #Search the account and change the status to Active
            self.driver.find_element_by_link_text("Advanced Search").click()
            self.driver.find_element_by_name("OfflineBankAccount[OB_REMARK]").send_keys(remark)
            select = Select(self.driver.find_element_by_name('OfflineBankAccount[BANK_ACCT_INT_BANK_CODE]'))        
            select.select_by_value(bn)
            self.driver.find_element_by_id("btn_Search").click()
            time.sleep(2)
            self.driver.find_element_by_id("SELECT_ACCT_NUM").click()
            self.driver.find_element_by_id("batch-update-account-btn").click()
            select = Select(self.driver.find_element_by_name('BANK_ACCT_STATUS'))
            select.select_by_visible_text("Active")
            time.sleep(2)
            self.driver.find_element_by_id("batch-update-btn").click()
            self.yes_active = self.driver.switch_to.alert
            self.yes_active.accept()
            time.sleep(2)
            
        #Back to Bank Account Management page
            self.driver.refresh()
            time.sleep(2)
            self.driver.find_element_by_link_text("Provider").click()
            self.driver.find_element_by_link_text("Bank Account Management").click()
            self.driver.find_element_by_link_text("Advanced Search").click()
            select = Select(self.driver.find_element_by_name('OfflineBankAccount[BANK_ACCT_INT_BANK_CODE]'))        
            select.select_by_value(bn)
            self.driver.find_element_by_name("OfflineBankAccount[OB_REMARK]").send_keys(remark)
            self.driver.find_element_by_id("btn_Search").click()
            #self.driver.find_element_by_id("quickViewBtn").click()
            time.sleep(2)

        #Catch the status of the bank account and check the status is Active or not
            b_acct = self.driver.find_element_by_xpath("//*[@id='offline-bank-account-grid']/table/tbody/tr/td[4]").text
            b_status = self.driver.find_element_by_xpath("//*[@id='offline-bank-account-grid']/table/tbody/tr/td[13]").text
            print("Bank account is created. \nBank account number is: " + b_acct + " The status is: "+ b_status)
        #Status is active => pass, else => failed
            self.assertEqual(b_status,"Active",msg="Ths status is not Acticve now!")
            tEnd = time.time()
            print("It cost " + str((tEnd - tStart)) + " sec.")
            time.sleep(2)
    
    #End the test, close the browser window
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
