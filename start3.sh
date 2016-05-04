#!/usr/bin/env bash

docker run -d -p 5001:5000 -v /home/kevin/projects/webdev/bullet-tracer/dist:/app/static --name bullet-sabot-container-1 bullet-sabot
docker run -d -p 5002:5000 -v /home/kevin/projects/webdev/bullet-tracer/dist:/app/static --name bullet-sabot-container-2 bullet-sabot
docker run -d -p 5003:5000 -v /home/kevin/projects/webdev/bullet-tracer/dist:/app/static --name bullet-sabot-container-3 bullet-sabot
