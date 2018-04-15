import unittest

import httpretty

from pkgparse.registry.base import BaseRegistry

class BaseRegistryTestCase(unittest.TestCase):

    @httpretty.activate
    def test_ping_registry_success(self):
        httpretty.register_uri(httpretty.GET, "https://registry.npmjs.org")
        registry = BaseRegistry()
        registry.base_url = "https://registry.npmjs.org"

        assert registry.ping() is True

    @httpretty.activate
    def test_ping_registry_failure(self):
        httpretty.register_uri(httpretty.GET, "https://registry.fake",
                               body="Not Found",
                               status=404)
        registry = BaseRegistry()
        registry.base_url = "https://registry.fake"

        assert registry.ping() is False

if __name__ == "__main__":
    unittest.main()