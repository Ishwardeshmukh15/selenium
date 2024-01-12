
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
chk1 = driver.find_element(By.XPATH,'//*[@id="checkbox1"]')
if chk1.is_selected():
    pass
else:
    chk1.click()

chk2 = driver.find_element(By.XPATH,'//*[@id="checkbox2"]')
if chk2.is_selected():
    pass
else:
    chk2.click()


