from flask import Flask
from flask.json import dumps

from pkgparse.registry.npm import NPMRegistry
from pkgparse.registry.pypi import PypiRegistry

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/npm/search/pkgparse')
def search_npm_package():
    registry = NPMRegistry()
    package = registry.fetch_pkg_details('pkgparse')
    return dumps(package)


app.route('/pypi/search/requests')
def search_pypi_package():
    registry = PypiRegistry()
    package = registry.fetch_pkg_details('requests')
    return dumps(package)