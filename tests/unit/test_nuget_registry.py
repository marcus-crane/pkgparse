import unittest

import httpretty

from pkgparse.registry.nuget import NugetRegistry
from tests import utils


class NugetRegistryUnitTestCase(unittest.TestCase):

    def test_fetch_nuget_pkg_details(self):
        """
        Test that given a valid NuGet package name, it can fetch the response,
        parse the specific NuGet JSON format and then do a generic repackaging
        of the information that it finds.
        """
        expected = {
            "name": "Newtonsoft.Json",
            "description": ("Json.NET is a popular high-performance "
                            "JSON framework for .NET"),
            "license": ("https://raw.github.com/JamesNK/Newtonsoft.Json"
                        "/master/LICENSE.md"),
            "source_repo": False,
            "homepage": "https://www.newtonsoft.com/json",
            "package_page": "https://www.nuget.org/packages/Newtonsoft.Json/",
            "tarball": "https://api.nuget.org/v3-flatcontainer/"
                        "newtonsoft.json/11.0.2/newtonsoft.json.11.0.2.nupkg",
            "latest_version": "11.0.2"
        }

        body = utils.load_json_fixture('nuget_pkg.json')
        httpretty.register_uri(httpretty.GET,
                               ("https://api.nuget.org/v3/registration3/"
                                "newtonsoft.json/index.json"),
                               body=body)
        registry = NugetRegistry()
        actual = registry.fetch_pkg_details('newtonsoft.json')

        assert actual == expected

    def test_parse_nuget_response(self):
        """
        Test that given a valid NuGet package response, it can be parsed
        properly by implementing a parser for the NuGet registry format.
        """
        registry = NugetRegistry()
        response = utils.load_json_fixture('nuget_pkg.json')
        actual = registry.parse_response(response)
        expected = {
            "name": "Newtonsoft.Json",
            "description": ("Json.NET is a popular high-performance "
                            "JSON framework for .NET"),
            "license": ("https://raw.github.com/JamesNK/Newtonsoft.Json"
                        "/master/LICENSE.md"),
            "homepage": "https://www.newtonsoft.com/json",
            "package_page": "https://www.nuget.org/packages/Newtonsoft.Json/",
            "tarball": "https://api.nuget.org/v3-flatcontainer/"
                        "newtonsoft.json/11.0.2/newtonsoft.json.11.0.2.nupkg",
            "latest_version": "11.0.2"
        }
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
