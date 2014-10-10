import unittest
from splinter import Browser

SERVER_URL = 'http://localhost:5000/'


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()

    def tearDown(self):
        self.browser.quit()

    def test_success(self):
        name = 'Python Day'
        self.browser.visit(SERVER_URL)
        self.browser.fill('name', name)
        self.browser.find_by_tag('button').click()
        if not self.browser.is_text_present(u'Welcome {0}'.format(name)):
            self.fail('Unable to find success message')

    def test_failure(self):
        self.browser.visit(SERVER_URL)
        self.browser.fill('name', '')
        self.browser.find_by_tag('button').click()
        if not self.browser.is_text_present(u'Please provide a name'):
            self.fail('Unable to find failure message')
