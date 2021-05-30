#!/bin/bash

if ! pgrep -xq mysqld
then
    mysqld &
    disown
fi

source venv/bin/activate
export FLASK_APP=webpage.py
flask run