FROM python:3.10

MAINTAINER Damian Golał damian.golal@dataspace.pl

ARG TOKEN
ARG REPO
ARG BRANCH

#Base packages
RUN apt update && \
        apt install -y \
        unzip \
        git \
        vim

COPY config/BASIC/docker-entrypoint.sh /docker-entrypoint.sh

EXPOSE 9099

ENTRYPOINT ["/docker-entrypoint.sh"]
