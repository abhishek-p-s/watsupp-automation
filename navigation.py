from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get('https://www.kali.org/')
print(driver.title)
time.sleep(2)
driver.get('https://www.facebook.com/')
print(driver.title)
time.sleep(2)
driver.back()

time.sleep(2)
print(driver.title)
driver.forward()

time.sleep(2)
print(driver.title)
driver.quit()



