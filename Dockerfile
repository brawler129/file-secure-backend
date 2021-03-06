FROM python:3.6.10

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /file_secure
WORKDIR /file_secure
COPY ./file_secure /file_secure

RUN adduser --no-create-home user
USER user



