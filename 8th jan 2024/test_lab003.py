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


    # // tagname[@attribute=value]
    #// selectorshub.com - xpath
    make_appointment_btn = driver.find_element(By.XPATH,"//a[@id='btn-make-appointment']")
    make_appointment_btn_text = driver.find_element(By.XPATH, "//a[text() ='Make Appointment']")
    #make_appointment_btn_partial = driver.find_element(By.XPATH, "//a[contains(text(), 'Make App')]")
    #make_appointment_btn.click()
    #make_appointment_btn_partial.click()



    #Partial Match

    #Contains
    # // a[contains(text(), 'Make App' )]
    # // a[contains(text(), 'Make' )]

    list_elements_p = driver.find_elements(By.XPATH,"//p[contains(text(),'A')]")
    for i in list_elements_p:
        if i.text == "Copyright":
            i.click()
        print(i.text)

    # starts-with
    # //a[starts-with(text(), 'Make')]
    # End-with

    # Find the p tag via the contains functions
    # //p[contains(text(), 'Copyright')]

    ptag = driver.find_element(By.CLASS_NAME, "text-muted")
    print(ptag.text)



    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(20)

    driver.quit()
