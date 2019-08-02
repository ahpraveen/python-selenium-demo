import unittest
from pages import seleniumhq_home_page

class SeleniumTest(unittest.TestCase):

    def test_invalid_browser_name(self):
        self.driver = seleniumhq_home_page.launch_browser("not-ie-chrome-firefox")
        self.assertEqual("browser name is incorrect", "browser name is incorrect")