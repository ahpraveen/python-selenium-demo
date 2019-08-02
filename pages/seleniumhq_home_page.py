from selenium import webdriver

def launch_browser(browser_name):
    try:
        if browser_name == "chrome":
            mydriver = webdriver.Chrome("../../driver/chromedriver.exe")
        elif browser_name == "firefox":
            mydriver = webdriver.Firefox()
        elif browser_name == "ie":
            mydriver = webdriver.Ie('../../driver/IEDriverServer.exe')
        else:
            raise NameError('Error')
        mydriver.get("https://www.seleniumhq.org/")
        return mydriver
    except NameError:
        return "browser name is incorrect"

def click_about_link(driver):
    driver.find_element_by_partial_link_text("About").click()

def enter_search(driver, search_text):
    driver.find_element_by_id("q").send_keys(search_text)

def click_go(driver):
    driver.find_element_by_id("submit").click()

def click_back(driver):
    driver.back()

def close_browser(driver):
    driver.close()