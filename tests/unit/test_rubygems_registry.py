import unittest

import httpretty

from pkgparse.registry.rubygems import RubygemsRegistry
from tests import utils


class RubygemsRegistryUnitTestCase(unittest.TestCase):

    def test_fetch_rubygems_pkg_details(self):
        """
        Test that given a valid Rubygems package name, it can fetch the response,
        parse the specific Rubygems JSON format and then do a generic repackaging
        of the information that it finds.
        """
        expected = ({
            "name": "jekyll",
            "description": "Jekyll is a simple, blog aware, static site generator.",
            "license": "MIT",
            "source_repo": "https://github.com/jekyll/jekyll",
            "homepage": False,
            "package_page": "https://rubygems.org/gems/jekyll",
            "tarball": "https://rubygems.org/gems/jekyll-3.7.3.gem",
            "latest_version": "3.7.3"
        })

        body = utils.load_json_string('../fixtures/rubygems_pkg.json')
        httpretty.register_uri(httpretty.GET,
                               "https://rubygems.org/api/v1/gems/jekyll.json",
                               body=body)
        registry = RubygemsRegistry()
        actual = registry.fetch_pkg_details('jekyll')

        assert actual == expected

    def test_parse_rubygems_response(self):
        """
        Test that given a valid Rubygems package response, it can be parsed
        properly by implementing a parser for the Rubygems registry format
        """
        registry = RubygemsRegistry()
        response = utils.load_json_fixture('../fixtures/rubygems_pkg.json')
        actual = registry.parse_response(response)
        expected = {
            "name": "jekyll",
            "description": "Jekyll is a simple, blog aware, static site generator.",
            "license": "MIT",
            "source_repo": "https://github.com/jekyll/jekyll",
            "package_page": "https://rubygems.org/gems/jekyll",
            "tarball": "https://rubygems.org/gems/jekyll-3.7.3.gem",
            "latest_version": "3.7.3"
        }

        assert actual == expected

if __name__ == "__main__":
    unittest.main()