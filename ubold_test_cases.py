import unittest
from pages.ubold_account_create_page import UboldAccountCreatePage
from pages.ubold_account_page import UboldAccountPage
from pages.ubold_homepage import UboldHomePage
from pages.ubold_signinpage import UboldSignInPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import settings
import time


class HomePageSetup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            settings.path_to_webdriver, options=settings.options)

    def tearDown(self):
        self.driver.quit()


class AccountCreation(HomePageSetup):

    def test_account_creation(self):
        """
        Confirm the user can enter his/her information and be directed to the
        login page.

        acceptance criteria
        --------------------
        -Given a user inputs valid information on the account creation page
         When the user clicks on the create account button
         Then the login page will open.
        """
        UboldHomePage(self.driver).click_sign_up_link()
        UboldAccountCreatePage(self.driver).account_create()
        self.assertIn('login', self.driver.current_url)

    def test_user_account_page(self):
        """
        Confirm the user can enter his/her login credential and be directed to
        his/her account page. This is done by testing if the user's first name
        appears in the navigation bar of the account page.

        acceptance criteria
        --------------------
        -Given a user inputs valid login credentials
         When the user clicks on the login button
         Then the account page will open with his/her first name in the
         navigation bar.
        """
        ubold_signin_page = UboldSignInPage(self.driver, True)
        ubold_signin_page.input_username_field(settings.ubold_username)
        ubold_signin_page.input_password_field(settings.ubold_password)
        ubold_signin_page.click_login_button()
        self.assertIn("Tony", UboldAccountPage(self.driver).first_name().text)


class Scope(HomePageSetup):
    def setUp(self):
        """
        To ensure the test_scope_object_creation is in the same state this
        setup method requires to delete all scope objects and then to log out
        and back in.
        """
        super().setUp()
        self.ubold_account_page = UboldAccountPage(self.driver)

        UboldSignInPage(self.driver, True).login()
        self.ubold_account_page.delete_all_scope_objects()
        self.ubold_account_page.logout_account()
        UboldHomePage(self.driver, False).click_sign_in_link()
        UboldSignInPage(self.driver).login()

    def test_scope_object_creation(self):
        """
        Confirm the scope object is created successfully.

        acceptance criteria
        -------------------
        Given the user inputs valid information to create a scope object
        When the user creates a scope object and navigates to the organization
        scope list
        Then the new scope object will appear on the scope list
        """
        ubold_account_page = self.ubold_account_page
        ubold_account_page.create_scope_object()
        ubold_account_page.click_org_scope_link()
        ubold_account_page.click_view_all_scopes_link()
        self.assertEqual(ubold_account_page.created_scope_object_name(),
                         ubold_account_page.scope_object_name)


class SignIn(HomePageSetup):

    def test_sign_in_link(self):
        """
        Confirm the log in internal link is correct.

        acceptance criteria
        --------------------
        -After clicking the sign in link, the URL has changed to the login page.
        """
        UboldHomePage(self.driver).click_sign_in_link()
        self.assertIn('login', self.driver.current_url)

    def test_ubold_logo_sign_in_link(self):
        """
        Confirm the Ubold logo internal link is correct.

        acceptance criteria
        --------------------
        -After clicking the Ubold logo link, the URL has changed to the login
         page.
        """
        UboldHomePage(self.driver).click_ubold_logo_link()
        self.assertIn('login', self.driver.current_url)


if __name__ == "__main__":
    unittest.main()
