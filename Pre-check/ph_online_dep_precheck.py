# coding=UTF-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from load_data import load_precheck_client, load_precheck_merchant


class Pre_check():
    def __init__(self):
        # self.cID = load_precheck_client()
        # self.mID = load_precheck_merchant()
        self.driver = webdriver.Ie()

    # 登入PH - Admin Console - Online
    def admin_login(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("https://phadminsd.pd.local/admin/auth/login")
        self.driver.get("javascript:document.getElementById('overridelink').click();")		# 可直接跳過ssl certificate不信任page
        self.driver.find_element_by_css_selector("input#UserLoginForm_username").clear()
        self.driver.find_element_by_css_selector("input#UserLoginForm_username").send_keys("at_1")
        self.driver.find_element_by_css_selector("input#UserLoginForm_password").clear()
        self.driver.find_element_by_css_selector("input#UserLoginForm_password").send_keys("qwertyuiop")
        self.driver.find_element_by_css_selector("input[value='Login']").click()

    # Check the client status
    '''Go to [Home » Client] and click View button of CQA001 to check the client status'''
    def chk_status_cli(self, cID):
        self.admin_login()
        self.driver.find_element_by_xpath("//span[contains(text(), 'Merchant')]").click()
        self.driver.find_element_by_css_selector("ul#nav>li>ul>li>a[href='/admin/client/admin']>span").click()
        self.driver.find_element_by_css_selector("div#content>a.search-button").click()
        self.driver.find_element_by_css_selector("tbody>tr>td>input#Client_CLIENT_NAME").clear()
        self.driver.find_element_by_css_selector("tbody>tr>td>input#Client_CLIENT_NAME").send_keys(cID[2][1])   # 該頁面是使用client name搜尋
        self.driver.find_element_by_css_selector("input#but_Search").click()
        self.driver.find_element_by_css_selector("a.view[href*='" + cID[1][1] + "']>img[src='/images/gridview/view.png']").click()
        cli_status = self.driver.find_element_by_xpath("//table[@id='yw0']/tbody/tr[6]/td").text    # 取得該標籤內容文字
        try:
            assert cli_status == "Open"
            print(cID[1][1], "- Client status is [" + cli_status + "]")
        except BaseException:
            print(cID[1][1], "- Client status is [Closed]")

    # Check the merchant status (Open / Closed)
    '''Go to [Home » Merchant » Manage Merchant] and check the merchant status'''
    def chk_status_mer_old(self):
        self.admin_login()
        self.driver.find_element_by_xpath("//span[contains(text(), 'Merchant')]").click()
        self.driver.find_element_by_css_selector("ul#nav>li>ul>li>a[href='/admin/merchant/admin']>span").click()
        self.driver.find_element_by_css_selector("div#content>a.search-button").click()
        self.driver.find_element_by_css_selector("select#MerchDetail_CLIENT_ID").click()
        self.driver.find_element_by_css_selector("select#MerchDetail_CLIENT_ID>option[value='CQA001']").click()
        self.driver.find_element_by_css_selector("input#btn_Search").click()
        # 檢查搜尋是否有結果
        try:
            locator = (By.XPATH, "//td[contains(text(), 'CQA001')]")
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
        except Exception as err:
            print(err)
            print("There is no any merchant under CQA001!")
        # 檢查MQA00005 / MQA00006 / MQA00001的status是否開啟
        mer1_status = self.driver.find_element_by_xpath("//div[@id='merch-detail-grid']/table[@class='items']/tbody/tr[1]/td[7]").text
        try:
            assert mer1_status == "Open"
            print("MQA00005 status is [" + mer1_status + "]")
        except Exception:
            print("MQA00005 status is [Closed]")
        mer2_status = self.driver.find_element_by_xpath("//div[@id='merch-detail-grid']/table[@class='items']/tbody/tr[2]/td[7]").text
        try:
            assert mer2_status == "Open"
            print("MQA00006 status is [" + mer2_status + "]")
        except Exception:
            print("MQA00006 status is [Closed]")
        mer3_status = self.driver.find_element_by_xpath("//div[@id='merch-detail-grid']/table[@class='items']/tbody/tr[5]/td[7]").text
        try:
            assert mer3_status == "Open"
            print("MQA00001 status is [" + mer3_status + "]")
        except Exception:
            print("MQA00001 status is [Closed]")
        # mer4_status = self.driver.find_element_by_xpath("//div[@id='merch-detail-grid']/table[@class='items']/tbody/tr/td[contains(text(), 'MQA00006')]/../td[7]").text
        mer4_status = self.driver.find_element_by_xpath("//tr[@class='even']/td[contains(text(), 'MQA00006')]/../td[7]").text
        print(mer4_status)

    # Check the merchant status (Open / Closed)
    '''Go to [Home » Merchant » Manage Merchant] and check the merchant status'''
    def chk_status_mer(self, cID):
        self.admin_login()
        self.driver.find_element_by_xpath("//span[contains(text(), 'Merchant')]").click()
        self.driver.find_element_by_css_selector("ul#nav>li>ul>li>a[href='/admin/merchant/admin']>span").click()
        self.driver.find_element_by_css_selector("div#content>a.search-button").click()
        self.driver.find_element_by_css_selector("select#MerchDetail_CLIENT_ID").click()
        self.driver.find_element_by_css_selector("select#MerchDetail_CLIENT_ID>option[value='" + cID + "']").click()
        self.driver.find_element_by_css_selector("input#btn_Search").click()
        # 檢查搜尋是否有結果
        try:
            locator = (By.XPATH, "//td[contains(text(), '" + cID + "')]")
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
        except Exception as err:
            print(err)
            print("There is no any merchant under", cID + "!")
        # 取得該Client底下的所有Merchant ID
        merList = self.driver.find_elements_by_xpath("//table[@class='items']/tbody/tr/td[3]")  # 取得所有merchant id的定位
        for mid in merList:
            try:
                assert self.driver.find_element_by_xpath("//tr/td[contains(text(), '" + mid.text + "')]/../td[7]").text == "Open"
                print(mid.text + " status is Open")
            except Exception:
                print(mid.text + " status is Closed")

    # Check the merchant information ()
    def chk_mer_info(self, cID, merID):
        self.admin_login()
        self.driver.find_element_by_xpath("//span[contains(text(), 'Merchant')]").click()
        self.driver.find_element_by_css_selector("ul#nav>li>ul>li>a[href='/admin/merchant/admin']>span").click()    # Go to "ome » Merchant » Manage Merchant"
        self.driver.find_element_by_css_selector("div#content>a.search-button").click()     # "Advanced Search"連結
        # self.driver.find_element_by_css_selector("select#MerchDetail_CLIENT_ID").click()
        self.driver.find_element_by_css_selector("select#MerchDetail_CLIENT_ID>option[value='" + cID + "']").click()
        # self.driver.find_element_by_css_selector("select#MerchDetail_MERCHANT_ID>option[value='" + merID + "']").click()
        self.driver.find_element_by_css_selector("input#btn_Search").click()
        # 檢查搜尋是否有結果
        locator = (By.XPATH, "//td[contains(text(), '" + merID + "')]")
        assert WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(locator)), "No merchant!"
        '''
        try:
            locator = (By.XPATH, "//td[contains(text(), 'CQA001')]")
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(locator))
        except Exception as err:
            print(err)
            print("There is no any merchant under CQA001!")'''
        # Go to Servece and Currency under merID
        self.driver.find_element_by_css_selector("a[href*='" + merID + "']>img[alt='View']").click()
        # 判斷是否存在 Service and Currency 設定 (沒有就可以不用繼續執行)
        assert self.isElementExist("xpath", "//td[@colspan='4']/span[@class='empty']") is False, 'No any setting of Service and Currency!'  # ===這裡判斷的有點久===
        # self.driver.find_element_by_xpath("//select/option[contains(text(), 'Service and Currency')]").click()

        # 先確認 Service and Currency 有幾個結果  [e.g. Displaying 1-5 of 5 result(s).] => 透過結果數量來定位總共有幾個 tr[n]
        resultSC = self.driver.find_element_by_xpath("//div[@id='merch-balance-detail-grid']/div[@class='summary']").text
        self.driver.find_element_by_xpath("//select/option[contains(text(), 'Service and Currency')]").click()
        print(resultSC[-16:-1])
        index = re.sub("\\D", "", resultSC[-16:-1])     # 擷取從字尾算起的16個字元 (只擷取數字,其他字元用''代替)
        print(index)
        self.availableServCcy(index)

        sleep(3)

    # 檢查是否有可用的Service and Currency (有Service and Currency但不知是否符合mock需求)
    def availableServCcy(self, index):
        available = 0
        num = int(index)
        # Service:1, Country:2, Currency:3, Status:6, Txn Type:7
        Service = '1'; Country = '2'; Currency = '3'; Status = '6'; TxnType = '7'
        while num != 0:
            # print(self.driver.find_element_by_xpath("//table[@class='items']/tbody/tr[" + index + "]/td[6]").text)
            if self.getServCcyInfo(index, Status) == "Open":
                if self.getServCcyInfo(index, Currency) == "CNY":
                    if self.getServCcyInfo(index, Country) == "China":
                        if self.getServCcyInfo(index, Service) == "Bankcard Gateway" or "Mobile Payment Gateway":
                            if self.getServCcyInfo(index, TxnType) == "All" or "Deposit Only":
                                available += 1
                            """else:
                                index = str(num - 1)
                                continue
                        else:
                            index = str(num - 1)
                            continue
                    else:
                        index = str(num - 1)
                        continue
                else:
                    index = str(num - 1)
                    continue
            else:
                index = str(num - 1)
                continue"""
            print(self.getServCcyInfo(index, Status))
            index = str(num - 1)
            print(index)
            num = int(index)
        if available != 0:
            return True
        else:
            return False

    # 取得Service and Currency的information
    def getServCcyInfo(self, index, item):
        locator = "//table[@class='items']/tbody/tr[" + index + "]/td[" + item + "]"
        return self.driver.find_element_by_xpath(locator).text

    # 檢查元素是否存在 (e.g. 檢查內容是否含有CQA001 => while not isElementExist("css", "//td[contains(text(), 'CQA001')]"): )
    def isElementExist(self, method, element):
        flag = True
        try:
            if method == "xpath":
                self.driver.find_element_by_xpath(element)
            elif method == "css":
                self.driver.find_element_by_css_selector(element)
            return flag
        except BaseException:
            flag = False
            return flag

    def closeBrowser(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    c = load_precheck_client()
    pc = Pre_check()
    pc.chk_status_cli(c)     # 檢查Client的status (Open / Closed)
    # pc.chk_status_cli("CQA001")     # 檢查Client的status (Open / Closed)
    # pc.chk_status_mer("CQA001")     # 檢查Merchant的status (Open / Closed)
    # pc.chk_mer_info("CQA001", "MQA00001")
    pc.closeBrowser()
