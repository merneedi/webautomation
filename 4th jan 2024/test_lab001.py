import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome -> chrome options
#edge - > edge options
#firefox -> firefox otions


def test_open_login():


    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    #driver.maximize_window()

    #make_appointment_btn = driver.find_element(By.ID, 'btn-make-appointment')
    #make_appointment_btn.click()

    #mp_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Appointment")
    #mp_btn.click()

    #mp_btn = driver.find_elements(By.CLASS_NAME, "btn.btn-dark.btn-lg")
    #mp_btn[1].click()

    mp_btn = driver.find_elements(By.TAG_NAME, "a")
    mp_btn[5].click()

    #click on the app
    # <a
    # id = 'btn-make-appointment'
    # Make Appointment
    # </a>

# Link text is full exact match
# Partial means contains

    # ID-unique Id
    # name, classname,
    # Tagname -
    # Link/partial
    # css selector
    # xpath
