#!/usr/bin/env bash

set -euo pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

docker build -f Dockerfile.local -t thewtex/itk-course:local $DIR
docker build -f Dockerfile.jupyterhub -t thewtex/itk-course:$(git rev-parse HEAD | cut -c1-7) $DIR
