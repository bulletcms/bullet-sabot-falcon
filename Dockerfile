FROM python:alpine

MAINTAINER Kevin Wang <wangkevin448@gmail.com>

COPY src/requirements.txt /app/

RUN apk add --no-cache --virtual build-dependencies gcc musl-dev && pip install --no-cache-dir --upgrade -r /app/requirements.txt && apk del build-dependencies && apk -vv info

COPY src/ /app/

VOLUME /app/static

EXPOSE 5000

WORKDIR /app

CMD ["python", "capsule.py"]
