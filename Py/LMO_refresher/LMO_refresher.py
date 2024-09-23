from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from datetime import datetime
import time

# 设置Chrome浏览器的路径（如果ChromeDriver不在系统路径中）
chrome_driver_path = r"C:\Tools\chromedriver-win64\chromedriver.exe"# 使用原始字符串

user_name = "Mochi.Pan23"
password = "xjtlu-panmochi@180305"

Bottom1_XP = "/html/body/div[2]/div[2]/div/div/section/div/div/div/div/div[2]/div[1]/a"
# UserName_XP = "//*[@id=\"username_show\"]"
# Passward_XP = "//*[@id=\"password_show\"]"
# lgin_XP = "/html/body/div[2]/div/div/div[2]/form[1]/div[2]/div/input"

# DDL_XP = "/html/body/div[3]/div[4]/div/div[2]/div/section/div/aside/section[6]/div"



# 创建Service对象
service = Service(chrome_driver_path)

# 创建Chrome浏览器的实例
driver = webdriver.Chrome(service=service)

# 打开指定的网页
url = 'https://core.xjtlu.edu.cn/'
driver.get(url)
wait = WebDriverWait(driver, 10)

botton1 = driver.find_element(By.XPATH, Bottom1_XP)
botton1.click()
UserName = driver.find_element(By.ID,'username_show')
UserName.send_keys(user_name)

Passward = driver.find_element(By.ID,'password_show')
Passward.send_keys(password)
Passward.send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 10)

# 获取页面初始高度
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 将网页滚动到页面底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 等待页面加载完成
    time.sleep(2)  # 你可以根据需要调整等待时间

    # 获取新的页面高度
    new_height = driver.execute_script("return document.body.scrollHeight")

    # 检查页面高度是否发生变化
    if new_height == last_height:
        break

    last_height = new_height
# element = wait.until(EC.presence_of_element_located((By.XPATH, DDL_XP)))  # 请替换为实际的元素定位方式
download_folder = r"C:\Users\pan\Downloads"
nowtime = datetime.now().strftime('%Y%m%d_%H%M')
screenshot_path = os.path.join(download_folder, f'element_screenshot_{nowtime}.png')
# 截取整个页面的截图并保存
driver.save_screenshot(screenshot_path)

print(f"元素截图已保存到: {screenshot_path}")


# 最后关闭浏览器
driver.quit()


