FROM public.ecr.aws/docker/library/python:3.12-alpine3.19 AS base

ENV PYTHONUNBUFFERED=1

RUN apk update && \
    apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    bash

WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir poetry==1.8.2
RUN poetry config virtualenvs.create false
RUN poetry install