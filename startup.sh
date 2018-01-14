#!/bin/bash

pihole disable &

./home/evengy/PIlexangrok http 5000 -subdomain pilocal > /dev/null &

python /home/evengy/PIlexa/pi-control.py > /dev/null &
