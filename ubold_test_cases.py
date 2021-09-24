from selenium import webdriver
import unittest
from ubold_page import UboldPage
import settings
import time
class HomePageSetup(unittest.TestCase):

    def setUp(self):
        options = Uboldage.options
        self.driver = webdriver.Chrome(
                                   settings.path_to_webdriver, options=options)
        UboldPage(self.driver)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
