#!/usr/bin/env bash

virtualenv venv
./venv/bin/pip install --upgrade -r bulletsabot/requirements.txt
./venv/bin/pip install --upgrade pex
