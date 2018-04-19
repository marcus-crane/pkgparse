import json
import os


def load_json_fixture(file_name, parse=True):
    CURRENT_PATH = os.path.dirname(__file__)
    fixture_path = os.path.join(CURRENT_PATH, f"fixtures/{file_name}")
    with open(fixture_path, encoding="utf-8") as file:
        return json.load(file)
