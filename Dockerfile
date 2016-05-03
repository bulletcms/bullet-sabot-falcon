FROM python:alpine
MAINTAINER Kevin Wang <wangkevin448@gmail.com>

WORKDIR /app

COPY src/ /app/
RUN pip install -r /app/requirements.txt

VOLUME /app/static

EXPOSE 5000

CMD ["gunicorn", "--workers=4", "-b 0.0.0.0:5000", "wsgi:sabotapp"]
