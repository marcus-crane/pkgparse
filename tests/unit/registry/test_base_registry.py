import json
import unittest

import httpretty

from pkgparse.registry.base import BaseRegistry


class BaseRegistryTestCase(unittest.TestCase):

    @httpretty.activate
    def test_make_request(self):
        """
        A generic helper functinon that makes a GET request and appends
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
        httpretty.register_uri(httpretty.GET, "https://registry.npmjs.org",
                               status=200)
        registry = BaseRegistry()
        registry.root = "https://registry.npmjs.org"

        assert registry.ping() is True

    @httpretty.activate
    def test_ping_registry_failure(self):
        """Pinging an invalid registry should return False to show it's down"""
        httpretty.register_uri(httpretty.GET, "https://registry.fake",
                               body="Not Found",
                               status=404)
        registry = BaseRegistry()
        registry.root = "https://registry.fake"

        assert registry.ping() is False

    def test_fetch_pkg_details(self):
        """
        Trying to use the BaseRegistry class directly should fail.
        Each inheriting registry class needs to implement its own package
        parsing function as responses are all wildly different.
        """
        registry = BaseRegistry()
        registry.pkg_route = "http://registry.npmjs.org/{0}"

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

        expected = json.dumps({
            'name': 'cool_package',
            'description': 'A neat package',
            'license': 'MIT',
            'source_repo': False,
            'homepage': False,
            'package_page': False,
            'tarball': False,
            'latest_version': '2.0.0'
        })

        assert actual == expected


if __name__ == "__main__":
    unittest.main()
