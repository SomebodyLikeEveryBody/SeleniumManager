######### [CONFIG] #########

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By

options = Options()
options.binary = FirefoxBinary(r'/usr/bin/firefox')
driver = webdriver.Firefox(executable_path=r'./geckodriver', options=options)

######### [END: CONFIG] #####))

def get(pUrl):
    driver.get(pUrl)

def close():
    driver.close()

def find_elements(pSelection):
    return driver.find_elements(By.CSS_SELECTOR, pSelection)
