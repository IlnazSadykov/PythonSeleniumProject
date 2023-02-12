import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


# @pytest.mark.run(order=3)
@allure.description('Test but product 1')
def test_select_product_1(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    g = Service('D:/PycharmProjects/chromedriver/chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print('Start test 1')

    login = Login_page(driver_g)
    login.authorization()

    mp = Main_page(driver_g)
    mp.select_product_1()

    cp = Cart_page(driver_g)
    cp.click_checkout_button()

    cip = Client_information_page(driver_g)
    cip.input_information()

    p = Payment_page(driver_g)
    p.click_finish_button()

    f = Finish_page(driver_g)
    f.finish()

    print('Finish test 1')
    time.sleep(2)
    driver_g.quit()


@pytest.mark.run(order=1)
def test_select_product_2():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    g = Service('D:/PycharmProjects/chromedriver/chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print('Start test 2')

    login = Login_page(driver_g)
    login.authorization()

    mp = Main_page(driver_g)
    mp.select_product_2()

    cp = Cart_page(driver_g)
    cp.click_checkout_button()

    print('Finish test 2')
    time.sleep(2)
    driver_g.quit()


# @pytest.mark.run(order=2)
def test_select_product_3():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    g = Service('D:/PycharmProjects/chromedriver/chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print('Start test 3')

    login = Login_page(driver_g)
    login.authorization()

    mp = Main_page(driver_g)
    mp.select_product_3()

    cp = Cart_page(driver_g)
    cp.click_checkout_button()

    print('Finish test 3')
    time.sleep(2)
    driver_g.quit()