#!/usr/bin/env bash
set -e

if [ "$EUID" -ne 0 ]; then
  echo "This script uses functionality which requires root privileges"
  exit 1
fi

version="v0.2.2"

# installs acbuild
if ! [ -e "$PWD/build_modules/acbuild" ]; then
  wget https://github.com/appc/acbuild/releases/download/$version/acbuild.tar.gz && tar -xvzf acbuild.tar.gz -C "$PWD/build_modules" && rm acbuild.tar.gz
fi


# Start the build with an empty ACI
./build_modules/acbuild --debug begin

# In the event of the script exiting, end the build
acbuildEnd() {
  export EXIT=$?
  ./build_modules/acbuild --debug end && exit $EXIT
}
trap acbuildEnd EXIT


# Name the ACI
./build_modules/acbuild --debug set-name xorkevin/bullet-sabot

# Version info
./build_modules/acbuild label add version 0.1.0
./build_modules/acbuild label add arch amd64
./build_modules/acbuild label add os linux
./build_modules/acbuild annotation add authors "xorkevin <wangkevin448@gmail.com>"

# Copy python and flask app
./build_modules/acbuild --debug copy ./venv /usr
./build_modules/acbuild --debug copy ./src /var/www

# Add a port for http traffic over port 5000
./build_modules/acbuild --debug port add http tcp 5000

# Add a mount point for static files to serve
./build_modules/acbuild --debug mount add static /var/www/src/static

# Run nginx in the foreground
./build_modules/acbuild --debug set-exec -- /usr/venv/bin/python /var/www/src/app.py

# Save the ACI
./build_modules/acbuild --debug write --overwrite bullet-sabot.aci
