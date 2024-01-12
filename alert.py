
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://brightinfo.in/login.html")
driver.maximize_window()

driver.find_element(By.ID,'username').send_keys("Bright@123")
driver.find_element(By.ID,'password').send_keys("pass123")
driver.find_element(By.XPATH,'/html/body/div[1]/div/form/div[3]/div/button/b').click()

driver.find_element(By.XPATH,'//*[@id="sidebar"]/ul/li[3]/ul[2]/li[2]/a').click()

driver.find_element(By.XPATH,'//*[@id="content"]/button[1]').click()
ab=driver.switch_to.alert
ab.accept()




#driver.find_element(By.XPATH,'//*[@id="homeSubmenu"]/li[2]/a').click()
