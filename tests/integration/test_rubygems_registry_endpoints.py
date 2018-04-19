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
        Verify that the search rubygems endpoint returns the expected response.

        The response should be a status code 200 and send with the Content-Type
        of application/json.
        """
        package_string = json.dumps({
            "name": "jekyll",
            "description": "Jekyll is a simple, blog aware, static site "
                           "generator.",
            "license": "MIT",
            "source_repo": "https://github.com/jekyll/jekyll",
            "homepage": False,
            "package_page": "https://rubygems.org/gems/jekyll",
            "tarball": "https://rubygems.org/gems/jekyll-3.7.3.gem",
            "latest_version": "3.7.3"
        }, sort_keys=True)

        data = utils.load_json_fixture('../fixtures/rubygems_pkg.json')
        httpretty.register_uri(httpretty.GET,
                               "https://rubygems.org/api/v1/gems/jekyll.json",
                               body=data)
        response = self.app.get('/rubygems/search/jekyll')

        expected = json.loads(package_string)
        actual = json.loads(response.data)

        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
