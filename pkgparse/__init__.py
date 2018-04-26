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

# General routes


@app.route('/')
def list_endpoints():
    func_list = {}
    endpoints = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            endpoints.append(rule.rule)
    endpoints.sort()
    for index, endpoint in enumerate(endpoints):
        func_list[index] = endpoint
    return jsonify(func_list)

# Ping Routes


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/ping/npm')
def ping_npm():
    registry = NPMRegistry()
    status = registry.ping()
    return jsonify(status)


@app.route('/ping/nuget')
def ping_nuget():
    registry = NugetRegistry()
    status = registry.ping()
    return jsonify(status)


@app.route('/ping/pypi')
def ping_pypi():
    registry = PypiRegistry()
    status = registry.ping()
    return jsonify(status)


@app.route('/ping/rubygems')
def ping_rubygems():
    registry = RubygemsRegistry()
    status = registry.ping()
    return jsonify(status)


# Registries

@app.route('/npm/<name>')
def search_npm_package(name):
    registry = NPMRegistry()
    package = registry.fetch_pkg_details(name)
    return jsonify(package)


@app.route('/nuget/<name>')
def search_nuget_package(name):
    registry = NugetRegistry()
    package = registry.fetch_pkg_details(name)
    return jsonify(package)


@app.route('/pypi/<name>')
def search_pypi_package(name):
    registry = PypiRegistry()
    package = registry.fetch_pkg_details(name)
    return jsonify(package)


@app.route('/rubygems/<name>')
def search_rubygems_package(name):
    registry = RubygemsRegistry()
    package = registry.fetch_pkg_details(name)
    return jsonify(package)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
