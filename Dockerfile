FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

# Install postgres client
RUN apk add --update --no-cache postgresql-client

# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev


# install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt


# Remove dependencies
RUN apk del .tmp-build-deps

WORKDIR /app
COPY ./app /app