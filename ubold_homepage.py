from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
import time
from ubold_basepage import UboldBasePage


class UboldHomePage(UboldBasePage):

    def __init__(self,spawn=True):
        """
        inputs
        -----
        spawn: bool
            The default case is for the driver to open the homepage. Or, the
            spawning of homepage is True and will occur. Spawn input exist's to
            alter this if desired.
        """
        if spawn: UboldBasePage.driver.get("https://qa.papaya.secvise.com/")

    #NAVIGATION BAR

    def click_ubold_logo_link(self):
        ubold_logo_link_loc = (By.XPATH,'//a[contains(@class,"logo")]')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(ubold_logo_link_loc))
        self.driver.find_element(*ubold_logo_link_loc).click()