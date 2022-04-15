#!/bin/bash
docker-compose down  
docker stop py_srv python_cbr_redis_1;docker rm py_srv python_cbr_redis_1;docker rmi python_cbr_server:latest redis:latest;docker network rm python_cbr_cbr_network

