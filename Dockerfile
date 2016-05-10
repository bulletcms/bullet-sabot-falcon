FROM python:alpine

MAINTAINER Kevin Wang <wangkevin448@gmail.com>

COPY bulletsabot/requirements.txt /app/

RUN apk add --no-cache --virtual build gcc musl-dev && pip install --no-cache-dir --upgrade -r /app/requirements.txt && apk del build && apk -vv info

COPY bulletsabot/ /app/

VOLUME /app/static

EXPOSE 5000

WORKDIR /

CMD ["python", "app"]
