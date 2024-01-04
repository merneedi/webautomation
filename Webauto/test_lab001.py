# QA -> Focus -> Testcase
from selenium import webdriver
import logging

def test_open_google():
    driver = webdriver.Chrome()
    LOGGER = logging.getLogger(__name__)
    # create a session with POST request (API POST request)
    # Fresh chrome browser will be open, session ID is created
    driver.get("https://google.com")
    driver.maximize_window()
    #print(driver.title)
    LOGGER.info(driver.title)

    #Session ID> close ID will be deleted
    #Multiple windows in same session