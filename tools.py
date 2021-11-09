from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException
from random import choice
import string


def generate_random_num(min_range, max_range, excluded_nums=[None]):
    """
    The range is inclusive and this method can exclude numbers.
    """
    return choice([num for num in range(min_range, max_range+1)
                  if num not in excluded_nums])


def generate_random_string(
                       str_length, letter=True, number=True, punctuation=True):
    """
    A method that generates a random string of a specified length. The boolean
    parameters can specify the exclusion of character types

    Parameters
    ----------
    str_length: the specified length of the string
    letter Boolean: By default, letters are included in the string,
                    can be excluded
    digit Boolean: By default, numbers/digits are included in the string,
                   can be excluded
    punctuation Boolean: By default, punctuations are included in the string,
                         can be excluded
    """
    letters = ''
    numbers = ''
    punctuations = ''
    characters = ''
    if letter and number and punctuation:
        characters = string.ascii_letters + string.digits + string.punctuation
    elif letter and number:
        characters = string.ascii_letters + string.digits
    elif letter and punctuation:
        characters = string.ascii_letters + string.punctuation
    elif number and punctuation:
        characters = string.digits + string.punctuation
    elif letter:
        characters = string.ascii_letters
    elif number:
        characters = string.digits
    elif punctuation:
        characters = string.punctuation

    return ''.join(choice(characters) for i in range(str_length))


def random_num_clicks_random_elements(driver, element_array_locator):
    """
    A method to perform a random number of clicks on an array of elements where
    the elements are chosen at random.

    Parameters
    ----------
    element_array_locator: a tuple used to find the array of elements that will
                           be clicked.

    Notes
    -----
    There is a small chance of an infinite loop occurring. I will come back to
    fix this.

    Internal Variables
    ------------------
    random_num_clicks: random number determining how many clicks are performed
                       on the element array.
    random_element_num: the random element array index that.
    clicked_element_nums: list of the element's indices that have been clicked
    skipped_click_num: the number of times a click was skipped due to that
                       element having already been clicked.
    """
    wait(driver, 15).until(
        EC.visibility_of_all_elements_located(element_array_locator))
    element_array = driver.find_elements(*element_array_locator)
    total_num_elements = len(element_array)
    random_num_clicks = generate_random_num(1, total_num_elements)
    clicked_element_nums = []
    skipped_click_num = 0
    i = 0

    while i + skipped_click_num < random_num_clicks + skipped_click_num:
        random_element_num = generate_random_num(0, total_num_elements-1)
        if random_element_num in clicked_element_nums:
            skipped_click_num += 1
        while(random_element_num not in clicked_element_nums):
            random_element = element_array[random_element_num]
            clicked_element_nums.append(random_element_num)
            wait(driver, 15).until(EC.visibility_of(random_element))
            random_element.click()
            i += 1
            break


# EXPECTED CONDITION

def input_value_is_present(locator):
    """
    An expected condition to check that some input value is present in a field.

    Parameters
    ----------
    locator: a tuple used to find the field
    """
    def _predicate(driver):

        input_value = driver.find_element(*locator).get_attribute('value')
        if len(input_value) != 0:
            return True
        else:
            return False

    return _predicate


def wait_for_scroll_to_click(driver, locator):
    """
    A method to wait to scroll to an element and click on it.

    Parameters
    ----------
    locator: a tuple used to find the element to be clicked.

    Note
    ----
    This can be used for any wait to scroll to an element and click, however
    other waits and actions can be used to accomplish this. This method is
    created because a specific situation required the visibility wait within
    the loop to successfully wait and click one element. This is a special case.
    """
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.execute_script("window.scrollBy(0,3000)")
    retry = 0
    while retry < 8:
        try:
            wait(driver, 3).until(EC.element_to_be_clickable(locator))
            driver.find_element(*locator).click()
            break
        except ElementClickInterceptedException:
            #driver.execute_script("window.scrollBy(0,3000)")
            retry += 1


# UNUSED METHODS

def check_element_exists(driver, locator):
    """
    A method to check if an element exists.

    Parameters
    ----------
    locator: a tuple used to find the element that exists or not.
    """
    try:
        driver.find_element(*locator)
    except NoSuchElementException:
        return False
    return True
