from pkgparse.registry.base import BaseRegistry


class PypiRegistry(BaseRegistry):

    def __init__(self):
        super().__init__()
        self.base_url = "https://pypi.org/pypi/"
        self.pkg_route = "https://pypi.org/pypi/{0}/json"
        self.package_page = "https://pypi.org/project/{0}/"

    def parse_response(self, data):
        response = {}

        response['name'] = data['info']['name']
        response['description'] = data['info']['summary']
        response['license'] = data['info']['license']
        if "https://pypi.org" not in data['info']['project_url']:
            response['source_repo'] = data['info']['project_url']
        response['homepage'] = data['info']['home_page']
        response['package_page'] = data['info']['package_url']
        version = data['info']['version']
        response['tarball'] = data["releases"][version][1]['url']
        response['latest_version'] = version

        return response
