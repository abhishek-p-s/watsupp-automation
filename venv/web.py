
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div/span/div/div/div').click()
driver.close()









