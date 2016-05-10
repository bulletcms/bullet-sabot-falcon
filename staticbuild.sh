#!/usr/bin/env bash

virtualenv venv
./venv/bin/pip install --upgrade -r bulletsabot/requirements.txt
./venv/bin/pip install --upgrade pex

./venv/bin/pex -r bulletsabot/requirements.txt -o build/bulletsabot.pex
