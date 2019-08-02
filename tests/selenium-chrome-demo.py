import unittest
from pages import seleniumhq_home_page

# Python demo - chrome driver
class SeleniumChromeTest(unittest.TestCase):

    def setUp(self):
        self.driver = seleniumhq_home_page.launch_browser("chrome")

    def test_selenium_homepage(self):
        self.assertEqual("Selenium - Web Browser Automation",self.driver.title)

    def test_about_selenium_page(self):
        seleniumhq_home_page.click_about_link(self.driver)
        self.assertEqual("About Selenium", self.driver.title)


    def test_search(self):
        seleniumhq_home_page.click_about_link(self.driver)
        seleniumhq_home_page.enter_search(self.driver,"Automation")
        seleniumhq_home_page.click_go(self.driver)
        self.assertEqual("Google Custom Search", self.driver.title)

    def test_back(self):
        seleniumhq_home_page.click_about_link(self.driver)
        seleniumhq_home_page.enter_search(self.driver, "Automation")
        seleniumhq_home_page.click_go(self.driver)
        seleniumhq_home_page.click_back(self.driver)
        self.assertEqual("About Selenium", self.driver.title)

    def tearDown(self):
        seleniumhq_home_page.close_browser(self.driver)

if __name__ == '__main__':
    unittest.main()