import os
from selenium import webdriver

class ph():
    
    def __init__(self):
        global case,item,data
        self.TC1 = []
        self.TC2 = []
        self.TC3 = []
        self.TC4 = []

    def readfile(self):
        if os.path.isfile('phfile.csv'):
            print('找到目標檔案 phfile.csv')
            #讀取檔案
            with open('phfile.csv', 'r',encoding = 'utf-8', errors = "ignore") as f:
                for line in f:
                    s = line.strip().split(',') # split(',')就是遇到','就切一刀下去變成兩個欄位
                    case = s[0]
                    item = s[1]
                    data = s[2]
                    if case == 'login':
                        self.TC1.append([item, data])
                    elif case == 'time':
                        self.TC2.append([item, data])
                    elif case == "time2":
                        self.TC3.append([item, data])
                    elif case == "prov":
                        self.TC4.append([item, data])

    def webd(self):
        acct     =  self.TC1[0][1]
        pw       =  self.TC1[1][1]
        name     =  self.TC1[2][1]
        dir = os.getcwd()
        ie_driver_path = dir + '\IEDriverServer.exe'
        # create a new Internet Explorer session
        driver = webdriver.Ie(ie_driver_path)
        driver.implicitly_wait(360)
        driver.maximize_window()
        driver.get('https://tadmin.xx217569.com/admin/auth/login')
        driver.find_element_by_id("UserLoginForm_username").clear()
        driver.find_element_by_id("UserLoginForm_username").send_keys(acct)
        driver.find_element_by_id("UserLoginForm_password").clear()
        driver.find_element_by_id("UserLoginForm_password").send_keys(pw)
        driver.find_element_by_name("yt0").click()

        return driver

    def login(self):  
        global acct,pw  
        acct     =  self.TC1[0][1]
        pw       =  self.TC1[1][1]
        name     =  self.TC1[2][1]
        return  self.TC1
    
    def date_a(self):
        global sdate,edate
        sdate     = self.TC2[0][1]
        edate     = self.TC2[1][1]
        return self.TC2

    def date_b(self):
        global sdate2,edate2
        sdate2     = self.TC3[0][1]
        edate2     = self.TC3[1][1]
        return self.TC3

    def provider(self):
        global prov
        prov     = self.TC4[0][1]
        return self.TC4