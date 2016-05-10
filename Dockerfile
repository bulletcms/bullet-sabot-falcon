FROM alpine

MAINTAINER Kevin Wang <wangkevin448@gmail.com>

RUN apk add --no-cache python3 && apk -vv info

COPY build/bulletsabot.pex /

COPY bulletsabot/ /app/

VOLUME /app/static

EXPOSE 5000

WORKDIR /

CMD ["./bulletsabot.pex", "app/__main__.py"]
