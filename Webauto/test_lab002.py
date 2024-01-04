import time
from selenium import webdriver

#Chrome -> chrome options
#edge - > edge options
#firefox -> firefox otions


def test_open_login():
    chrome_options = webdriver.ChromeOptions()

    extension_path = "/Users/HP/Downloads/adblocker.crx"
    chrome_options.add_extension(extension_path)

    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://google.com")
    driver.maximize_window()

    print(driver.title)
    time.sleep(2000)

    #good practise to use this
    driver.quit() #close all the windows