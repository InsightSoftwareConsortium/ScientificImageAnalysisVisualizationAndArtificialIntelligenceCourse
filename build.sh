#!/usr/bin/env bash

set -euo pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

docker build -f Dockerfile.local -t vicory/ms-hackathon:local $DIR
docker build -f Dockerfile.jupyterhub -t vicory/ms-hackathon:$(git rev-parse HEAD | cut -c1-7) $DIR
