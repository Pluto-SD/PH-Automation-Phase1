# coding=UTF-8

from time import time
import unittest
from deposit_by_vnet import Deposit_by_VNet
from load_data import load_vnet_amt, load_precheck_info
from decimal import Decimal
from ph_online_dep_precheck import Pre_check


class VNetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        類級別: 類開始 - 所有case執行之前的前置
        """
        cls.tTime = time()  # Calculate test total time

    def setUp(self):
        """
        函數級別 - 測試固件(test fixture)的setUp()的代碼，主要是測試的提前準備工作
        函數開始 - 每條case之前執行
        """
        self.sTime = time()     # Calculate one test case time

    @unittest.skip('這裡寫跳過的原因')      # 無條件跳過此項case
    def test_00001_dep_precheck(self):
        pchk = Pre_check()
        info = load_precheck_info()
        self.assertIs(pchk.chk_status_cli(info), True, msg="Test fail - CID status is closed!")
        self.assertIs(, True, msg="Test fail - MID status is closed!")
        self.assertIs(, True, msg="Test fail - Error in Service & Currency!")
        self.assertIs(, True, msg="Test fail - Scheme error!")
        self.assertIs(, True, msg="Test fail - Pool error!")
        pchk.closeBrowser()

    @unittest.skip('這裡寫跳過的原因')      # 無條件跳過此項case
    def test_00002_VNet_all_bank(self):
        banklist = []
        vnet = Deposit_by_VNet()
        vnet.vnet_info_input(load_vnet_amt())
        banklist = vnet.get_all_banks()
        self.assertIs(vnet.dep_all_banks_by_vnet(banklist), True, msg="Test fail!")

    @unittest.skip('這裡寫跳過的原因')      # 無條件跳過此項case
    def test_00003_VNet_one_bank(self):
        vnet = Deposit_by_VNet()
        self.assertIs(vnet.dep_one_bank_by_vnet(), True, msg="Test fail!")

    def test_00004_VNet(self):
        pass

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
