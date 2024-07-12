FROM python:3.11.5-alpine

RUN apk update && apk add python3-dev gcc libc-dev

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./galmart /app/backend
ADD ./docker /app/docker
