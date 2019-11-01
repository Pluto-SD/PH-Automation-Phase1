# coding=UTF-8

from selenium import webdriver
from selenium.common import exceptions
# from selenium.webdriver.common.keys import Keys
from time import sleep, time
import random
import datetime
import os


# 生成隨機n位數
def get_random_num(degits):
    rand_num = ""
    for i in range(degits):
        ch = chr(random.randrange(ord("0"), ord("9") + 1))
        rand_num += ch
    return rand_num


# 生成隨機Customer Tag
def customer_tag():
    # today = datetime.date.today()
    # formatted_today = today.strftime("%Y%m%d%H%M%S")
    dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    c_tag = dt + get_random_num(2)
    return c_tag


# 银行選擇
def select_bank(code):
    bank_code = "input[value='" + code + "']"
    index = driver.find_element_by_css_selector(bank_code).is_displayed()
    if (index is True):
        print("selected bank is", bank_name(code))
        driver.find_element_by_css_selector(bank_code).click()
        return True
    else:
        print("Cannot use", bank_name(code), "to deposit!")
        return False


# 银行名稱
def bank_name(bankcode):
    bank_dict = {'086102': '工商銀行', '086308': '招商銀行', '086103': '農業銀行', '086105': '建設銀行', '086104': '中國銀行',
                        '086305': '民生銀行', '086309': '興業銀行', '086310': '浦東發展銀行', '086301': '交通銀行', '086302': '中信銀行',
                        '086303': '光大銀行', '086304': '華夏銀行', '086306': '發展銀行', '086502': '平安銀行', '086501': '北京銀行',
                        '086403': '郵政儲蓄銀行', '086507': '上海銀行', '086517': '農村商業銀行', '086505': 'BEA東亞銀行'}
    return bank_dict[bankcode]


# 輸入交易資訊
def vnet_info_input(amt):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Start to input transaction info.")
    driver.find_element_by_css_selector("li[onclick*='mockvnc']").click()
    driver.find_element_by_name("mer_id").click()
    try:
        driver.find_element_by_css_selector("option[value='MQA00002']").click()     # Merchant ID: MQA00001
        driver.find_element_by_name("cust_tag").send_keys(customer_tag())
        driver.find_element_by_name("txn_amt").clear()
        """ Use random number to be txn amount
        deposit = get_random_num(4)
        driver.find_element_by_name("txn_amt").send_keys(deposit)
        """
        driver.find_element_by_name("txn_amt").send_keys(amt)   # 透過csv檔讀取txn amount
        print("deposit amount is $" + str(int(amt)/100))
        driver.find_element_by_name("Submit").click()
        driver.find_element_by_name("btn_buyCard").click()
        # driver.find_element_by_name("card_type_debit").click()      # Debit Card; 使用MQA00002需註解，因為不須選擇
    except exceptions.NoSuchElementException as err:
        driver.save_screenshot("/SD/VNet_Deposit_Error.png")
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        print("\n", err)
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        print("=> This merchant cannot be used to deposit!")
        return False
    else:
        print("Input complete.")
        sleep(1)
        return True


# Use all available banks to deposit
def dep_all_banks_by_vnet(allbanks):
    for bank in allbanks:
        # print("Get bank code:")
        # print(bank, bank_name(bank))
        if (select_bank(bank) is True):
            driver.find_element_by_css_selector("td>input#btn_submit").submit()
            driver.find_element_by_css_selector("input[value*='Success']").click()  # The simulation result of success
            driver.find_element_by_css_selector("div#btn>input#btn_back[type='button']").click()
            print("Deposit transaction result: Success!")
            print("============================")
            sleep(1)
        else:
            continue

        if (bank != allbanks[-1]):
            driver.get("http://mock.systest.site/sdprod")
            driver.find_element_by_id("mockpwd").send_keys("mockpwd\n")
            sleep(1)
            vnet_info_input(txnamt[0][1])


if __name__ == '__main__':
    txnamt = []
    if os.path.isfile("txnamt.csv"):
        print("檔案- txnamt.csv 存在.")
        with open("txnamt.csv", "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                # if 'VNet' in line: continue # 繼續，跳到下一迴()
                s = line.strip().split(',')     # split(',') 遇到 ',' 就切開分成另一個欄位
                case = s[0]
                item = s[1]
                data = s[2]
                if case == '\ufeffVNet':
                    txnamt.append([item, data])
                elif case == 'login':
                    pass
                elif case == 'invalid':
                    pass
                elif case == 'repeat':
                    pass

    driver = webdriver.Ie()
    driver.maximize_window()
    driver.implicitly_wait(6)

    T1 = time()

    # Loging Mock & Input Txn Info
    driver.get("http://mock.systest.site/sdprod")
    driver.find_element_by_id("mockpwd").send_keys("mockpwd\n")
    if vnet_info_input(txnamt[0][1]):
        # Get all banks that display on screen
        banks_list = []
        elements_list = driver.find_elements_by_css_selector("input[value*='086']")     # 取得所有屬性value有包含086的元素定位
        for ele in elements_list:
            banks_list.append(ele.get_attribute('value'))

        print("Bank Code:", banks_list)
        dep_all_banks_by_vnet(banks_list)   # 循序使用該merchant所有可用銀行deposit

    print("Total testing time is", str(time() - T1))
    sleep(2)
    driver.close()
    driver.quit()
