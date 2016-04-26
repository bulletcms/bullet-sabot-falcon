FROM python:alpine
MAINTAINER Kevin Wang <wangkevin448@gmail.com>

WORKDIR /app

COPY src/ /app/
RUN pip install -r /app/requirements.txt

VOLUME /app/static

EXPOSE 5000

CMD ["python", "app.py"]
