FROM ubuntu:latest
MAINTAINER Landon Jurgens landon@computer.org
RUN DEBIAN_FRONTEND=noninteractive apt-get update --fix-missing && apt-get install -y build-essential python python-dev python-setuptools libssl-dev libffi-dev libpq-dev
COPY . /app
WORKDIR /app
RUN pip install .
ENTRYPOINT ["python"]
CMD ["ircb runserver"]
