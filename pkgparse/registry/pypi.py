from pkgparse.registry.base import BaseRegistry


class PypiRegistry(BaseRegistry):

    def __init__(self):
        super().__init__()
        # TODO: Base URL is a bit redundant here. Consider just ignoring it
        self.base_url = "https://pypi.org/pypi/"
        self.pkg_route = "https://pypi.org/pypi/{0}/json"

    def parse_response(self, data):
        """
        This is the implementation of the parse_response method tailored to
        work with the PyPi registry.

        If no project url is provided for a package, it seems to default to
        the package page so we ignore that because it's just duplicate info
        that the user probably won't care about getting twice.

        :param data: dictionary
        :return: dictionary
        """
        response = {}

        response['name'] = data['info']['name']
        response['description'] = data['info']['summary']
        response['license'] = data['info']['license']
        if "https://pypi.org" not in data['info']['project_url']:
            response['source_repo'] = data['info']['project_url']
        response['homepage'] = data['info']['home_page']
        response['package_page'] = data['info']['package_url']
        version = data['info']['version']
        response['tarball'] = data["releases"][version][-1]['url']
        response['latest_version'] = version

        return response
