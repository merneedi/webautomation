import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome -> chrome options
#edge - > edge options
#firefox -> firefox otions


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    #relative xpath
    rel_xpath_email = driver.find_element(By.XPATH,"//input[@type='email']")
    rel_xpath_email.send_keys("admin@idrive.com")






    time.sleep(20)

    driver.quit()
