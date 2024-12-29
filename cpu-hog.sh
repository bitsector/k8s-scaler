#!/bin/bash

while true; do
    for i in $(seq 1 10000); do
        if [ $(echo "$(factor $i)" | wc -w) -eq 2 ]; then
            echo $i
        fi
    done
done
