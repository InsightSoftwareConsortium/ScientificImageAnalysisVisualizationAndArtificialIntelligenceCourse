#!/usr/bin/env bash

docker run \
  -it \
  --rm \
  -p 8888:8888 \
  --user root \
  -e NB_UID=$(id -u) \
  -e NB_GID=$(id -g) \
  -e GRANT_SUDO=yes \
  -v $PWD:/home/jovyan/work \
  vicory/ms-hackathon:local
