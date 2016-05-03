#!/usr/bin/env bash

docker run -d --net=host -v /home/kevin/projects/webdev/bullet-tracer/dist:/app/static --name bullet-sabot-container bullet-sabot 
