from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.get('https://www.facebook.com/')
driver.maximize_window()

driver.find_element_by_name('firstname').send_keys("Akshay")
driver.find_element_by_name('lastname').send_keys("MR")
driver.find_element_by_name('reg_email__').send_keys("akshaymr@gmail.com")
driver.find_element_by_name('reg_email_confirmation__').send_keys("akshaymr@gmail.com")
driver.find_element_by_name('reg_passwd__').send_keys("podamyre")

day=driver.find_element_by_name('birthday_day')
days=Select(day)
days.select_by_value("27")

month=driver.find_element_by_name('birthday_month')
months=Select(month)
months.select_by_value("2")

year=driver.find_element_by_name('birthday_year')
years=Select(year)
years.select_by_value("2000")

driver.find_element_by_id("u_0_7").click()












