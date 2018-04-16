from pkgparse.registry.base import BaseRegistry


class NPMRegistry(BaseRegistry):

    def __init__(self):
        super().__init__()
        self.pkg_route = "https://registry.npmjs.com/{0}/latest"
        self.test_pkg = "tiny-tarball"
        self.pkg_page = "https://npmjs.com/package/{0}"

    def parse_response(self, data):
        """
        This is the implementation of the parse_response method tailored to
        work with the NPM registry.

        If no homepage is provided for a package, it seems to default to the
        repository url so we ignore that because it's just duplicate info
        that the user probably won't care about getting twice.

        :param data: dictionary
        :return: dictionary
        """
        response = {}

        response['name'] = data['name']
        response['description'] = data['description']
        response['license'] = data['license']
        response['source_repo'] = data['repository']['url'][4:-4]
        if 'https://github.com' not in data['homepage']:
            response['homepage'] = data['homepage']
        response['package_page'] = self.pkg_page.format(data['name'])
        response['tarball'] = data['dist']['tarball']
        response['latest_version'] = data['version']

        return response
