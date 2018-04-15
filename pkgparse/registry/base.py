import json
import requests
import sys

from pkgparse import settings


class BaseRegistry:

    def __init__(self):
        self.root = None
        self.pkg_route = None
        self.package_page = None

    def make_request(self, url, headers={}):
        headers.update({ "User-Agent": settings.USER_AGENT })
        return requests.get(url, headers=headers)

    def ping(self):
        try:
            r = self.make_request(self.root)
            if r.status_code is 200:
                return True
            return False
        except requests.exceptions.Timeout:
            print("Dang, I timed out")
        except requests.exceptions.TooManyRedirects:
            print("Whoa, I'm being bounced all over the place!")
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

    def fetch_pkg_details(self, name):
        r = self.make_request(self.pkg_route.format(name))
        data = r.json()
        try:
            response = self.parse_response(data)
        except NotImplementedError:
            raise
        return self.build_api_response(response)

    def build_api_response(self, response):
        package = {}

        if 'name' in response:
            package['name'] = response['name']
        else:
            package['name'] = False

        if 'description' in response:
            package['description'] = response['description']
        else:
            package['description'] = False

        if 'license' in response:
            package['license'] = response['license']
        else:
            package['license'] = False

        if 'source_repo' in response:
            package['source_repo'] = response['source_repo']
        else:
            package['source_repo'] = False

        if 'homepage' in response:
            package['homepage'] = response['homepage']
        else:
            package['homepage'] = False

        if 'package_page' in response:
            package['package_page'] = response['package_page']
        else:
            package['package_page'] = False

        if 'tarball' in response:
            package['tarball'] = response['tarball']
        else:
            package['tarball'] = False

        if 'latest_version' in response:
            package['latest_version'] = response['latest_version']
        else:
            package['latest_version'] = False

        return json.dumps(package)

    def parse_response(self, data):
        raise NotImplementedError
