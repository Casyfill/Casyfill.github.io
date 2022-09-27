FROM python:3.7-slim as base 
ARG PELICAN_THEME_FOLDER="./theme"
ARG PELICAN_CONFIG_FILE="./pelicanconf.py"
ARG PELICAN_CONTENT_FOLDER="./content"

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8


RUN apt-get update \
    && apt-get install --no-install-recommends -qy git curl bash

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs

COPY ./theme ./theme
RUN npm install

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt


COPY ./pelicanconf.py ./pelicanconf.py
COPY ./content ./content
RUN pelican ${PELICAN_CONTENT_FOLDER:=content} -o output -s ${PELICAN_CONFIG_FILE:=pelicanconf.py}