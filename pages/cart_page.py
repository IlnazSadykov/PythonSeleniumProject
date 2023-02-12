import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

        # Locators

    checkout_button = '//*[@id="checkout"]'

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Click checkout_button')

    # Methods

    def product_confirmation(self):
        with allure.step('product_confirmation'):
            Logger.add_start_step(method='product_confirmation')
            self.get_current_url()
            self.click_checkout_button()
            Logger.add_end_step(url=self.driver_g.current_url, method='product_confirmation')