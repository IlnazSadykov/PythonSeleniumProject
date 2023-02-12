import datetime
import time


class Base():

    def __init__(self, driver_g):
        self.driver_g = driver_g


    '''Method get current URL'''

    def get_current_url(self):
        get_url = self.driver_g.current_url
        print('Current url' + get_url)

    '''Method assert word'''

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    '''Method screenshot'''

    def get_screenshot(self):
        time.sleep(2)
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver_g.save_screenshot('D:\\PycharmProjects\\pythonSeleniumProject\\screen\\' + name_screenshot)
        print('Screenshot' + name_screenshot)

    '''Method assert URL'''

    def assert_url(self, result):
        time.sleep(1)
        get_url = self.driver_g.current_url
        assert get_url == result
        print('Good value URL')
