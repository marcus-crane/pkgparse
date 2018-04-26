import json
import unittest


from pkgparse import app


class AppIntegrationTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_list_endpoints(self):
        """
        Test that the endpoints route lists all available endpoints
        """
        routes = [
            '/',
            '/npm/<name>',
            '/nuget/<name>',
            '/ping',
            '/ping/npm',
            '/ping/nuget',
            '/ping/pypi',
            '/ping/rubygems',
            '/pypi/<name>',
            '/rubygems/<name>',
        ]
        expected = {}
        for num, route in enumerate(routes):
            expected[str(num)] = route

        response = self.app.get('/')
        assert json.loads(response.data) == expected

    def test_ping(self):
        """Test that the pkgparse server is alive and well."""
        response = self.app.get('/ping')

        assert response.status_code == 200
        assert response.data == b"pong"


if __name__ == "__main__":
    unittest.main()
