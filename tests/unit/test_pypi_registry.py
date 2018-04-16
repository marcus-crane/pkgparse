import unittest
import unittest

import httpretty

from pkgparse.registry.pypi import PypiRegistry
from tests import utils


class PypiRegistryUnitTestCase(unittest.TestCase):

    def test_fetch_pypi_pkg_details(self):
        """
        Test that given a valid PyPi package name, it can fetch the response,
        parse the specific PyPi JSON format and then do a generic repackaging
        of the information that it finds.
        """
        expected = ({
            "name": "requests",
            "description": "Python HTTP for Humans.",
            "license": "Apache 2.0",
            "source_repo": False,
            "homepage": "http://python-requests.org",
            "package_page": "https://pypi.org/project/requests/",
            "tarball": "https://files.pythonhosted.org/packages/b0/e1/eab4fc3752e3d240468a8c0b284607899d2fbfb236a56b7377a329aa8d09/requests-2.18.4.tar.gz",
            "latest_version": "2.18.4"
        })

        body = utils.load_json_string('../fixtures/pypi_pkg.json')
        httpretty.register_uri(httpretty.GET,
                               "https://pypi.org/pypi/requests/json",
                               body=body)
        registry = PypiRegistry()
        actual = registry.fetch_pkg_details('requests')

        assert actual == expected

    def test_parse_pypi_response(self):
        """
        Test that given a valid PyPi package response, it can be parsed
        properly by implementing a parser for the PyPi registry format
        """
        registry = PypiRegistry()
        response = utils.load_json_fixture('../fixtures/pypi_pkg.json')
        actual = registry.parse_response(response)
        expected = {
            "name": "requests",
            "description": "Python HTTP for Humans.",
            "license": "Apache 2.0",
            "homepage": "http://python-requests.org",
            "package_page": "https://pypi.org/project/requests/",
            "tarball": "https://files.pythonhosted.org/packages/b0/e1/eab4fc3752e3d240468a8c0b284607899d2fbfb236a56b7377a329aa8d09/requests-2.18.4.tar.gz",
            "latest_version": "2.18.4"
        }

        assert actual == expected

if __name__ == "__main__":
    unittest.main()