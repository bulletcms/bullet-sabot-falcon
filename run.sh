#!/usr/bin/env bash

# ./venv/bin/python src/app.py

version="v1.2.1"

if ! [ -e "$PWD/rkt/rkt" ]; then
  wget "https://github.com/coreos/rkt/releases/download/$version/rkt-$version.tar.gz" -O rkt.tar.gz
  tar -xvzf rkt.tar.gz -C "$PWD/rkt" --strip-components=1
  rm rkt.tar.gz
fi

if ! [ -e "$PWD/bullet-sabot.aci" ]; then
  ./build.sh
fi

./rkt/rkt --insecure-options=image run --hostname="bullet-sabot" --port=http:80 --volume static,kind=host,source=/home/kevin/projects/webdev/bullet-tracer/dist,readOnly=true ./bullet-sabot.aci
