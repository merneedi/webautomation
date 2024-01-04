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

