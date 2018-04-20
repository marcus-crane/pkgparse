import json
import unittest

import httpretty

from pkgparse import app
from tests import utils


class PypiRegistryIntegrationTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @httpretty.activate
    def test_query_pypi_details(self):
        """
        Verify that the search pypi endpoint returns the expected response.

        The response should be a status code 200 and send with the Content-Type
        of application/json.
        """
        package_string = json.dumps({
            "name": "requests",
            "description": "Python HTTP for Humans.",
            "license": "Apache 2.0",
            "source_repo": False,
            "homepage": "http://python-requests.org",
            "package_page": "https://pypi.org/project/requests/",
            "tarball": "https://files.pythonhosted.org/packages/b0/e1/"
                        "eab4fc3752e3d240468a8c0b284607899d2fbfb236a56b7377a3"
                        "29aa8d09/requests-2.18.4.tar.gz",
            "latest_version": "2.18.4"
        }, sort_keys=True)

        data = utils.load_json_fixture('pypi_pkg.json')
        httpretty.register_uri(httpretty.GET,
                               "https://pypi.org/pypi/requests/json",
                               body=json.dumps(data))
        response = self.app.get('/pypi/search/requests')

        expected = json.loads(package_string)
        actual = json.loads(response.data)

        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
