FROM alpine:latest
MAINTAINER Kevin Wang <wangkevin448@gmail.com>

COPY src/ /app/
RUN apk add --no-cache python3 && python3 -m ensurepip && pip3 install --upgrade pip
RUN apk add --no-cache --virtual build-dependencies build-base python3-dev && pip3 install --no-cache-dir --upgrade -r /app/requirements.txt && apk del build-dependencies

VOLUME /app/static

EXPOSE 5000

WORKDIR /app

CMD ["gunicorn", "--workers=2", "--worker-class=gevent", "-b 0.0.0.0:5000", "wsgi:sabotapp"]
