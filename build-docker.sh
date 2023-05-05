#!/bin/bash
docker rm -f mnmlsm_challenge
docker build --tag=mnmlsm_challenge .
docker run -p 1337:8005 -it --name=mnmlsm_challenge mnmlsm_challenge
