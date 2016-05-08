#!/usr/bin/env bash
export DATASTORE_DATASET=bullet-sabot-test
export DATASTORE_HOST=http://localhost:8080
export DATASTORE_EMULATOR_HOST=localhost:8080
export DATASTORE_PROJECT_ID=bullet-sabot-test

cd src; ../venv/bin/python capsule.py
