#!/bin/sh
export FLASK_APP=/MAXMIND/geoip.py
pipenv run flask --debug run -h 0.0.0.0