from selenium.webdriver.chrome.options import Options
import secure
import sys
import os


if sys.platform.startswith('win32'):
    path_to_webdriver = (os.path.dirname(os.path.realpath(__file__)) + 
                        "\Resources\windows_chromedriver\chromedriver.exe")
elif sys.platform.startswith('linux'):
    path_to_webdriver = (os.path.dirname(os.path.realpath(__file__)) + 
                        "/Resources/linux_chromedriver/chromedriver")
elif sys.platform.startswith('darwin'):
    path_to_webdriver = (os.path.dirname(os.path.realpath(__file__)) + 
                        "/Resources/mac_chromedriver/chromedriver")

# replace secure.ubold_username and secure.ubold_password with the 
# username and password that you created.
ubold_username = secure.ubold_username
ubold_password = secure.ubold_password
ubold_email    = secure.ubold_email

# OPTIONS FOR THE DRIVER
options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
options.add_argument("--start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])