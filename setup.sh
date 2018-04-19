#!/usr/bin/env bash

pip3 install invoke
pip3 install virtualenv

rm -rf venv
virtualenv -p python3.6 env
source env/bin/activate
pip install -r requirements.txt