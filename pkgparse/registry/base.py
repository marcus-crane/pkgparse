import sys

import requests

from pkgparse import settings


class BaseRegistry:

    def __init__(self):
        """
        This function is called whenever a new BaseRegistry class is created
        and these variables also pass onto inheriting classes.

        Inheriting classes need to create a definition for them as they're
        used for a number of things:

        pkg_route is the endpoint that returns details about a package.
        At the moment, this means whichever endpoint provides the most
        information with the smallest Content-Length. For example, NPM
        provides a /latest route which only returns the latest version.
        This is ideal, for now, as we don't do anything with previous
        versions.

        test_pkg is nothing more than the name of a package that is known
        to exist and can be pinged in order to test that a response is
        being returned. Most of the registries don't seem to have actual
        ping routes and pinging the root of the API doesn't always return
        the designed response ie; HTML, a 404 and so on.

        pkg_page is the URL that would pull up, well, the page
        for a package. That is to say, what's the URL that a user,
        not a developer, would visit ie; HTML, not JSON.

        It should be noted that pkg_route and pkg_page both use
        string interpolation. As an example, the pkg_page for
        Jekyll, which lives on RubyGems, would be
        https://rubygems.org/gems/{0} where the {0} is later
        filled with the string "jekyll".

        You'll find that a number of registries omit the pkg_page
        variable however because their API responses already prove
        a link to one. It felt a bit redundant defining it when
        the response we're already getting contains a link to
        the package page, y'know?
        """
        self.pkg_route = None
        self.test_pkg = None
        self.pkg_page = None

    def make_request(self, url, headers={}):
        """
        A generic requests wrapper that handles appending the User Agent
        for me automatically.

        :param url: string
        :param headers: dictionary
        :return: requests.models.Response
        """
        headers.update({"User-Agent": settings.USER_AGENT})
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
            url = self.pkg_route.format(self.test_pkg)
            r = self.make_request(url)
            if r.status_code == 200:
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
        implement their own version, this base class throws a
        NotImplementedError upon attempting to use it.

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
        elif self.pkg_page:
            package['package_page'] = self.pkg_page.format(response['name'])
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
