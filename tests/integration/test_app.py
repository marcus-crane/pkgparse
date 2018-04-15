import unittest

from pkgparse import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        assert b"Hello, World!" == response.data

    def test_ping(self):
        response = self.app.get('/ping')
        assert b"pong" == response.data


if __name__ == "__main__":
    unittest.main()