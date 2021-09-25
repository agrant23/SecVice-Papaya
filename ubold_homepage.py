from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException

class UboldHomePage():

    options = Options()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')

    def __init__(self, driver):
        self.driver = driver
        driver.get("https://qa.papaya.secvise.com/")

    #NAVIGATION BAR

    def click_ubold_logo_link(self):
        ubold_logo_link_loc = (By.XPATH,'//a[contains(@class,"logo")]')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(ubold_logo_link_loc))
        self.driver.find_element(*ubold_logo_link_loc).click()

    #FIELDS

    def username_field(self):
        username_field_loc = (By.ID, 'emailaddress')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(username_field_loc))
        return self.driver.find_element(*username_field_loc)

    def input_username_field(self, userName):
        self.username_field().send_keys(userName)

    def password_field(self):
        password_field_loc = (By.ID, 'password')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(password_field_loc))
        return self.driver.find_element(*password_field_loc)

    def input_password_field(self, userName):
        self.password_field().send_keys(userName)

    #CHECK BOX

    def click_remember_me_box(self):
        remember_me_box_loc = (By.ID, 'checkbox-signin')
        self.driver.find_element(*remember_me_box_loc).click()
