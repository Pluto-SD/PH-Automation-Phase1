# coding=UTF-8

from selenium import webdriver
from selenium.common import exceptions
from time import sleep
import random
import datetime
from load_data import load_vnet_amt


class Deposit_by_VNet():
    def __init__(self):
        self.bank_list = []
        self.element_list = []
        self.amt = load_vnet_amt()
        self.driver = webdriver.Ie()

    # 生成隨機n位數
    def get_random_num(self, digits):
        rand_num = ""
        for i in range(digits):
            ch = chr(random.randrange(ord("0"), ord("9") + 1))
            rand_num += ch
        return rand_num

    # 生成隨機Customer Tag
    def customer_tag(self):
        # today = datetime.date.today()
        # formatted_today = today.strftime("%Y%m%d%H%M%S")
        dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        c_tag = dt + self.get_random_num(2)
        return c_tag

    # 銀行選擇
    def select_bank(self, code):
        bank_code = "input[value='" + code + "']"
        index = self.driver.find_element_by_css_selector(bank_code).is_displayed()
        if (index is True):
            print("selected bank is", self.bank_name(code))
            self.driver.find_element_by_css_selector(bank_code).click()
            return True
        else:
            print("Cannot use", self.bank_name(code), "to deposit!")
            return False

    # 銀行名稱
    def bank_name(self, bankcode):
        bank_dict = {'086102': '工商銀行', '086308': '招商銀行', '086103': '農業銀行', '086105': '建設銀行', '086104': '中國銀行',
                        '086305': '民生銀行', '086309': '興業銀行', '086310': '浦東發展銀行', '086301': '交通銀行', '086302': '中信銀行',
                        '086303': '光大銀行', '086304': '華夏銀行', '086306': '發展銀行', '086502': '平安銀行', '086501': '北京銀行',
                        '086403': '郵政儲蓄銀行', '086507': '上海銀行', '086517': '農村商業銀行', '086505': 'BEA東亞銀行'}
        return bank_dict[bankcode]

    # 輸入交易資訊
    def vnet_info_input(self, amt):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("Start to input transaction info.")
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("http://mock.systest.site/sdprod")
        self.driver.find_element_by_id("mockpwd").send_keys("mockpwd\n")
        self.driver.find_element_by_css_selector("li[onclick*='mockvnc']").click()
        self.driver.find_element_by_name("mer_id").click()
        try:
            self.driver.find_element_by_css_selector("option[value='MQA00002']").click()    # 目前常用MID: MQA00001 / MQA00002
            self.driver.find_element_by_name("cust_tag").send_keys(self.customer_tag())
            self.driver.find_element_by_name("txn_amt").clear()
            self.driver.find_element_by_name("txn_amt").send_keys(amt[0][1])  # 透過csv檔讀取txn amount
            print("deposit amount is $" + str(int(amt[0][1])/100))
            self.driver.find_element_by_name("Submit").click()
            self.driver.find_element_by_name("btn_buyCard").click()
            if self.driver.find_element_by_css_selector("input#debit_card_type[value='debit']").is_displayed():
                self.driver.find_element_by_name("card_type_debit").click()     # Debit Card; 使用MQA00002不須選卡別
        except exceptions.NoSuchElementException as err:
            self.driver.save_screenshot("/SD/VNET_Deposit_Error.png")
            print("+++++++++++++++++++++++++++++++++++++++++++++++")
            print("\n", err)
            print("+++++++++++++++++++++++++++++++++++++++++++++++")
            print("=> This merchant cannot be used to deposit!")
            return False
        else:
            print("Input complete.")
            sleep(1)
            return True

    # Get all available banks
    def get_all_banks(self):
        self.element_list = self.driver.find_elements_by_css_selector("input[value*='086']")    # 取得屬性value所有包含086的元素
        for ele in self.element_list:
            self.bank_list.append(ele.get_attribute('value'))
        return self.bank_list

    # Use all available banks to deposit
    def dep_all_banks_by_vnet(self, allbanks):
        try:
            for bank in allbanks:
                if (self.select_bank(bank) is True):
                    self.driver.find_element_by_css_selector("td>input#btn_submit").submit()
                    self.driver.find_element_by_css_selector("input[value*='Success']").click()     # 模擬交易成功
                    self.driver.find_element_by_css_selector("div#btn>input#btn_back[type='button']").click()
                    print("Deposit transaction result: Success!")
                    print("============================")
                    sleep(1)
                else:
                    print("Bank code: " + bank + "cannot be selected!")
                    continue

                if (bank != allbanks[-1]):
                    self.vnet_info_input(self.amt)
                else:
                    self.driver.close()
                    self.driver.quit()
            return True    # 用來讓GTMLTestRunner判斷測試結果
        except BaseException as err:
            print("Reason:", err)
            return False    # 用來讓GTMLTestRunner判斷測試結果

    # Use one single bank to deposit
    def dep_one_bank_by_vnet(self):
        try:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("Start to input transaction info.")
            self.driver.maximize_window()
            self.driver.implicitly_wait(8)
            self.driver.get("http://mock.systest.site/sdprod")
            self.driver.find_element_by_id("mockpwd").send_keys("mockpwd\n")
            self.driver.find_element_by_css_selector("li[onclick*='mockvnc']").click()
            self.driver.find_element_by_name("mer_id").click()
            self.driver.find_element_by_css_selector("option[value='MQA00001']").click()    # Merchant ID: MQA00001
            self.driver.find_element_by_name("cust_tag").send_keys(self.customer_tag())
            self.driver.find_element_by_name("txn_amt").clear()
            self.driver.find_element_by_name("txn_amt").send_keys(self.amt[0][1])
            print("Deposit amount is $" + str(int(self.amt[0][1])/100))
            self.driver.find_element_by_name("Submit").click()
            self.driver.find_element_by_name("btn_buyCard").click()
            if self.driver.find_element_by_css_selector("input#debit_card_type[value='debit']").is_displayed():
                self.driver.find_element_by_name("card_type_debit").click()     # Debit Card; 使用MQA00002不須選卡別
            self.driver.find_element_by_css_selector("input[value='086302']").click()   # 中信銀行
            self.driver.find_element_by_id("btn_submit").click()
            self.driver.find_element_by_css_selector("input[value*='Success']").click()
            print("Deposit transaction result: Success!")
            print("============================")
        except BaseException as err:
            self.driver.close()
            self.driver.quit()
            print("Reason:", err)
            return False
        else:
            self.driver.close()
            self.driver.quit()
            return True


if __name__ == '__main__':
    vnet = Deposit_by_VNet()
    vnet.dep_one_bank_by_vnet()
"""
    banklist = []
    vnet = Deposit_by_VNet()
    vnet.vnet_info_input(load_vnet_amt())
    banklist = vnet.get_all_banks()
    vnet.dep_all_banks_by_vnet(banklist)
"""
