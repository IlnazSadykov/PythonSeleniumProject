import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

        # Locators

    user_name = '//input[@id="user-name"]'
    password = '//input[@id="password"]'
    login_button = '//input[@id="login-button"]'
    main_word = '//span[@class="title"]'

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def input_username(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('input user name')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('input password')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')

    # Methods

    def authorization(self):
        with allure.step('Authorization'):
            Logger.add_start_step(method='authorization')
            self.driver_g.get(self.url)
            self.driver_g.maximize_window()
            self.input_username('standard_user')
            self.input_password('secret_sauce')
            self.click_login_button()
            self.assert_word(self.get_main_word(), 'PRODUCTS')
            Logger.add_end_step(url=self.driver_g.current_url, method='authorization')
