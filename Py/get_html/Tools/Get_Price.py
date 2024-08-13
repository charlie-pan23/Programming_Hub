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

BTCB = ETH = USDT = BNB = SOL = USDC = WBTC = AVAX = DAI = MATIC = 0.0000001

try:
    driver = webdriver.Chrome()
    driver.minimize_window()
    driver.get(target_web)
    wait = WebDriverWait(driver, 10)
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
        elif name.text == 'SOL':
            SOL = (driver.find_element(By.XPATH,vl)).text
            print(i)
        elif name.text == 'USDC':
            USDC = (driver.find_element(By.XPATH,vl)).text
            print(i)
        elif name.text == 'WBTC':
            WBTC = (driver.find_element(By.XPATH,vl)).text
            print(i)
        elif name.text == 'AVAX':
            AVAX = (driver.find_element(By.XPATH,vl)).text
            print(i)
        elif name.text == 'DAI':
            DAI = (driver.find_element(By.XPATH,vl)).text
            print(i)
        elif name.text == 'MATIC':
            MATIC = (driver.find_element(By.XPATH,vl)).text
            print(i)

finally:
    driver.quit()

#将钱币形式转换成浮点数
BTCB = BTCB.replace("$", "").replace(",", "")
ETH = ETH.replace("$", "").replace(",", "")
USDT = USDT.replace("$", "").replace(",", "")
BNB = BNB.replace("$", "").replace(",", "")
SOL = SOL.replace("$", "").replace(",", "")
USDC = USDC.replace("$", "").replace(",", "")
WBTC = WBTC.replace("$", "").replace(",", "")
AVAX = AVAX.replace("$", "").replace(",", "")
DAI = DAI.replace("$", "").replace(",", "")
MATIC = MATIC.replace("$", "").replace(",", "")


BTCB = float(BTCB)
ETH = float(ETH)
USDT = float(USDT)
BNB = float(BNB)
SOL = float(SOL)
USDC = float(USDC)
WBTC = float(WBTC)
AVAX = float(AVAX)
DAI = float(DAI)
MATIC = float(MATIC)

# 使用openpyxl加载现有的Excel文件
workbook = load_workbook(filename=respath)
sheet = workbook['Price_TD']
# 将字符串填入特定单元格
sheet['B2'] = BTCB
sheet['B3'] = ETH
sheet['B4'] = USDT
sheet['B5'] = BNB
sheet['B6'] = SOL
sheet['B7'] = USDC
sheet['B8'] = WBTC
sheet['B9'] = AVAX
sheet['B10'] = DAI
sheet['B11'] = MATIC
# 保存修改后的文件
workbook.save(filename=respath)

