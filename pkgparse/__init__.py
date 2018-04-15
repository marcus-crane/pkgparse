from flask import Flask, jsonify

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
