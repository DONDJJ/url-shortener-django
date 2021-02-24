from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from time import sleep

class NewVisitorTest(unittest.TestCase):

    def setUp(self):  # особые методы
        self.browser = webdriver.Chrome()

    def tearDown(self):  # особые методы которые выполняются перед и после каждого теста
        self.browser.quit()

    def test_first_correct(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Create New URL', self.browser.title)  # входит ли первый аргумент во второй

    def test_input(self):
        self.test_first_correct()
        form = self.browser.find_element_by_id('id_user_original_url')
        form.send_keys(
            'https://www.google.com/search?q=how+to+input+form+selenium&oq=how+to+input+form+selenium&aqs=chrome..69i57j0i22i30j0i390.15045j0j7&sourceid=chrome&ie=UTF-8')  # общепринятый способ ввода данных в input поля
        form.send_keys(Keys.ENTER)
        sleep(2)
        new_label = self.browser.find_element_by_id("prev_url_label")
        self.assertTrue("Готово:" in new_label.text and "http://127.0.0.1:8000" in new_label.text)



if __name__ == '__main__':
    unittest.main(warnings='ignore')
