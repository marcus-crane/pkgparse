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
        """
        A generic requests wrapper that handles appending the User Agent
        for me automatically.

        :param url: string
        :param headers: dictionary
        :return: requests.models.Response
        """
        headers.update({ "User-Agent": settings.USER_AGENT })
        return requests.get(url, headers=headers)

    def ping(self):
        """
        A generic ping function that makes a GET request to the root
        of the inheriting registry (ie; https://registry.npmjs.com)
        and makes a GET request.

        If a 200 is returned, we assume it's alive and well, otherwise
        we figure that it's not. It works for now.

        :return: boolean
        """
        try:
            r = self.make_request(self.root)
            if r.status_code is 200:
                return True
            return False
        except requests.exceptions.RequestException as e:
            # TODO: Implement a better way of handling errors
            print(e)
            sys.exit(1)

    def fetch_pkg_details(self, name):
        """
        A generic fetch function that takes the name of a package
        and then performs everything requests to fetch details
        about that package.

        The majority of this function, excluding the parse_response
        function is abstracted away from the actual registries thenselves.

        Unfortunately, parse_response can't be avoided since each registry
        has a different response.

        In order to ensure that inheriting classes
        implement their own version, this base class throws a NotImplementedError
        upon attempting to use it.

        :param name: string
        :return: dictionary
        """
        r = self.make_request(self.pkg_route.format(name))
        if r.status_code == 200:
            data = r.json()
        else:
            """
            TODO: A very hacky way of ignoring invalid packages.
            
            Error messages should presumably be stored externally and
            thrown as needed.
            
            Any errors here with the request, that aren't external repo
            related, don't really need to be logged to the user since
            it'd be my fault.
            """
            return {'error': 'Invalid package name'}
        try:
            response = self.parse_response(data)
        except NotImplementedError:
            raise
        return self.build_api_response(response)

    def build_api_response(self, response):
        """
        A generic object reshaping function. I don't know what you'd call
        it but it just checks what was found and what wasn't.

        The registry specific parse_response functions return only the keys
        that it finds, rather than filling in blank entries with a zero value.

        :param response: dictionary
        :return: dictionary
        """
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
        elif self.package_page:
            package['package_page'] = self.package_page.format(response['name'])
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

        return package

    def parse_response(self, data):
        raise NotImplementedError
