FROM jenkins/jenkins:lts
LABEL maintainer="a.svarych@gmail.com"

ADD requirements.jenkins .

USER root
RUN apt-get update
RUN apt-get install -y wget python3-full python3-pip vim mc docker-compose
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN python3 -m venv ~/venv
RUN ~/venv/bin/python -m pip install --upgrade pip setuptools wheel
RUN ~/venv/bin/python -m pip install -r requirements.jenkins
