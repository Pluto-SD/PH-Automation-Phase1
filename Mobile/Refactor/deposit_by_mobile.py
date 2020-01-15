# coding=UTF-8

from selenium import webdriver
from time import sleep
from PIL import Image
import pyzbar.pyzbar as pyzbar
import random
import datetime
from load_data import load_amt


class Deposit_by_QR():
    def __init__(self, method):
        self.method = method    # 判斷使用何種QR支付
        self.amt = load_amt()    # 從外部檔案(CSV)讀取 deposit amount
        self.driver = webdriver.Ie()

    # 生成隨機 n 位數
    def get_random_num(self, digits):
        rand_num = ""

        for i in range(digits):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            rand_num += ch

        return rand_num

    # 生成隨機Customer Tag
    def customer_tag(self):
        dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        c_tag = dt + self.get_random_num(2)
        return c_tag

    # 讀取QR Code
    def load_qr_info(self):
        # self.driver.save_screenshot("/QR-Code.png")
        self.driver.save_screenshot("C:\\SD\\QR-Code.png")

        # 確認可讀取QR Code的資訊
        notFound = True
        decodeFail = 0
        while notFound:
            # barcodes = pyzbar.decode(Image.open("/QR-Code.png"))
            barcodes = pyzbar.decode(Image.open("C:\\SD\\QR-Code.png"))
            decodeFail += 1
            if decodeFail > 5:
                break
            if len(barcodes):
                notFound = False

        # 若解碼成功返回二維碼內容，反之解碼失敗
        if notFound is False:
            barcodeData = barcodes[0].data.decode("utf-8")
        else:
            barcodeData = False

        return barcodeData

    # 支付Service - Mobile - QR Code
    def deposit_by_mobile_qr(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("http://mock.systest.site/sdprod/")
        self.driver.find_element_by_id("mockpwd").send_keys("mockpwd\n")
        self.driver.find_element_by_xpath("//b[contains(text(), 'Mobile Mock Merchant')]").click()
        self.driver.find_element_by_css_selector("select#mer_id").click()
        self.driver.find_element_by_css_selector("option[value='MQA00005']").click()        # MerchantID: MQA VMOBILE2
        self.driver.find_element_by_css_selector("td.nnormal>input#cust_tag").send_keys(self.customer_tag())      # 亂數生成Customer Tag
        self.driver.find_element_by_css_selector("input#txn_amt").clear()
        # 不同的QR code使用不同的 transaction amount
        if self.method == 'WeChat':
            self.driver.find_element_by_css_selector("input#txn_amt").send_keys(self.amt[0][1])
        elif self.method == 'QQ':
            self.driver.find_element_by_css_selector("input#txn_amt").send_keys(self.amt[1][1])
        elif self.method == 'Alipay':
            self.driver.find_element_by_css_selector("input#txn_amt").send_keys(self.amt[2][1])
        elif self.method == 'CUP':
            self.driver.find_element_by_css_selector("input#txn_amt").send_keys(self.amt[3][1])
        # self.driver.find_element_by_css_selector("input#txn_amt").send_keys(self.get_random_num(4))      # 亂數生成deposit amount
        # PSP Account ID: driver.find_elements_by_css_selector("select#selected_pid[name='selected_pid']").click()
        # Bank Code: driver.find_elements_by_css_selector("select#bank_code").click()
        self.driver.find_element_by_css_selector("input#Submit").click()
        self.driver.find_element_by_css_selector("input.nnormal[name='mobileno']").clear()
        self.driver.find_element_by_css_selector("input.nnormal[name='mobileno']").send_keys("11111111111")
        self.driver.find_element_by_css_selector("input[value='086097']").click()        # 086097: 掃碼支付
        self.driver.find_element_by_css_selector("tr>td>input.btnSubmit[type='submit']").click()
        """driver.find_element_by_css_selector("input#086081").click()     ID不支援'#'後面接數字的用法 => invalid or illegal selector"""
        # Select payment method of QR
        # 086081: 微信支付 / 086082: QQ錢包 /  086083: 支付寶 /  086084: 銀聯二維碼支付
        if self.method == 'WeChat':
            self.driver.find_element_by_css_selector("input[id='086081']").click()
        elif self.method == 'QQ':
            self.driver.find_element_by_css_selector("input[id='086082']").click()
        elif self.method == 'Alipay':
            self.driver.find_element_by_css_selector("input[id='086083']").click()
        elif self.method == 'CUP':
            self.driver.find_element_by_css_selector("input[id='086084']").click()

        self.driver.find_element_by_css_selector("input#btn[type='submit']").click()
        # 讀取QR Code
        sleep(1)
        confirm_page = self.load_qr_info()
        # 判斷二維碼是否解碼成功
        if confirm_page is False:
            print("Cannot decode the barcode on screen!")
            print(self.method + ": Deposit failed!")
            print("=====================================")
            self.driver.close()
            self.driver.quit()
            return False
        else:
            # 開啟二維碼內藏的網址
            js = 'window.open("' + confirm_page + '");'
            self.driver.execute_script(js)
            handles = self.driver.window_handles
            self.driver.switch_to_window(handles[-1])
            sleep(1)
            self.driver.maximize_window()
            self.driver.find_element_by_css_selector("input#btn_yes[value*='Success']").click()
            # driver.find_element_by_css_selector("input#btn_yes[value*='Failed']").click()
            print(self.method + ": Deposit successfully!")
            print("=====================================")
            sleep(1)
            self.driver.close()
            self.driver.switch_to_window(handles[0])
            # driver.find_element_by_css_selector("input.btnSubmit[value='查询交易结果']").click()
            self.driver.close()
            self.driver.quit()
            return True

    # 不同的Payment method使用不同的 transaction amount
    def input_txn_amt(self, pmt_method):
        if pmt_method == 'WeChat':
            return self.amt[0][1]
        elif pmt_method == 'QQ':
            return self.amt[1][1]
        elif pmt_method == 'Alipay':
            return self.amt[2][1]
        elif pmt_method == 'CUP':
            return self.amt[3][1]
        elif pmt_method == 'EC':
            return self.amt[4][1]
        elif pmt_method == 'WAP':
            return self.amt[5][1]
        elif pmt_method == 'WeChat_H5':
            return self.amt[6][1]
        elif pmt_method == 'QQ_H5':
            return self.amt[7][1]
        elif pmt_method == 'Alipay_H5':
            return self.amt[8][1]

    # Select payment
    def select_payment(self, pmt_method):
        if (pmt_method == 'WeChat') or (pmt_method == 'QQ') or (pmt_method == 'Alipay') or (pmt_method == 'CUP'):
            self.driver.find_element_by_css_selector("input[value='086097']").click()        # 086097: 掃碼支付
        elif pmt_method == 'EC':
            self.driver.find_element_by_css_selector("input[value='086098']").click()   # 086098: 快捷支付
        elif pmt_method == 'WAP':
            self.driver.find_element_by_css_selector("input[value='086099']").click()   # 086099: 手机银行
        elif pmt_method == 'WeChat_H5':
            self.driver.find_element_by_css_selector("input[value='086094']").click()   # 086094: 微信支付 (H5)
        elif pmt_method == 'QQ_H5':
            self.driver.find_element_by_css_selector("input[value='086095']").click()   # 086095: QQ钱包支付 (H5)
        elif pmt_method == 'Alipay_H5':
            self.driver.find_element_by_css_selector("input[value='086096']").click()   # 086096: 支付宝支付 (H5)

    # Select QR method (WeChat / QQ / Alipay / CUP)
    def qr_method(self, pmt_method):
        if pmt_method == 'WeChat':
            self.driver.find_element_by_css_selector("input[id='086081']").click()
        elif pmt_method == 'QQ':
            self.driver.find_element_by_css_selector("input[id='086082']").click()
        elif pmt_method == 'Alipay':
            self.driver.find_element_by_css_selector("input[id='086083']").click()
        elif pmt_method == 'CUP':
            self.driver.find_element_by_css_selector("input[id='086084']").click()

    # 支付Service - Mobile - QR / EC / WAP / H5
    def deposit_by_mobile(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("http://mock.systest.site/sdprod/")
        self.driver.find_element_by_id("mockpwd").send_keys("mockpwd\n")
        self.driver.find_element_by_xpath("//b[contains(text(), 'Mobile Mock Merchant')]").click()
        self.driver.find_element_by_css_selector("select#mer_id").click()
        self.driver.find_element_by_css_selector("option[value='MQA00005']").click()        # MerchantID: MQA VMOBILE2
        self.driver.find_element_by_css_selector("td.nnormal>input#cust_tag").send_keys(self.customer_tag())      # 亂數生成Customer Tag
        self.driver.find_element_by_css_selector("input#txn_amt").clear()
        self.driver.find_element_by_css_selector("input#txn_amt").send_keys(self.input_txn_amt(self.method))    # 不同的Payment method使用不同的 transaction amount
        self.driver.find_element_by_css_selector("input#Submit").click()
        self.driver.find_element_by_css_selector("input.nnormal[name='mobileno']").clear()
        self.driver.find_element_by_css_selector("input.nnormal[name='mobileno']").send_keys("11111111111")
        self.select_payment(self.method)   # Select payment  (except QR)
        self.driver.find_element_by_css_selector("tr>td>input.btnSubmit[type='submit']").click()
        """driver.find_element_by_css_selector("input#086081").click()     ID不支援'#'後面接數字的用法 => invalid or illegal selector"""
        # WAP與QR需要額外的處理
        if self.method == 'WAP':
            self.driver.find_element_by_css_selector("td.bankname>input[value='086508']").click()  # 建设银行-WAP
            # self.driver.find_element_by_css_selector("td.bankname>input[value='086509']").click()  # 工商银行-WAP
            # self.driver.find_element_by_css_selector("td.bankname>input[value='086510']").click()  # 招商银行-WAP
            # self.driver.find_element_by_css_selector("td.bankname>input[value='086523']").click()  # 交通银行-WAP
            self.driver.find_element_by_css_selector("input.btnSubmit[type='submit']").click()
        elif (self.method == 'EC') or (self.method == 'WeChat_H5') or (self.method == 'QQ_H5') or (self.method == 'Alipay_H5'):
            pass
        else:   # QR Code
            self.qr_method(self.method)
            self.driver.find_element_by_css_selector("input#btn[type='submit']").click()

        # 選QR要解碼 而其他的則走別種方法
        if (self.method == 'WeChat') or (self.method == 'QQ') or (self.method == 'Alipay') or (self.method == 'CUP'):
            sleep(1)
            confirm_page = self.load_qr_info()  # 讀取 QR Code
            # 判斷二維碼是否解碼成功
            if confirm_page is False:
                print("Cannot decode the barcode on screen!")
                print(self.method + ": Deposit failed!")
                print("=====================================")
                self.driver.close()
                self.driver.quit()
                return False
            else:
                # 開啟二維碼內藏的網址
                js = 'window.open("' + confirm_page + '");'
                self.driver.execute_script(js)  # 開啟新視窗 (二維碼內藏的網址)
                handles = self.driver.window_handles    # 取得目前所有視窗的handle
                self.driver.switch_to_window(handles[-1])   # 將handle切換到新開啟的視窗 (新視窗的 handle 會排在 list 最後的位置)
                sleep(1)
                self.driver.maximize_window()
                self.driver.find_element_by_css_selector("input#btn_yes[value*='Success']").click()
                # driver.find_element_by_css_selector("input#btn_yes[value*='Failed']").click()
                print(self.method + ": Deposit successfully!")
                print("=====================================")
                sleep(1)
                self.driver.close()
                self.driver.switch_to_window(handles[0])    # 將 handle 切換回初始視窗
                # driver.find_element_by_css_selector("input.btnSubmit[value='查询交易结果']").click()
                self.driver.close()
                self.driver.quit()
                return True
        else:
            self.driver.find_element_by_css_selector("input#btn_yes[value*='Success']").click()
            print(self.method + ": Deposit successfully!")
            print("=====================================")
            self.driver.close()
            self.driver.quit()
            return True
