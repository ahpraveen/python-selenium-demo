from selenium import webdriver
import unittest

# Python demo - Firefox driver
class SeleniumFireFoxTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.seleniumhq.org/")

    def test_selenium_homepage(self):
        self.assertEqual("Selenium - Web Browser Automation",self.driver.title)

    def test_about_selenium_page(self):
        self.driver.find_element_by_partial_link_text("About").click()
        self.assertEqual("About Selenium", self.driver.title)


    def test_search(self):
        self.driver.find_element_by_partial_link_text("About").click()
        self.driver.find_element_by_id("q").send_keys("Automation")
        self.driver.find_element_by_id("submit").click()
        self.assertEqual("Google Custom Search", self.driver.title)

    def test_back(self):
        self.driver.find_element_by_partial_link_text("About").click()
        self.driver.find_element_by_id("q").send_keys("Automation")
        self.driver.find_element_by_id("submit").click()
        self.driver.back()
        self.assertEqual("About Selenium", self.driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
     unittest.main()