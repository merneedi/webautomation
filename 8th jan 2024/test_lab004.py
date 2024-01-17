import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome -> chrome options
#edge - > edge options
#firefox -> firefox otions


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    assert driver.title == "CURA Healthcare Service"



    make_appointment_btn_partial = driver.find_element(By.XPATH, "//a[contains(text(), 'Make App')]")
    make_appointment_btn_partial.click()



    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(20)

    driver.quit()

def test_open_login_Edge():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    assert driver.title == "CURA Healthcare Service"



    make_appointment_btn_partial = driver.find_element(By.XPATH, "//a[contains(text(), 'Make App')]")
    make_appointment_btn_partial.click()


    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(20)

    driver.quit()