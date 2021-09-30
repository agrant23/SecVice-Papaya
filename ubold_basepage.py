from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import settings

class UboldBasePage():
    
    options = Options()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(settings.path_to_webdriver, options=options)
    actions = ActionChains(driver)