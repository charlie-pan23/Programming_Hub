import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By





exlpath = "D:\Programming_Hub\Py\Py_EOA_searcher\EOA_accounts.xlsx"
xlsx1 = pd.read_excel(exlpath,sheet_name='Sheet1')
addr = search_terms = xlsx1['Address'].tolist()

target_web = 'https://bscscan.com/'
driver = webdriver.Chrome()


for n in range(len(addr)):

    driver.get(target_web)
    wait = WebDriverWait(driver, 10)
    search_box = driver.find_element(By.ID,'search-panel')
    search_box.send_keys(addr[n])
    search_box.send_keys(Keys.ENTER)
    wait = WebDriverWait(driver, 10)
    botton1 = driver.find_element(By.ID,'lnkTxAgeDateTime')
    botton1.click()
    total_value = driver.find_element(By.XPATH,'/html/body/main/section[3]/div[4]/div[1]/div/div[2]/table/tbody/tr[1]/td[5]/span')
    print(total_value.text)
    time.sleep(2)
    #print(addr[n])