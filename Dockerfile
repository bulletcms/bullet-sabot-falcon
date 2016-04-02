FROM alpine:latest
MAINTAINER Kevin Wang <wangkevin448@gmail.com>

RUN apk add --update python py-pip && pip install virtualenv && rm -rf /var/cache/apk/*

WORKDIR /app

COPY src/ /app/
RUN pip install -r /app/requirements.txt

VOLUME /app/static

EXPOSE 5000

CMD ["python", "app.py"]
