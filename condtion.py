from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('https://www.facebook.com/')
driver.maximize_window()
time.sleep(10)
email=driver.find_element_by_name('email')
print(email.is_displayed())
print(email.is_enabled())

password=driver.find_element_by_name('pass')
print(password.is_displayed())
print(password.is_enabled())

email.send_keys("aneeshaks2001@gmail.com")
password.send_keys("abhishek")

button=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input')
button.click()
forget=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/form/div/div[4]/div/a')
forget.click()
driver.back()
driver.back()






