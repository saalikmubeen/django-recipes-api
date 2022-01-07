FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1


# install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
COPY ./app /app