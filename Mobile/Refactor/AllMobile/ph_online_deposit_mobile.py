# coding=UTF-8

from time import time
import unittest
# from deposit_by_qr import Deposit_by_QR
from deposit_by_mobile import Deposit_by_Mobile
from decimal import Decimal


""" 已經在deposit_by_qr.py引用"from load_data import load_amt"來讀取外部檔案
if os.path.isfile("txnamt.csv"):
    amt = []
    print("檔案- txnamt.csv 存在.")
    # Read file
    with open("txnamt.csv", "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            # If 'QR' in line: continue # 繼續，跳到下一迴()
            s = line.strip().split(',')     # split(',') 遇到 ',' 就切開分成另一個欄位
            case = s[0]
            item = s[1]
            data = s[2]
            if case == 'QR':
                amt.append([item, data])
            elif case == 'VNet':
                pass
            else:
                pass
"""


class MobileTests(unittest.TestCase):   # class MobileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        類級別: 類開始 - 所有case執行之前的前置
        """
        cls.tTime = time()      # Calculate test total time

    def setUp(self):
        """
        函數級別 - 測試固件(test fixture)的setUp()的代碼，主要是測試的提前準備工作
        函數開始 - 每條case之前執行
        """
        self.sTime = time()     # Calculate one test case time

    def test_00001_QR_WeChat(self):
        wc = Deposit_by_Mobile('WeChat')
        # self.assertIs(wc.deposit_by_mobile_qr(), True, msg="test fail!")
        self.assertIs(wc.deposit_by_mobile(), True, msg="test fail!")

    @unittest.skip('這裡寫跳過的原因')      # 無條件跳過此項case
    def test_00002_QR_QQ(self):
        qq = Deposit_by_Mobile('QQ')
        self.assertIs(qq.deposit_by_mobile_qr(), True, msg="test fail!")

    @unittest.skip('這裡寫跳過的原因')      # 無條件跳過此項case
    def test_00003_QR_Alipay(self):
        ap = Deposit_by_Mobile('Alipay')
        self.assertIs(ap.deposit_by_mobile_qr(), True, msg="test fail!")

    @unittest.skip('這裡寫跳過的原因')      # 無條件跳過此項case
    def test_00004_QR_CUP(self):
        cup = Deposit_by_Mobile('CUP')
        self.assertIs(cup.deposit_by_mobile_qr(), True, msg="test fail!")

    def test_00005_QQ_H5(self):
        qq_h5 = Deposit_by_Mobile('QQ_H5')
        self.assertIs(qq_h5.deposit_by_mobile(), True, msg="test fail!")

    def test_00005_EC(self):
        ec = Deposit_by_Mobile('EC')
        self.assertIs(ec.deposit_by_mobile(), True, msg="test fail!")

    def test_00005_WAP(self):
        wap = Deposit_by_Mobile('WAP')
        self.assertIs(wap.deposit_by_mobile(), True, msg="test fail!")

    def tearDown(self):
        """
        函數級別 - 測試結束後的操作，這裡基本上都是關閉瀏覽器 (but 已在test case中關閉)
        函數結束 - 每條case之後執行
        """
        total = time() - self.sTime
        print("Cost time is " + str(Decimal(total).quantize(Decimal('0.00'))) + " seconds.")
        # print("Cost time is " + str(time() - self.sTime))

    @classmethod
    def tearDownClass(cls):
        """
        類級別: 類結束 - 所有case執行之後的後置
        """
        ttl = time() - cls.tTime
        print("Cost time is " + str(Decimal(ttl).quantize(Decimal('0.00'))) + " seconds.")
        # print("The total time of test cases is " + str(time() - cls.tTime))


if __name__ == '__main__':
    unittest.main(verbosity=2)
