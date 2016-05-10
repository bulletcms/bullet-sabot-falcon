#!/usr/bin/env bash

./venv/bin/pex . -r bulletsabot/requirements.txt -m bulletsabot -o pexdist/bulletsabot.pex
