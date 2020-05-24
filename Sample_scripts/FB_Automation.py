from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome(r'C:\Users\mkmur\OneDrive - Hewlett Packard Enterprise\Personal\Study\Python\Mytectra\chromedriver_win32\chromedriver.exe')
driver.get('https:/www.facebook.com')
driver.maximize_window()
time.sleep(3)
driver.find_element_by_id('email').send_keys('muruganmk8@live.com')
driver.find_element_by_name('pass').send_keys('Temp#123')
driver.find_element_by_id('loginbutton').click()
