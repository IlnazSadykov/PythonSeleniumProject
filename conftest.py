import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def set_up():
    print('\nStart test\n')
    yield
    print('\nFinish test\n')


@pytest.fixture(scope='module')
def set_group():
    print('Enter system')
    yield
    print('Exit system\n')