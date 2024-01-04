import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome -> chrome options
#edge - > edge options
#firefox -> firefox otions


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_btn = driver.find_element(By.ID, 'btn-make-appointment')
    make_appointment_btn.click()

    print(driver.current_url)

#assert
    assert driver.current_url == ""

    username = driver.find_element(By.NAME,'username')
    username.send_keys("John")

    password = driver.find_element(By.ID, 'password')
    password.send_keys("ThisIsNotPassword")

    submit_btn = driver.find_element(By.ID, 'btn-login')
    submit_btn.click()