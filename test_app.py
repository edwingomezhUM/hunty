import unittest
from flask import Flask
from flask_testing import TestCase

class MyTest(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_hello_world(self):
        response = self.client.get("/messages?")
        


        self.assertDictContainsSubset(response.data, b'Hello, World!')

if __name__ == '__main__':
    unittest.main()