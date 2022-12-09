"""
Because all the other built-in wait options are trash
"""

def clickable_by_link_text(driver, text, timeout=10):
    """
    Checks to see if a given element is clickable as a way to check if page is done loading.
    The timeout is to keep from infinite loop.
    """
    success = False
    count = 0
    while not success:
        if count > timeout:
            print("WARNING: loop has timed out or no results available")
            return False
        else:
            try:
                element = driver.find_element(By.LINK_TEXT, text)
                element.click()
                success = True
                return True
            except:
                count += 1
                time.sleep(1)


def clickable_by_id(driver, input_id, timeout=10):
    """
    Checks to see if a given element is clickable as a way to check if page is done loading.
    The timeout is to keep from infinite loop.
    """
    success = False
    count = 0
    while not success:
        if count > timeout:
            print("WARNING: loop has timed out or no results available")
            return False
        else:
            try:
                element = driver.find_element(By.ID, input_id)
                element.click()
                success = True
                return True
            except:
                count += 1
                time.sleep(1)


def clickable_by_xpath(driver, xpath, timeout=10):
    """
    Checks to see if a given element is clickable as a way to check if page is done loading.
    The timeout is to keep from infinite loop.
    """
    success = False
    count = 0
    while not success:
        if count > timeout:
            print("WARNING: loop has timed out or no results available")
            return False
        else:
            try:
                element = driver.find_element(By.XPATH, xpath)
                element.click()
                success = True
                return True
            except:
                count += 1
                time.sleep(1)
