import os

global case,item,data
TC1 = []
TC2 = []
TC3 = []
TC4 = []

def readfile():
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
                    TC1.append([item, data])
                elif case == 'time':
                    TC2.append([item, data])
                elif case == "time2":
                    TC3.append([item, data])
                elif case == "prov":
                    TC4.append([item, data])

def login():  
    global acct,pw  
    acct     = TC1[0][1]
    pw       = TC1[1][1]
    name     = TC1[2][1]
    return TC1
   
def date_a():
    global sdate,edate
    sdate     = TC2[0][1]
    edate     = TC2[1][1]
    return TC2

def date_b():
    global sdate2,edate2
    sdate2     = TC3[0][1]
    edate2     = TC3[1][1]
    return TC3

def provider():
    global prov
    prov     = TC4[0][1]
    return TC4