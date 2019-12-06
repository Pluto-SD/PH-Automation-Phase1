import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from decimal import *
from common import ph

read = ph()
read.readfile()

#統計所有case執行時間用
unittest.total = 0

class LoginTests(unittest.TestCase):

    #initiation for the test
    def setUp(self):
        
        self.driver = read.webd_nologin()

   #Login process
    def test_00001_Login(self):
        data = read.login()
        for i in range(0,len(data),3):
            acct = data[i][1]
            pw = data[i+1][1]
            tStart = time.time()
            self.driver.find_element_by_id("UserLoginForm_username").clear()
            self.driver.find_element_by_id("UserLoginForm_username").send_keys(acct)
            self.driver.find_element_by_id("UserLoginForm_password").clear()
            self.driver.find_element_by_id("UserLoginForm_password").send_keys(pw)
            self.driver.find_element_by_name("yt0").click()
            
            #依照 url/title/text 確認是否成功login
            url_now = self.driver.current_url
            msg = self.driver.find_element_by_id("headerText").text
            text = self.driver.find_element_by_class_name("summary").text
            self.assertIn("client/admin",url_now, msg="Login Error!")
            self.assertIn("(SD Prod)",msg, msg="Login Error!")
            self.assertIn("Displaying",text, msg="Login Error!")
            
            self.driver.close()
            tEnd = time.time()
            t01 = tEnd - tStart
            print("It cost " + str(Decimal(t01).quantize(Decimal('0.00'))) + "seconds.")
            unittest.total = t01

    #Logout process
    def test_00002_Logout(self):
        data = read.login()
        for i in range(0,len(data),3):
            acct = data[i][1]
            pw = data[i+1][1]
            name = data[i+2][1]
            tStart = time.time()
            self.driver.find_element_by_id("UserLoginForm_username").clear()
            self.driver.find_element_by_id("UserLoginForm_username").send_keys(acct)
            self.driver.find_element_by_id("UserLoginForm_password").clear()
            self.driver.find_element_by_id("UserLoginForm_password").send_keys(pw)
            #self.driver.find_element_by_name("yt0").send_keys(Keys.ENTER)
            self.driver.find_element_by_name("yt0").click()
            self.driver.find_element_by_link_text("Account (" + name + ")").click()
            self.driver.find_element_by_link_text("Logout (" + name + ")").click()
            
        #Make sure that Logout success
            url_now = self.driver.current_url
            mes = self.driver.find_element_by_id("logo2").text
            self.assertIn("admin/auth",url_now, msg="Logout Failed!")
            self.assertIn("(OfflineProduction)",mes, msg="Logout Failed!")
            
            self.driver.close()
            tEnd = time.time()
            t02 = tEnd - tStart
            print("It cost " + str(Decimal(t02).quantize(Decimal('0.00'))) + "seconds.") 
            unittest.total = unittest.total + t02

    #account = blank, pw = blank, both account&pw blank
    def test_00003_Error_blank(self):
        data = read.blank()
        for i in range(0,len(data),2):
            acct2 = data[i][1]
            pw2 = data[i+1][1]
            tStart = time.time()
            self.driver.find_element_by_id("UserLoginForm_username").clear()
            self.driver.find_element_by_id("UserLoginForm_username").send_keys(acct2)
            self.driver.find_element_by_id("UserLoginForm_password").clear()
            self.driver.find_element_by_id("UserLoginForm_password").send_keys(pw2)
            #self.driver.find_element_by_name("yt0").send_keys(Keys.ENTER)
            self.driver.find_element_by_name("yt0").click()
            
            E_msg = self.driver.find_element_by_class_name("errorSummary").text
            self.assertIn("cannot be blank",E_msg, msg="Error message wrong!")
            print("Case: ")
            print("Account: "+acct2+" password: "+pw2)
            print("Error message: " + "\n" + E_msg)
            time.sleep(2)
            tEnd = time.time()
            t03 = tEnd - tStart
            print("It cost " + str(Decimal(t03).quantize(Decimal('0.00'))) + "seconds.") 
            unittest.total = unittest.total + t03
       
    
    #account = blank, pw = blank, both account&pw blank
    def test_00004_Error_invalid(self):
        data = read.invalid()
        for i in range(0,len(data),2):
            acct3 = data[i][1]
            pw3 = data[i+1][1]
            tStart = time.time()
            self.driver.find_element_by_id("UserLoginForm_username").clear()
            self.driver.find_element_by_id("UserLoginForm_username").send_keys(acct3)
            self.driver.find_element_by_id("UserLoginForm_password").clear()
            self.driver.find_element_by_id("UserLoginForm_password").send_keys(pw3)
            #self.driver.find_element_by_name("yt0").send_keys(Keys.ENTER)
            self.driver.find_element_by_name("yt0").click()
            
            E_msg = self.driver.find_element_by_class_name("errorSummary").text
            self.assertIn("combination invalid.",E_msg, msg="Error message wrong!")
            print("Case: ")
            print("Account: "+acct3+" password: "+pw3)
            print("Error message: "+ "\n" + E_msg)
            time.sleep(2)
            tEnd = time.time()
            t04 = tEnd - tStart
            print("It cost " + str(Decimal(t04).quantize(Decimal('0.00'))) + "seconds.") 
            unittest.total = unittest.total + t04

    def test_00005_LoginLoop(self):
        count = 0
        data = read.looplogin()
        for i in range(0,len(data),3):
            acct4 = data[i][1]
            pw4   = data[i+1][1]
            name4 = data[i+2][1]
            tStart = time.time()
            #settc4(i)
            self.driver.find_element_by_id("UserLoginForm_username").clear()
            self.driver.find_element_by_id("UserLoginForm_username").send_keys(acct4)
            self.driver.find_element_by_id("UserLoginForm_password").clear()
            self.driver.find_element_by_id("UserLoginForm_password").send_keys(pw4)
            self.driver.find_element_by_name("yt0").click()
            self.driver.find_element_by_link_text("Account (" + name4 + ")").click()
            self.driver.find_element_by_link_text("Logout (" + name4 + ")").click()
            count +=1
            print("\n"+"Test:" + str(count) + "\n" +"Account: "+acct4+" password: "+pw4)
            time.sleep(2)
            tEnd = time.time()
            t05 = tEnd - tStart
            print("It cost " + str(Decimal(t05).quantize(Decimal('0.00'))) + "seconds.") 
            unittest.total = unittest.total + t05

        print("\n"+"Number of login/logout test: "+ str(count))
    
    def test_00006_TotalTime(self):
        print("All test case cost " + str(Decimal(unittest.total).quantize(Decimal('0.00'))) + "seconds.")

    #End the test, close the browser window
    def tearDown(self):
        unittest.total = 0
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
