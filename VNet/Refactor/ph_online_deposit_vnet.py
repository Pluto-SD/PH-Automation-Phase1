# coding=UTF-8

from time import time
import unittest
from deposit_by_vnet import Deposit_by_VNet
from load_data import load_vnet_amt


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

    def test_00001_VNet_all_bank(self):
        banklist = []
        vnet = Deposit_by_VNet()
        vnet.vnet_info_input(load_vnet_amt())
        banklist = vnet.get_all_banks()
        self.assertIs(vnet.dep_all_banks_by_vnet(banklist), True, msg="Test fail!")

    def test_00002_VNet_one_bank(self):
        vnet = Deposit_by_VNet()
        self.assertIs(vnet.dep_one_bank_by_vnet(), True, msg="Test fail!")

    def test_00003_VNet(self):
        pass

    def tearDown(self):
        """
        函數級別 - 測試結束後的操作，這裡基本上都是關閉瀏覽器 (but 已在test case中關閉)
        函數結束 - 每條case之後執行
        """
        print("Cost time is " + str(time() - self.sTime))

    @classmethod
    def tearDownClass(cls):
        """
        類級別: 類結束 - 所有case執行之後的後置
        """
        print("The total time of test cases is " + str(time() - cls.tTime))


if __name__ == '__main__':
    unittest.main(verbosity=2)
