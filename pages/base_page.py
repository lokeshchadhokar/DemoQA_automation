from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def enter_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(locator).perform()

    def close_google_add(self, locator):
        try:
            ad_close_button = WebDriverWait(self.driver,5).until(
                EC.element_to_be_clickable(locator)
            )
            ad_close_button.click()
            print("goodle ad closed")

        except Exception as e:
            print("No add found",str(e))