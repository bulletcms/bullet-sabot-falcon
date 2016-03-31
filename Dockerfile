FROM alpine:latest
EXPOSE 8080
COPY venv/ /venv/
COPY src/ /src/
ENTRYPOINT ["/venv/bin/python", "/src/app.py"]
