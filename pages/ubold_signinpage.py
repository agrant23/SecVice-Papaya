from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class UboldSignInPage():
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
        if spawn: self.driver.get("https://dev.papaya.secvise.com/login")

    #FIELDS

    def username_field(self):
        username_field_loc = (By.ID, 'username')
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
        wait(self.driver, 15).until(    #after testing I don't need this wait, so do I really need this
            EC.element_to_be_clickable(remember_me_box_loc))
        self.driver.find_element(*remember_me_box_loc).click()

    #BUTTONS

    def click_login_button(self):
        login_button_loc = (By.XPATH,"//button[contains(text(),'Log In')]")
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(login_button_loc))
        url_before_click = self.driver.current_url
        self.driver.find_element(*login_button_loc).click()
        wait(self.driver, 15).until(EC.url_changes(url_before_click))

    #USER FLOW

    def login(self):
        self.input_username_field("Tony")
        self.input_password_field("mypassword")
        self.click_login_button()
