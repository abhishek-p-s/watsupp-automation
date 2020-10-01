from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.flipkart.com/')
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)


