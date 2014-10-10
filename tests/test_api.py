import unittest
import urlparse
import requests


SERVER_URL = 'http://localhost:5000/'
ECHO_API_URL = urlparse.urljoin(SERVER_URL, '/api/echo')


class APITestCase(unittest.TestCase):
    def test_success(self):
        name = 'Python Day'
        response = requests.post(ECHO_API_URL, data={'name': name})
        data = response.json()
        self.assertIn('response', data)
        self.assertEqual(data['response'], name)

    def test_failure(self):
        response = requests.post(ECHO_API_URL, data={'name': ''})
        data = response.json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], u'Please provide a name')
