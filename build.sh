#!/usr/bin/env bash

set -euo pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

docker build -f Dockerfile.local -t thewtex/krs-course-in-biomedical-image-analysis-and-visualization:local $DIR
