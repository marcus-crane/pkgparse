import json
import unittest

import httpretty

from pkgparse import server
from tests import utils


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = server.app.test_client()

    def test_index(self):
        response = self.app.get('/')
        assert b"Hello, World!" == response.data

    def test_ping(self):
        response = self.app.get('/ping')
        assert b"pong" == response.data

    def test_query_npm_details(self):
        package_string = json.dumps({
            "name": "pkgparse",
            "description": "A module for searching details about other modules",
            "license": "MIT",
            "source_repo": "https://github.com/marcus-crane/pkgparse",
            "homepage": False,
            "package_page": "https://npmjs.com/package/pkgparse",
            "tarball": "https://registry.npmjs.org/pkgparse/-/pkgparse-2.1.1.tgz",
            "latest_version": "2.1.1"
        }, sort_keys=True)

        data = utils.load_json_string('../fixtures/npm_pkg_latest.json')
        httpretty.register_uri(httpretty.GET,
                               "https://registry.npmjs.org/pkgparse/latest",
                               body=data)
        response = self.app.get('/npm/search/pkgparse')

        expected = json.loads(package_string)
        actual = json.loads(response.data)


        assert expected == actual


if __name__ == "__main__":
    unittest.main()