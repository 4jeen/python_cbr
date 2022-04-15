FROM ubuntu:20.04
#FROM python:3.10-slim as compiler
RUN apt update && \
	apt install -y python3-pip \
		python3-dev \
		build-essential \
		libssl-dev \
		libffi-dev \
		python3-setuptools \
		python3-venv && \
    rm -rf /var/lib/apt/lists/* && \
    apt clean && \
    mkdir /usr/local/cbr2json 

ADD *.py /usr/local/cbr2json/
ADD *.txt /usr/local/cbr2json/

WORKDIR /usr/local/cbr2json

RUN pip3 install -Ur requirements.txt

VOLUME /usr/local/cbr2json

EXPOSE 8000

CMD [ "python3", "./srv.py"]



