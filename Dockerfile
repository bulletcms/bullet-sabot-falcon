FROM python:alpine

MAINTAINER Kevin Wang <wangkevin448@gmail.com>

COPY src/ /app/

RUN apk add --no-cache --virtual build-dependencies gcc musl-dev && pip install --no-cache-dir --upgrade -r /app/requirements.txt && apk del build-dependencies && apk -vv info

VOLUME /app/static

EXPOSE 5000

WORKDIR /app

CMD ["gunicorn", "--workers=4", "--worker-class=gevent", "-b 0.0.0.0:5000", "wsgi:sabotapp"]
