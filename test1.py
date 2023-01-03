from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()

# 네이버로 이동
driver.get('https://www.naver.com/')
# elem 변수 지정
elem = driver.find_element(By.ID, 'query')
elem.send_keys('최은진')

# elem.send_keys(Keys.RETURN)

btn_elm = driver.find_element(By.ID, 'search_btn')
btn_elm.click()

sleep(30)
driver.quit()
