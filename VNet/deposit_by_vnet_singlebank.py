# coding=UTF-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, time
import random
import datetime
from decimal import Decimal


# 生成隨機n位數
def get_random_num(degits):
    rand_num = ""
    for i in range(degits):
        ch = chr(random.randrange(ord("0"), ord("9") + 1))
        rand_num += ch

    return rand_num


# 生成隨機Customer Tag
def customer_tag():
    today = datetime.date.today()
    formatted_today = today.strftime("%Y%m%d")
    c_tag = formatted_today + get_random_num(4)
    return c_tag


def bank_code(code):
    bcode = "input[value='" + code + "']"
    return bcode


def deposit_by_vnet():
    driver.find_element_by_css_selector("li[onclick*='mockvnc']").click()
    driver.find_element_by_name("mer_id").click()
    driver.find_element_by_css_selector("option[value='MQA00001']").click()     # Merchant ID: MQA00001
    driver.find_element_by_name("cust_tag").send_keys(customer_tag())
    driver.find_element_by_name("txn_amt").clear()
    deposit = get_random_num(4)
    driver.find_element_by_name("txn_amt").send_keys(deposit)
    print("deposit amount is $" + str(int(deposit)/100))
    driver.find_element_by_name("Submit").click()
    driver.find_element_by_name("btn_buyCard").click()
    driver.find_element_by_name("card_type_debit").click()      # Debit Card
    """
    工商銀行 (086102) / 招商銀行 (086308) / 農業銀行 (086103) / 建設銀行 (086105) / 中國銀行 (086104) / 民生銀行 (086305) /
    興業銀行 (086309) / 浦東發展銀行 (086310) / 交通銀行 (086301) / 中信銀行 (086302) / 光大銀行 (086303) / 華夏銀行 (086304) /
    發展銀行 (086306) / 平安銀行 (086502) / 北京銀行 (086501) / 郵政儲蓄銀行 (086403) / 上海銀行 (086507) / 農村商業銀行 (086517)
    """
    driver.find_element_by_css_selector(bank_code('086302')).click()        # 中信銀行
    # driver.find_element_by_id("debit_bank_id_9").click()					# 排序為第9的銀行
    driver.find_element_by_id("btn_submit").click()

    driver.find_element_by_css_selector("input[value*='Success']").click()      # 模擬成功
    # driver.find_element_by_css_selector("input[value*='Failed']").click()		# 模擬失敗


driver = webdriver.Ie()
driver.maximize_window()
driver.implicitly_wait(6)

T1 = time()

# Loging Mock
driver.get("http://mock.systest.site/sdprod")
driver.find_element_by_id("mockpwd").send_keys("mockpwd\n")
deposit_by_vnet()
total = time() - T1
print("Cost time is " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
# print("Cost time is", str(time() - T1))        # 測試耗時

sleep(2)
driver.quit()
