from flask import Flask, jsonify

from pkgparse.registry.npm import NPMRegistry
from pkgparse.registry.pypi import PypiRegistry

app = Flask(__name__)

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


@app.route('/pypi/search/<name>')
def search_pypi_package(name):
    registry = PypiRegistry()
    package = registry.fetch_pkg_details(name)
    return jsonify(package)