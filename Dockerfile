FROM python:3.8-alpine

# Set environtment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFEERED 1

# Set working directory
WORKDIR /src

# install build-essentials
RUN apk update \
    && apk add --virtual build-deps gcc musl-dev \
    && apk add --no-cache mysql-dev mariadb-connector-c-dev

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN apk del build-deps

# Copy project
COPY . .

# create table
RUN python create_db.py
