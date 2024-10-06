#!/bin/bash

source .venv/bin/activate

LOG_EXTRACT_FILE="$(mktemp)"

grep Answer /var/log/syslog | egrep 'rcode="0"' | cut -d" " -f 21-23 | sort -u > ${LOG_EXTRACT_FILE}
python3 dns-pusher.py

rm ${LOG_EXTRACT_FILE}