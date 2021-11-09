from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import tools
import time


class UboldAccountPage():
    def __init__(self, driver, spawn=False):
        """
        inputs
        -----
        spawn: bool
            The default case is that the driver will already be at the sign in
            page as part of a user workflow. Or there is no need to spawn the
            sign in page (spawn is False). Spawn input exists to alter this if
            desired.
        """
        self.driver = driver
        if spawn:
            self.driver.get(
                   "https://https://dev.papaya.secvise.com/organization-scope")

    # CLASS VARIABLES

    scope_object_name = ""

    # NAVIGATION BAR

    def click_account_dropdown(self):
        account_dropdown_loc = (By.XPATH,
                                        '//span[contains(@class,"user-name")]')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(account_dropdown_loc)).click()

    def click_logout_dropdown_option(self):
        logout_dropdown_loc = (By.ID, 'logout-form')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(logout_dropdown_loc)).click()

    def first_name(self):
        first_name_loc = (By.XPATH, '//span[contains(@class,"user-name")]')
        first_name_elem = wait(self.driver, 15).until(
            EC.visibility_of_element_located(first_name_loc))
        return first_name_elem

    # SIDEBAR

    def click_org_scope_link(self):
        org_scope_loc = (By.XPATH, '//span[text()="Organization & Scope"]')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(org_scope_loc)).click()

    def click_view_all_scopes_link(self):
        all_scopes_loc = (By.ID, 'sidebarscope')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(all_scopes_loc)).click()

    # BUTTONS

    def click_scope_object_button(self):
        scope_object_create_button_loc = (By.XPATH,
                                 '//button[contains(text(), "Begin Scoping")]')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(scope_object_create_button_loc))
        self.driver.find_element(*scope_object_create_button_loc).click()

    def click_scope_object_button_w_obj_saved(self):
        """
        This click is needed because a different scope object button needs
        to be clicked when one scope object has already been saved.
        """
        scope_object_begin_button_loc = (By.XPATH,
                                      '//button[contains(text(),"Start New")]')
        self.driver.refresh()
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(scope_object_begin_button_loc))
        self.driver.find_element(*scope_object_begin_button_loc).click()

    def click_start_scope_button(self):
        start_scope_object_button_loc = (By.XPATH,
                '//form[@id="default_form"]//button[contains(text(),"Start")]')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(start_scope_object_button_loc))
        url_before_click = self.driver.current_url
        self.driver.find_element(*start_scope_object_button_loc).click()
        wait(self.driver, 15).until(EC.url_changes(url_before_click))

    def click_scope_business_info_next_button(self):
        bus_info_next_loc = (By.XPATH,
                               '//div[@id="businessDetail"]//a[text()="Next"]')
        self.driver.execute_script(
                               "window.scrollTo(0,document.body.scrollHeight)")
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(bus_info_next_loc)).click()

    def click_scope_industry_next_button(self):
        bus_done_next_loc = (By.XPATH,
                               '//div[@id="industryDetail"]//a[text()="Next"]')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(bus_done_next_loc))
        self.driver.find_element(*bus_done_next_loc).click()

    def click_scope_business_activity_next_button(self):
        bus_activity_next_loc = (By.XPATH,
                       '//div[@id="businessActivityDetail"]//a[text()="Next"]')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(bus_activity_next_loc))
        self.driver.find_element(*bus_activity_next_loc).click()

    def click_scope_technology_next_button(self):
        technology_next_loc = (By.XPATH,
                             '//div[@id="technologyDetail"]//a[text()="Next"]')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(technology_next_loc))
        self.driver.find_element(*technology_next_loc).click()

    # FIELDS

    def scope_object_name_field(self):
        scope_object_name_loc = (By.ID, 'name')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(scope_object_name_loc))
        return self.driver.find_element(*scope_object_name_loc)

    def input_scope_object_name_field(self, scope_object_name):
        self.scope_object_name_field().send_keys(scope_object_name)

    def scope_num_employees_field(self):
        scope_num_employees_loc = (By.ID, 'num_employees')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(scope_num_employees_loc))
        return self.driver.find_element(*scope_num_employees_loc)

    def input_scope_num_employees(self, scope_num_employees):
        """
        The wait in this method fixed a bug. Before this wait was implemented
        the user input was not always saved in the field before the next button
        was clicked.
        """
        self.scope_num_employees_field().send_keys(scope_num_employees)
        scope_num_employees_loc = (By.ID, 'num_employees')
        wait(self.driver, 15).until(tools.input_value_is_present(
            scope_num_employees_loc))

    def scope_num_customers_field(self):
        scope_num_customers_loc = (By.ID, 'num_customers')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(scope_num_customers_loc))
        return self.driver.find_element(*scope_num_customers_loc)

    def input_scope_num_customers(self, scope_num_customers):
        self.scope_num_customers_field().send_keys(scope_num_customers)

    def scope_bus_address_field(self):
        scope_object_bus_address_loc = (By.ID, 'business_address_1')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(scope_object_bus_address_loc))
        return self.driver.find_element(*scope_object_bus_address_loc)

    def input_scope_bus_adress(self, scope_bus_address):
        self.scope_bus_address_field().send_keys(scope_bus_address)

    def scope_bus_city_field(self):
        scope_bus_city_loc = (By.ID, 'business_city')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(scope_bus_city_loc))
        return self.driver.find_element(*scope_bus_city_loc)

    def input_scope_bus_city(self, scope_bus_adress):
        self.scope_bus_city_field().send_keys(scope_bus_adress)

    def scope_bus_state_field(self):
        scope_bus_state_loc = (By.ID, 'business_state_provence')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(scope_bus_state_loc))
        return self.driver.find_element(*scope_bus_state_loc)

    def input_scope_bus_state(self, scope_bus_state):
        self.scope_bus_state_field().send_keys(scope_bus_state)

    def scope_bus_zip_field(self):
        scope_bus_zip_loc = (By.ID, 'business_postal_code')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(scope_bus_zip_loc))
        return self.driver.find_element(*scope_bus_zip_loc)

    def input_scope_bus_zip(self, scope_bus_state):
        self.scope_bus_zip_field().send_keys(scope_bus_state)

    def scope_bus_phone_field(self):
        scope_bus_phone_loc = (By.ID, 'business_phone')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(scope_bus_phone_loc))
        return self.driver.find_element(*scope_bus_phone_loc)

    def input_scope_bus_phone(self, scope_bus_phone):
        self.scope_bus_phone_field().send_keys(scope_bus_phone)

    def scope_IT_sec_count_field(self):
        scope_IT_sec_count_loc = (By.ID, 'it_security_headcount')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(scope_IT_sec_count_loc))
        return self.driver.find_element(*scope_IT_sec_count_loc)

    def input_scope_IT_sec_count(self, scope_IT_sec_count):
        self.scope_IT_sec_count_field().send_keys(scope_IT_sec_count)

    def scope_prim_contact_field(self):
        scope_prim_contact_loc = (By.ID, 'primary_contact')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(scope_prim_contact_loc))
        return self.driver.find_element(*scope_prim_contact_loc)

    def input_scope_prim_contact(self, scope_prim_contact):
        self.scope_prim_contact_field().send_keys(scope_prim_contact)

    # DROP DOWNS

    def click_scope_location_drop_down(self):
        scope_location_locator = (By.ID, 'location')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(scope_location_locator))
        self.driver.find_element(*scope_location_locator).click()

    def click_scope_random_location_drop_down_option(self):
        scope_locations_opt_loc = (By.XPATH, '//select[@id="location"]/option')
        wait(self.driver, 15).until(
            EC.presence_of_all_elements_located(scope_locations_opt_loc))
        all_scope_locations = self.driver.find_elements(*scope_locations_opt_loc)
        scope_random_location = all_scope_locations[
                                               tools.generate_random_num(1, 3)]
        scope_random_location.click()

    def click_scope_revenue_drop_down(self):
        scope_revenue_loc = (By.ID, 'revenue')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(scope_revenue_loc))
        self.driver.find_element(*scope_revenue_loc).click()

    def click_scope_random_revenue_drop_down_option(self):
        scope_revenue_opt_loc = (By.XPATH, '//select[@id="revenue"]/option')
        wait(self.driver, 15).until(
            EC.presence_of_all_elements_located(scope_revenue_opt_loc))
        all_scope_revenues = self.driver.find_elements(
                                                 *scope_revenue_opt_loc)
        scope_random_revenue = all_scope_revenues[
                                               tools.generate_random_num(1, 3)]
        scope_random_revenue.click()

    def click_scope_bus_country_drop_down(self):
        scope_bus_country_loc = (By.ID, 'business_country')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(scope_bus_country_loc))
        self.driver.find_element(*scope_bus_country_loc).click()

    def click_scope_random_bus_country_drop_down_option(self):
        scope_bus_country_opt_loc = (
                           By.XPATH, '//select[@id="business_country"]/option')
        wait(self.driver, 15).until(
            EC.presence_of_all_elements_located(scope_bus_country_opt_loc))
        all_scope_bus_countries = self.driver.find_elements(
                                                    *scope_bus_country_opt_loc)
        scope_random_bus_country = all_scope_bus_countries[
                  tools.generate_random_num(1, len(all_scope_bus_countries)-1)]
        scope_random_bus_country.click()

    def click_scope_industry_drop_down(self):
        scope_object_industry_loc = (By.ID, 'industry_id')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(scope_object_industry_loc))
        self.driver.find_element(*scope_object_industry_loc).click()

    def click_scope_random_industry_drop_down_option(self):
        scope_industry_opt_loc = (By.XPATH,
                                          '//select[@id="industry_id"]/option')
        wait(self.driver, 15).until(
            EC.presence_of_all_elements_located(scope_industry_opt_loc))
        all_scope_industries = self.driver.find_elements(
                                
                                
                                
                                                       *scope_industry_opt_loc)
        scope_random_industry = all_scope_industries[
                     tools.generate_random_num(1, len(all_scope_industries)-1)]
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(scope_random_industry.text))
        scope_random_industry.click()

    # CHECKBOXES

    def click_scope_random_bus_activities(self):
        scope_bus_activities_array_loc = (By.XPATH,
                                   "//div[@id='business_activity_box']//input")
        tools.random_num_clicks_random_elements(
            self.driver, scope_bus_activities_array_loc)

    # BODY SCOPE

    def delete_all_scope_objects(self):
        """
        This method deletes all scope objects and clicks all the following
        dialogue boxes to confirm it. If there are no scope objects to delete
        the method is exited.
        """
        scope_obj_del_link_array_loc = (By.XPATH,
                                              '//i[contains(@class,"delete")]')
        confirm_delete_loc = (By.XPATH, '//button[text()="Yes, delete it!"]')
        delete_ok_confirm_loc = (By.XPATH, '//button[text()="OK"]')
        try:
            scope_obj_del_link_array = wait(self.driver, 3).until(
                EC.visibility_of_all_elements_located(
                                        scope_obj_del_link_array_loc))
        except TimeoutException:
            return
        i = 0
        for i in range(len(scope_obj_del_link_array)):
            scope_obj_del_link_array = wait(self.driver, 15).until(
                EC.visibility_of_all_elements_located(
                                                 scope_obj_del_link_array_loc))
            scope_obj_del_link_array[0].click()
            wait(self.driver, 15).until(
                EC.element_to_be_clickable(confirm_delete_loc)).click()
            wait(self.driver, 51).until(
                EC.element_to_be_clickable(delete_ok_confirm_loc)).click()

    def created_scope_object_name(self):
        created_scope_object_name_loc = (By.CLASS_NAME, "scope_name")
        created_scope_object_name = wait(self.driver, 15).until(
            EC.visibility_of_element_located(created_scope_object_name_loc))
        return created_scope_object_name.text

    # USER FLOWS

    def logout_account(self):
        self.click_account_dropdown()
        self.click_logout_dropdown_option()

    def create_scope_object(self):
        self.click_scope_object_button()
        self.scope_object_name = tools.generate_random_string(15,punctuation=False)
        self.input_scope_object_name_field(self.scope_object_name)
        self.click_start_scope_button()
        self.input_scope_num_employees(tools.generate_random_num(1, 99999))
        self.click_scope_location_drop_down()
        self.click_scope_random_location_drop_down_option()
        self.click_scope_revenue_drop_down()
        self.click_scope_random_revenue_drop_down_option()
        self.input_scope_num_customers(tools.generate_random_num(1, 99999))
        self.input_scope_bus_adress('1331 W. Loyola Ave. Apt 407')
        self.input_scope_bus_city('Chicago')
        self.input_scope_bus_state('Illinois')
        self.input_scope_bus_zip('60626')
        self.click_scope_bus_country_drop_down()
        self.click_scope_random_bus_country_drop_down_option()
        self.input_scope_bus_phone('3096635692')
        self.input_scope_IT_sec_count('5')
        self.input_scope_prim_contact('Business Phone')
        self.click_scope_business_info_next_button()
        self.click_scope_industry_drop_down()
        self.click_scope_random_industry_drop_down_option()
        self.click_scope_industry_next_button()
        self.click_scope_random_bus_activities()
        self.click_scope_business_activity_next_button()
        # more will go here after technology and system info is developed
        self.click_scope_technology_next_button()
