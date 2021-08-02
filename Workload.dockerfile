FROM alpine:3.14

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app

WORKDIR $APP_HOME

RUN apk add --no-cache python3 py3-pip \
    && pip install flask gunicorn

COPY workload.py ./

CMD exec gunicorn --bind :$PORT --workers 4 --threads 8 --timeout 0 workload:app
