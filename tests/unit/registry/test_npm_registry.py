import unittest


from pkgparse.registry.npm import NPMRegistry
from tests import utils


class NPMRegistryTestCase(unittest.TestCase):

    def test_parse_npm_package_latest_version_only(self):
        """Test that given a valid NPM package response, it can be parsed"""
        registry = NPMRegistry()
        response = utils.load_json_fixture('../fixtures/npm_package_latest.json')
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