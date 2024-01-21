FROM ubuntu:23.04
LABEL maintainer="a.svarych@gmail.com"

ADD requirements.selenium .

RUN apt-get update
RUN apt-get install python3-full python3-pip wget mc -y
RUN ln /usr/bin/python3 /usr/bin/python

RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN apt-get update && apt-get -qqy install google-chrome-stable

RUN python -m venv ~/venv
RUN ~/venv/bin/python -m pip install -r requirements.selenium
