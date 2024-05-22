#!/bin/sh
export FLASK_APP=geoip/geoip.py
pipenv run flask --debug run -h 0.0.0.0