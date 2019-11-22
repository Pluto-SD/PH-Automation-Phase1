# coding=UTF-8

import os


def load_amt():
    if os.path.isfile("txnamt.csv"):
        print("檔案 - txnamt.csv 存在.")
        amt = []
        # Read file
        with open("txnamt.csv", "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                s = line.strip().split(',')     # split(',') 遇到 ',' 就切開分成另一個欄位
                case = s[0]
                item = s[1]
                data = s[2]
                if case == 'QR':     # Load how much amout that user select QR to deposit
                    amt.append([item, data])
                elif case == 'VNet':
                    pass
                else:
                    pass
            if amt != []:
                return amt
