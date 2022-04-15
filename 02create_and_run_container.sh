#/bin/bash
export WEB_DNS_NAME=xch2json
export NETWORK=python_cbr_cbr_network
export WEB_IP_ADDR=172.59.0.2
export WEB_IP_PORT=8000
export REDIS_IP_ADDR=172.59.0.3
export REDIS_NAME=redisdb
export REDIS_PORT=6379

#-d --restart unless-stopped \ -v "$PWD/src":/usr/local/cbr2json 

docker run -d --restart unless-stopped \
    --network ${NETWORK} --ip ${WEB_IP_ADDR} \
    --add-host=${REDIS_NAME}:${REDIS_IP_ADDR} \
    --net-alias=${WEB_DNS_NAME} --hostname ${WEB_DNS_NAME} \
    -p ${WEB_IP_PORT}:${WEB_IP_PORT} \
    --name py_srv \
    python_cbr_server:latest 

docker run -d --restart unless-stopped \
    --network ${NETWORK} --ip ${REDIS_IP_ADDR} \
    --net-alias=${REDIS_NAME} --hostname ${REDIS_NAME} \
    --add-host=${WEB_DNS_NAME}:${WEB_IP_ADDR} \
    -p ${REDIS_PORT}:${REDIS_PORT} \
    --name python_cbr_redis_1 \
    redis:latest

