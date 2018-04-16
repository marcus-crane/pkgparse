import json


def load_json_string(file_path):
    with open(file_path, encoding="utf-8") as file:
        return file.read()


def load_json_fixture(file_path):
    with open(file_path, encoding="utf-8") as file:
        return json.load(file)