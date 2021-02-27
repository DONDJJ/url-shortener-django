from django.test import Client
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from string import ascii_lowercase


class NewVisitorTest(unittest.TestCase):

    def setUp(self):  # особые методы
        self.browser = webdriver.Chrome()

    def tearDown(self):  # особые методы которые выполняются перед и после каждого теста
        self.browser.quit()

    def test_first_correct(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Create New URL', self.browser.title)  # входит ли первый аргумент во второй

    def test_anon_user_input(self):
        self.test_first_correct()
        form = self.browser.find_element_by_id('id_user_original_url')
        form.send_keys(
            'https://www.google.com/search?q=how+to+input+form+selenium&oq=how+to+input+form+selenium&aqs=chrome..69i57j0i22i30j0i390.15045j0j7&sourceid=chrome&ie=UTF-8')  # общепринятый способ ввода данных в input поля
        form.send_keys(Keys.ENTER)
        sleep(2)
        new_label = self.browser.find_element_by_id("prev_url_label")
        self.assertTrue("Готово:" in new_label.text and "http://127.0.0.1:8000" in new_label.text)

    def test_authed_user_input_and_save(self):
        self.test_first_correct()

        login_button = self.browser.find_element_by_id("login_button_layout")
        login_button.click()
        sleep(1)

        login_button = self.browser.find_element_by_id("enter_reg_page")
        login_button.click()
        sleep(1)

        login_form = self.browser.find_element_by_id("id_username")
        password_form = self.browser.find_element_by_id("id_password")
        login_form.send_keys('admin')
        password_form.send_keys('admin')
        password_form.send_keys(Keys.ENTER)
        sleep(3)

        random_url = 'https://www.' + "".join([random.choice(ascii_lowercase) for x in range(10)]) + ".com/"

        profile_button = self.browser.find_element_by_id("profile_link_layout")
        profile_button.click()
        sleep(2)

        login_button = self.browser.find_element_by_id("url_short_link_layout")
        login_button.click()
        sleep(1)

        form = self.browser.find_element_by_id('id_user_original_url')
        form.send_keys(random_url)
        form.send_keys(Keys.ENTER)
        sleep(2)
        new_label_txt = self.browser.find_element_by_id("prev_url_layout").text

        profile_button = self.browser.find_element_by_id("profile_link_layout")
        profile_button.click()
        sleep(2)
        elem_0 = self.browser.find_element_by_id("url_profile_item")
        old_0 = self.browser.find_element_by_id("old_url_0")

        self.assertTrue(random_url in old_0.text and new_label_txt in elem_0.text, "Новый элемент не появился в списке!")
        sleep(2)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
