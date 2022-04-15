#!/bin/sh
cd ./src
docker build -t python_cbr_server:latest .

NETWORK_NAME=python_cbr_cbr_network
SUBNET=172.59.0.0/16
docker network inspect ${NETWORK_NAME} >/dev/null 2>&1 || \
    docker network create --subnet=${SUBNET} --driver bridge ${NETWORK_NAME}
cd ..
docker pull redis:latest
