
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

input("please scan qr code and press any key to continue.......")
name=driver.find_element_by_css_selector('span[title="Chechi"]')
name.click()
testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]")

testinput.send_keys("hi")



















