#!/bin/bash

./ngrok http 5000 -subdomain pilocal > /dev/null &

python pi-control.py > /dev/null &
