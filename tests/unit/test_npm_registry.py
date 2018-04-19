import unittest

import httpretty

from pkgparse.registry.npm import NPMRegistry
from tests import utils


class NPMRegistryUnitTestCase(unittest.TestCase):

    def test_fetch_npm_pkg_details(self):
        """
        Test that given a valid NPM package name, it can fetch the response,
        parse the specific NPM JSON format and then do a generic repackaging
        of the information that it finds.
        """
        expected = {
            "name": "pkgparse",
            "description": "A module for searching details about other modules",
            "license": "MIT",
            "source_repo": "https://github.com/marcus-crane/pkgparse",
            "homepage": False,
            "package_page": "https://npmjs.com/package/pkgparse",
            "tarball": "https://registry.npmjs.org/pkgparse/-/pkgparse-2.1.1.tgz",
            "latest_version": "2.1.1"
        }

        body = utils.load_json_fixture('npm_pkg_latest.json')
        httpretty.register_uri(httpretty.GET,
                               "https://registry.npmjs.org/pkgparse/latest",
                               body=body)
        registry = NPMRegistry()
        actual = registry.fetch_pkg_details('pkgparse')

        assert actual == expected

    def test_parse_npm_response(self):
        """
        Test that given a valid NPM package response, it can be parsed
        properly by implementing a parser for the NPM registry format.
        """
        registry = NPMRegistry()
        response = utils.load_json_fixture('npm_pkg_latest.json')
        actual = registry.parse_response(response)
        expected = {
            "name": "pkgparse",
            "description": "A module for searching details about other modules",
            "license": "MIT",
            "source_repo": "https://github.com/marcus-crane/pkgparse",
            "package_page": "https://npmjs.com/package/pkgparse",
            "tarball": "https://registry.npmjs.org/pkgparse/-/pkgparse-2.1.1.tgz",
            "latest_version": "2.1.1"
        }
        assert actual == expected


if __name__ == "__main__":
    unittest.main()