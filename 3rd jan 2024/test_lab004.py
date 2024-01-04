import time
from selenium import webdriver

#Chrome -> chrome options
#edge - > edge options
#firefox -> firefox otions


def test_open_login():


    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.maximize_window()

    print(driver.title)
    time.sleep(2000)

    #driver.navigate to x
    #good practise to use this
    driver.quit() #close all the windows
    #session == none

    driver.close() # close the current window
    #it will not close the other tabs
    # seion != none