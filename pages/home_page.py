from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    FORMS_MENU = (By.XPATH, "//h5[text()='Forms']")
    GOOGLE_ADD = (By.CSS_SELECTOR, "")
    ELEMENT = (By.XPATH, '//div[@class="card-body"]/h5[text()="Elements"]')

    def navigate_to_element(self):
        display = self.find_element(self.ELEMENT)
        self.scroll_to_element(self.ELEMENT)
        self.click_element(self.ELEMENT)
        print("inside",display)

    def navigate_to_forms(self):
        self.scroll_to_element(self.FORMS_MENU)
        self.click_element(self.FORMS_MENU)

    def handle_google_add(self):
        self.close_google_add(self.GOOGLE_ADD)

