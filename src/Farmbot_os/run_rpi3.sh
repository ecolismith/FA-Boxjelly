#!/bin/bash

set -e
set -o pipefail

export MIX_ENV=test

echo "######### Fetch Deps"
mix deps.get --all
mix format
MIX_ENV=test mix compile --force

echo "######### Build RPI3 FW"

MIX_TARGET=rpi3 MIX_ENV=prod mix deps.get
MIX_TARGET=rpi3 MIX_ENV=prod mix compile --force
MIX_TARGET=rpi3 MIX_ENV=prod mix firmware

echo "######### Build RPI3 IMG"
fwup -a -d myimage.img -i _build/rpi3/rpi3_prod/nerves/images/farmbot.fw -t complete


