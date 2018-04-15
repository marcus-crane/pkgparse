from pkgparse.registry.base import BaseRegistry


class NPMRegistry(BaseRegistry):

    def __init__(self):
        super().__init__()
        self.base_url = "https://registry.npmjs.com"
        self.pkg_route = "https://registry.npmjs.com/{0}/latest"
        self.package_page = "https://npmjs.com/package/{0}"

    def parse_response(self, data):
        response = {}

        response['name'] = data['name']
        response['description'] = data['description']
        response['license'] = data['license']
        response['source_repo'] = data['repository']['url'][4:-4]
        if 'https://github.com' not in data['homepage']:
            response['homepage'] = data['homepage']
        response['package_page'] = self.package_page.format(data['name'])
        response['tarball'] = data['dist']['tarball']
        response['latest_version'] = data['version']

        return response
