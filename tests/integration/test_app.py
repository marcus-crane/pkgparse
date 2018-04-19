import unittest


from pkgparse import app


class AppIntegrationTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        """
        Test that the root of the server returns something!
        Basically a placeholder for a future homepage
        """
        response = self.app.get('/')
        assert response.data == b"Hello, World!"

    def test_ping(self):
        """Test that the pkgparse server is alive and well."""
        response = self.app.get('/ping')

        assert response.status_code == 200
        assert response.data == b"pong"


if __name__ == "__main__":
    unittest.main()
