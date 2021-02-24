from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):  # особые методы
        self.browser = webdriver.Chrome()

    def tearDown(self):  # особые методы которые выполняются перед и после каждого теста
        self.browser.quit()

    def test_first_correct(self):
        self.browser.get('http://127.0.0.1:8000/') 
        self.assertIn('Create New URL', self.browser.title)  # входит ли первый аргумент во второй


if __name__ == '__main__':
    unittest.main(warnings='ignore')
