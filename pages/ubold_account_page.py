from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class UboldAccountPage():
    def __init__(self,driver, spawn = False):
        """
        inputs
        -----
        spawn: bool
            The default case is that the driver will already be at the sign in 
            page as part of a user workflow. Or there is no need to spawn the 
            sign in page (spawn is False). Spawn input exist's to alter this if
            desired.
        """
        self.driver = driver
        if spawn: self.driver.get(
            "https://https://dev.papaya.secvise.com/organization-scope")

    #NAVIGATION BAR

    def first_name(self):
        first_name_loc = (By.XPATH,'//span[contains(@class,"user-name")]')
        first_name_elem = wait(self.driver, 15).until(
            EC.visibility_of_element_located(first_name_loc))
        return first_name_elem