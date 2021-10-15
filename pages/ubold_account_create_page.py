import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
import settings


class UboldAccountCreatePage():
    def __init__(self, driver, spawn = False):
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
        if spawn: self.driver.get("https://dev.papaya.secvise.com/register")

    #FIELDS

    def firstname_field(self):
        firstname_field_loc = (By.ID,'fullname')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(firstname_field_loc))
        return self.driver.find_element(*firstname_field_loc)
    
    def input_firstname_field(self, firstName):
        self.firstname_field().send_keys(firstName)

    def lastname_field(self):
        lastname_field_loc = (By.ID,'last_name')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(lastname_field_loc))
        return self.driver.find_element(*lastname_field_loc)
    
    def input_lastname_field(self, lastName):
        self.lastname_field().send_keys(lastName)

    def email_field(self):
        email_field_loc = (By.ID,'emailaddress')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(email_field_loc))
        return self.driver.find_element(*email_field_loc)
    
    def input_email_field(self, email):
        self.email_field().send_keys(email)
    
    def username_field(self):
        username_field_loc = (By.ID,'username')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(username_field_loc))
        return self.driver.find_element(*username_field_loc)
    
    def input_username_field(self, username):
        self.username_field().send_keys(username)
    
    def phone_num_field(self):
        phone_num_field_loc = (By.ID,'phone')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(phone_num_field_loc))
        return self.driver.find_element(*phone_num_field_loc)
    
    def input_phone_num_field(self, phone_num):
        self.phone_num_field().send_keys(phone_num)

    def org_name_field(self):
        org_name_field_loc = (By.ID,'organization_name')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(org_name_field_loc))
        return self.driver.find_element(*org_name_field_loc)
    
    def input_org_name_field(self, org_name):
        self.org_name_field().send_keys(org_name)

    def password_field(self):
        password_field_loc = (By.ID,'password')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(password_field_loc))
        return self.driver.find_element(*password_field_loc)
    
    def input_password_field(self, password):
        self.password_field().send_keys(password)

    def password_confirm_field(self):
        password_confirm_field_loc = (By.ID,'c_password')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(password_confirm_field_loc))
        return self.driver.find_element(*password_confirm_field_loc)
    
    def input_password_confirm_field(self, password_confirm):
        self.password_confirm_field().send_keys(password_confirm)

    #CHECK BOX

    def click_accept_terms_box(self):
        accept_terms_box_loc = (By.ID, 'checkbox-signup')

        self.driver.execute_script("arguments[0].scrollIntoView();",
            wait(self.driver, 20).until(
                EC.visibility_of_element_located(accept_terms_box_loc)))
        time.sleep(0.2)  #I know this is suboptimal I will come back and fix this
        self.driver.find_element(*accept_terms_box_loc).click()
        #ActionChains(self.driver).move_to_element(wait(self.driver, 20).until(EC.element_to_be_clickable(accept_terms_box_loc))).click().perform() 

    #BUTTONS

    def click_signup_button(self):
        signup_button_loc = (By.XPATH,"//button[contains(text(),'Sign Up')]")
        self.driver.execute_script("arguments[0].scrollIntoView();",
            wait(self.driver, 20).until(
                EC.visibility_of_element_located(signup_button_loc)))
        time.sleep(0.2)  #I know this is suboptimal I will come back and fix this
        url_before_click = self.driver.current_url
        self.driver.find_element(*signup_button_loc).click()
        wait(self.driver, 15).until(EC.url_changes(url_before_click))

    #ERROR MESSAGES

    def username_status_message(self):
        username_status_loc = (By.ID, "parsley-id-11")
        username_status_element = wait(self.driver, 15).until(
            EC.presence_of_element_located(username_status_loc))
        return username_status_element
    
    def account_create_status_message(self):
        account_create_status_loc = (
            By.XPATH, "//div[contains(@class,'alert-danger')]")
        account_create_status_element = wait(self.driver, 15).until(
            EC.presence_of_element_located(account_create_status_loc))
        return account_create_status_element

    #CONFIRM MESSAGES

    def username_accept_message(self):
        username_accept_mess_loc = (By.XPATH, "//div[contains(@class , 'uname')]")
        username_accept_mess_element = wait(self.driver, 15).until(
            EC.presence_of_element_located(username_accept_mess_loc))
        return username_accept_mess_element

    def account_create(self):
        self.input_firstname_field("Tony")
        self.input_lastname_field("Grant")
        #the email must be changed after each passing test
        self.input_email_field("madeUpemail456@gmail.com")
        #the username must be changed after each passing test
        self.input_username_field(settings.ubold_username)
        self.input_phone_num_field("3093103171")
        self.input_org_name_field("SecVice")
        self.input_password_field(settings.ubold_password)
        self.input_password_confirm_field(settings.ubold_password)
        self.click_accept_terms_box()
        self.click_signup_button()