#!/usr/bin/env bash
export DATASTORE_DATASET=bullet-sabot-test
export DATASTORE_HOST=http://localhost:8080
export DATASTORE_EMULATOR_HOST=localhost:8080
export DATASTORE_PROJECT_ID=bullet-sabot-test

cd src; ../venv/bin/gunicorn --workers=4 --worker-class=meinheld.gmeinheld.MeinheldWorker -b 0.0.0.0:5000 wsgi:application
