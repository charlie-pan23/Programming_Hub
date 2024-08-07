# import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
respath = "Price.xlsx"
# D:\Programming_Hub\Py\Get_Price\
target_web = "https://www.coingecko.com/"

driver = webdriver.Chrome()
driver.minimize_window()
driver.get(target_web)
wait = WebDriverWait(driver, 10)
BTCB = ETH = USDT = BNB = USDC = DAI = 0.0000001

try:
    # 搜取各币种价格
    for i in range(1,31):
        td = '/html/body/div[2]/main/div/div[5]/table/tbody/tr[' + str(i) +']/td[3]/a/div/div/div'
        vl = '/html/body/div[2]/main/div/div[5]/table/tbody/tr[' + str(i) +']/td[5]/span'
        name = driver.find_element(By.XPATH, td)

        if name.text == 'BTC':
            BTCB =(driver.find_element(By.XPATH,vl)).text
            print(i)
        elif name.text == 'ETH':
            ETH = (driver.find_element(By.XPATH,vl)).text
            print(i)
        elif name.text == 'USDT':
            USDT = (driver.find_element(By.XPATH,vl)).text
            print(i)
        elif name.text == 'BNB':
            BNB = (driver.find_element(By.XPATH,vl)).text
            print(i)
        elif name.text == 'USDC':
            USDC = (driver.find_element(By.XPATH,vl)).text
            print(i)
        elif name.text == 'DAI':
            DAI = (driver.find_element(By.XPATH,vl)).text
            print(i)
finally:
    driver.quit()

#将钱币形式转换成浮点数
BTCB = BTCB.replace("$", "").replace(",", "")
ETH = ETH.replace("$", "").replace(",", "")
USDT = USDT.replace("$", "").replace(",", "")
USDC = USDC.replace("$", "").replace(",", "")
DAI = DAI.replace("$", "").replace(",", "")
BNB = BNB.replace("$", "").replace(",", "")

BTCB = float(BTCB)
ETH = float(ETH)
USDT = float(USDT)
USDC = float(USDC)
DAI = float(DAI)
BNB = float(BNB)
# 使用openpyxl加载现有的Excel文件
workbook = load_workbook(filename=respath)
sheet = workbook['Price_TD']
# 将字符串填入特定单元格
sheet['B2'] = BTCB
sheet['B3'] = ETH
sheet['B4'] = USDT
sheet['B5'] = USDC
sheet['B6'] = DAI
sheet['B7'] = BNB
# 保存修改后的文件
workbook.save(filename=respath)

