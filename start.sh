#!/usr/bin/env bash

docker run -d -p 5000:5000 -v /home/kevin/projects/webdev/bullet-tracer/dist:/app/static --name bullet-sabot-container bullet-sabot 
