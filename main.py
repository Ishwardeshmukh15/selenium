#driver.find_element(By.XPATH,'//*[@id="footer"]/div[2]/div/div/a').click()
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://brightinfo.in/login.html")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.ID,'username').send_keys("Bright@123")
driver.find_element(By.ID,'password').send_keys("pass123")
driver.find_element(By.XPATH,'/html/body/div[1]/div/form/div[3]/div/button/b').click()

driver.find_element(By.XPATH,'//*[@id="homeSubmenu"]/li[2]/a').click()

driver.find_element(By.XPATH,'//*[@id="myCheck"]').click()


