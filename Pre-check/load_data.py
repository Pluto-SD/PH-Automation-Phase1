# coding=UTF-8

import os


# use for mobile - qr
def load_qr_amt():
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


# use for vnet
def load_vnet_amt():
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
                if case == '\ufeffVNet':     # Load how much amout that user select QR to deposit
                    amt.append([item, data])
                elif case == 'QR':
                    pass
                else:
                    pass
            if amt != []:
                return amt


# get client id
def load_precheck_client():
    if os.path.isfile("precheck_info.csv"):
        print("檔案 - precheck_info.csv 存在.")
        info = []
        # Read file
        with open("precheck_info.csv", "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                s = line.strip().split(',')     # split(',') 遇到 ',' 就切開分成另一個欄位
                case = s[0]
                item = s[1]
                data = s[2]
                if case == 'Precheck_C':     # Load the conditions of precheck
                    info.append([item, data])
                elif case == 'QR':
                    pass
                else:
                    pass
            if info != []:
                return info


# get precheck information
def load_precheck_info():
    if os.path.isfile("precheck_info.csv"):
        print("檔案 - precheck_info.csv 存在.")
        info = []
        # Read file
        with open("precheck_info.csv", "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                s = line.strip().split(',')     # split(',') 遇到 ',' 就切開分成另一個欄位
                case = s[0]
                item = s[1]
                data = s[2]
                if case == 'Precheck_S':     # Load the conditions of precheck
                    info.append([item, data])
                elif case == 'Precheck_C':
                    info.append([item, data])
                elif case == 'Precheck_M':
                    info.append([item, data])
                elif case == 'QR':
                    pass
                else:
                    pass
            if info != []:
                return info


if __name__ == "__main__":
    s = load_precheck_info()
    print(type(s))
    print(s)
    print(s[0][0])
    print(s[0][1])
