from pkgparse.registry.base import BaseRegistry


class RubygemsRegistry(BaseRegistry):

    def __init__(self):
        super().__init__()
        self.base_url = "https://rubygems.org"
        self.pkg_route = "https://rubygems.org/api/v1/gems/{0}.json"

    def parse_response(self, data):
        """
        This is the implementation of the parse_response method tailored to
        work with the Rubygems registry.

        :param data: dictionary
        :return: dictionary
        """
        response = {}

        response['name'] = data['name']
        response['description'] = data['info']
        response['license'] = data['licenses'][0]
        response['source_repo'] = data['source_code_uri']
        if 'https://github.com' not in data['homepage_uri']:
            response['homepage'] = data['homepage_uri']
        response['package_page'] = data['project_uri']
        response['tarball'] = data['gem_uri']
        response['latest_version'] = data['version']

        return response
