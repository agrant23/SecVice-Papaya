from selenium import webdriver
import unittest
from ubold_homepage import UboldHomePage
import settings
import time
class HomePageSetup(unittest.TestCase):

    def setUp(self):
        options = UboldHomePage.options
        self.driver = webdriver.Chrome(
                                   settings.path_to_webdriver, options=options)
        UboldHomePage(self.driver)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
