
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://brightinfo.in/login.html")
driver.maximize_window()

driver.save_screenshot("C:\\hp\\BIN\\qwerty\\unit.png")
