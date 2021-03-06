import json
import unittest

import httpretty

from pkgparse.registry.base import BaseRegistry


class BaseRegistryUnitTestCase(unittest.TestCase):

    @httpretty.activate
    def test_make_request(self):
        """
        A generic helper function that makes a GET request and appends
        the correct User-Agent which is specified in the settings file.
        """
        httpretty.register_uri(httpretty.GET, "https://test.net",
                               body="hi", status=200)
        registry = BaseRegistry()
        r = registry.make_request('https://test.net')

        assert r.status_code == 200
        assert r.text == "hi"

    @httpretty.activate
    def test_ping_registry_success(self):
        """Pinging a valid registry should return True to show it's online"""
        httpretty.register_uri(httpretty.GET, "https://registry.npmjs.com/"
                                              "tiny-tarball/latest",
                               status=200)
        registry = BaseRegistry()
        registry.pkg_route = "https://registry.npmjs.com/{0}/latest"
        registry.test_pkg = "tiny-tarball"

        assert registry.ping()['status'] is 'online'

    @httpretty.activate
    def test_ping_registry_failure(self):
        """Pinging an invalid registry should return False to show it's down"""
        httpretty.register_uri(httpretty.GET, "https://registry.fake/"
                                              "hotdog-farmer",
                               body="Not Found",
                               status=404)
        registry = BaseRegistry()
        registry.pkg_route = "https://registry.fake/{0}"
        registry.test_pkg = "hotdog-farmer"

        assert registry.ping()['status'] is 'offline'

    @httpretty.activate
    def test_fetch_pkg_details(self):
        """
        Trying to use the BaseRegistry class directly should fail.
        Each inheriting registry class needs to implement its own package
        parsing function as responses are all wildly different.
        """
        body = {
            "name": "pkgparse",
            "description": "A module for searching details about other "
                           "modules",
            "license": "MIT",
            "source_repo": "https://github.com/marcus-crane/pkgparse",
            "homepage": "",
            "package_page": "https://npmjs.com/package/pkgparse",
            "tarball": "https://registry.npmjs.org/pkgparse/-"
                       "/pkgparse-2.1.1.tgz",
            "latest_version": "2.1.1"
        }
        httpretty.register_uri(httpretty.GET,
                               "https://registry.npmjs.org/pkgparse/latest",
                               body=json.dumps(body))
        registry = BaseRegistry()
        registry.pkg_route = "https://registry.npmjs.org/{0}/latest"

        with self.assertRaises(NotImplementedError):
            registry.fetch_pkg_details('pkgparse')

    def test_build_api_response(self):
        """
        The build_api_response function should have no idea about what
        repo class is implementing it.

        All it knows how to do is check if a key exists in the response
        dictionary and adds it to the response object. As a result,
        it will only need testing once which is neat.

        If the key doesn't exist, it just returns a zero value eg; False
        """
        registry = BaseRegistry()

        dummy_parsed_response = {
            'name': 'cool_package',
            'description': 'A neat package',
            'license': 'MIT',
            'latest_version': '2.0.0'
        }

        actual = registry.build_api_response(dummy_parsed_response)

        expected = {
            'name': 'cool_package',
            'description': 'A neat package',
            'license': 'MIT',
            'source_repo': "",
            'homepage': "",
            'package_page': "",
            'tarball': "",
            'latest_version': '2.0.0'
        }

        assert actual == expected


if __name__ == "__main__":
    unittest.main()
