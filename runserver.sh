#!/bin/bash

pid=$(ps aux | grep "./manage.py runserver" | grep -v grep | head -1 | xargs | cut -f2 -d" ")

if [[ -n "$pid" ]]; then
    kill $pid
fi

fuser -k 8000/tcp
python3 manage.py runserver
