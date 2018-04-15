import requests

from pkgparse import settings


class BaseRegistry:

    def __init__(self):
        base_url = None

    def ping(self):
        headers = { "User-Agent": settings.USER_AGENT }
        r = requests.get(self.base_url, headers=headers)
        if r.status_code is 200:
            return True
        return False
