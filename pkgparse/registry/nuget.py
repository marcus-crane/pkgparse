from pkgparse.registry.base import BaseRegistry


class NugetRegistry(BaseRegistry):

    def __init__(self):
        super().__init__()
        self.pkg_route = ("https://api.nuget.org/v3/registration3/"
                          "{0}/index.json")
        self.test_pkg = "newtonsoft.json"
        self.pkg_page = "https://www.nuget.org/packages/{0}/"

    def parse_response(self, data):
        """
        This is the implementation of the parse_response method tailored to
        work with the NuGet registry.

        :param data: dictionary
        :return: dictionary
        """
        response = {}

        entry = data['items'][0]['items'][-1]['catalogEntry']
        response['name'] = entry['id']
        response['description'] = entry['description']
        response['license'] = entry['licenseUrl']
        if 'https://github.com' not in entry['projectUrl']:
            response['homepage'] = entry['projectUrl']
        response['package_page'] = self.pkg_page.format(entry['id'])
        response['tarball'] = entry['packageContent']
        response['latest_version'] = entry['version']

        return response
