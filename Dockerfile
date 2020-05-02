FROM python:3.6.10
MAINTAINER Devesh Pradhan

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /file_secure
WORKDIR /file_secure
COPY ./file_secure /file_secure

RUN adduser -D user
USER user



