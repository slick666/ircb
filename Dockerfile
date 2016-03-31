FROM ubuntu:latest
MAINTAINER Landon Jurgens landon@computer.org
RUN DEBIAN_FRONTEND=noninteractive apt-get update --fix-missing && apt-get install -y build-essential python3 python3-pip python3-dev python3-setuptools libssl-dev libffi-dev libpq-dev python3-psycopg2 git
COPY . /app
WORKDIR /app
RUN python3 setup.py develop
RUN chmod +x /app/dockerrun.sh
CMD "/app/dockerrun.sh"
