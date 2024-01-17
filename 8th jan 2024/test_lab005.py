import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome -> chrome options
#edge - > edge options
#firefox -> firefox otions


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/xpath/")


    ancestor_of_mammal = driver.find_element(By.XPATH, "//div[@class= 'Mammal']/ancestor::div")
    print(ancestor_of_mammal.text)



    assert driver.current_url == "https://awesomeqa.com/xpath/"
    time.sleep(20)

    driver.quit()

def test_open_login_ebay():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    assert driver.current_url == "https://www.ebay.com/"

    search_box = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    search_box.send_keys("16 gb")

    search_btn = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_btn.click()

    list_results = driver.find_elements(By.XPATH,"//span[@role='heading']")
    for i in list_results:
        print(i.text)


    time.sleep(10)

    driver.quit()

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    #assert driver.current_url == "https://app.vwo.com/"

    email_input = driver.find_element(By.CSS_SELECTOR, "#login-username")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    submit_input = driver.find_element(By.CSS_SELECTOR, "button[id='js-login-btn']")

    email_input.send_keys("san@email.com")
    pass_input.send_keys("admin123")

    submit_input.click()


    time.sleep(5)

    driver.quit()

