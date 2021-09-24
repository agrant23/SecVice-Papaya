from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import by
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

class UboldPage():

    options = Options()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')

    def __init__(self, driver):
        self.driver = driver
        driver.get("https://qa.papaya.secvise.com/")

    #NAVIGATION BAR

    def click_ubold_logo_link(self):
        ubold_logo_link_loc = (by.XPATH,)

