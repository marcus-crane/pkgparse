import json
import unittest

import httpretty

from pkgparse import app
from tests import utils


class PypiRegistryIntegrationTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_query_pypi_details(self):
        """
        Verify that the search pypi endpoint returns the expected response.

        The response should be a status code 200 and send with the Content-Type
        of application/json.
        """
        package_string = json.dumps({
            "name": "pkgparse",
            "description": "A module for searching details about other "
                           "modules",
            "license": "MIT",
            "source_repo": "https://github.com/marcus-crane/pkgparse",
            "homepage": False,
            "package_page": "https://npmjs.com/package/pkgparse",
            "tarball": "https://registry.npmjs.org/pkgparse/-/"
                       "pkgparse-2.1.1.tgz",
            "latest_version": "2.1.1"
        }, sort_keys=True)

        data = utils.load_json_fixture('../fixtures/npm_pkg_latest.json')
        httpretty.register_uri(httpretty.GET,
                               "https://registry.npmjs.org/pkgparse/latest",
                               body=data)
        response = self.app.get('/npm/search/pkgparse')

        expected = json.loads(package_string)
        actual = json.loads(response.data)

        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
