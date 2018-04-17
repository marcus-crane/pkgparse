from flask import Flask, jsonify

from pkgparse.registry.npm import NPMRegistry
from pkgparse.registry.nuget import NugetRegistry
from pkgparse.registry.pypi import PypiRegistry
from pkgparse.registry.rubygems import RubygemsRegistry

app = Flask(__name__)

"""
Disables a feature deprecated here:
https://github.com/pallets/werkzeug/pull/1099
The master branch of Flask fixes this but there
hasn't been a release since the fix was made.
"""
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/npm/search/<name>')
def search_npm_package(name):
    registry = NPMRegistry()
    package = registry.fetch_pkg_details(name)
    return jsonify(package)


@app.route('/nuget/search/<name>')
def search_nuget_package(name):
    registry = NugetRegistry()
    package = registry.fetch_pkg_details(name)
    return jsonify(package)


@app.route('/pypi/search/<name>')
def search_pypi_package(name):
    registry = PypiRegistry()
    package = registry.fetch_pkg_details(name)
    return jsonify(package)


@app.route('/rubygems/search/<name>')
def search_rubygems_package(name):
    registry = RubygemsRegistry()
    package = registry.fetch_pkg_details(name)
    return jsonify(package)
