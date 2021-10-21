from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

def wait_for_scroll_to_click(driver, locator):
    """
    A method to wait to scroll to an element and click on it. 
    
    Parameters
    ----------
    locator : a tuple used to find the element to be clicked.

    Note
    ----
    This can be used for any wait to scroll to an element and click, however
    other waits and actions can be used to accomplish this. This method is
    created because a specific situation required this wait to scroll.
    """
    driver.execute_script(
                               "window.scrollTo(0,document.body.scrollHeight)")
    retry = 0
    while retry < 5:
        try:
            wait(driver, 2).until(
                EC.visibility_of_element_located(locator))
            driver.find_element(*locator).click()
            break
        except:
            StaleElementReferenceException
            retry += 1