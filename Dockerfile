FROM python:3.11.1-alpine3.17
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY . /niyo
WORKDIR /niyo

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt 

COPY . .
