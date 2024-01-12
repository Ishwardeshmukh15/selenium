
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

radio = driver.find_element(By.XPATH,'//*[@id="radio1"]')
if radio.is_selected():
    pass
else:
    radio.click()

radio2 = driver.find_element(By.XPATH,'//*[@id="radio2"]')
if radio2.is_selected():
    pass
else:
    radio2.click()