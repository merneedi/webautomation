from selenium import webdriver

def test_open_google():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    print(driver.title)