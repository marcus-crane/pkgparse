import json
import unittest

import httpretty

from pkgparse import app
from tests import utils


class NugetRegistryIntegrationTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_query_nuget_details(self):
        """
        Verify that the search nuget endpoint returns the expected response.

        The response should be a status code 200 and send with the Content-Type
        of application/json.
        """
        package_string = json.dumps({
            "name": "Newtonsoft.Json",
            "description": ("Json.NET is a popular high-performance "
                            "JSON framework for .NET"),
            "license": ("https://raw.github.com/JamesNK/Newtonsoft.Json"
                        "/master/LICENSE.md"),
            "source_repo": False,
            "homepage": "https://www.newtonsoft.com/json",
            "package_page": "https://www.nuget.org/packages/Newtonsoft.Json/",
            "tarball": ("https://api.nuget.org/v3-flatcontainer/"
                        "newtonsoft.json/11.0.2/newtonsoft.json.11.0.2.nupkg"),
            "latest_version": "11.0.2"
        }, sort_keys=True)

        data = utils.load_json_fixture('../fixtures/nuget_pkg.json')
        httpretty.register_uri(httpretty.GET,
                               ("https://api.nuget.org/v3/registration3/"
                                "newtonsoft.json/index.json"),
                               body=data)
        response = self.app.get('/nuget/search/newtonsoft.json')

        expected = json.loads(package_string)
        actual = json.loads(response.data)

        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
