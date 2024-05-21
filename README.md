# MAXMIND geoip lookup service

## Overview

RESTful API that responds to POST methods with application/json content type.
The API receives two data elements in a json format (IPv4 address and a list of allowed countires).

Function "chkCountry" queries the mmdb (MAXMIND DB) file to match the country that IP belongs and compares the matched country with the list of allowed countries we have received in the POST and returns an indication of "PASS" or "FAIL" for the request.

A Dockerfile is included that helps you build your image to be used with Docker engine or an existing kubernetes cluster that can also keep the country mapping data up to date.

Cronjob is added to the docker image to run geoipupdate every Tuesday & Friday.


## Functionality

## Requirements

    - Python 3.9+
    - pip
    - Maxmind Account
    - Maxmind geoip.conf
    - Docker Engine (Optional)
    - Existing Kubernetes Cluster (Optional)
    - minikube Kubernets Cluster for local run (Optional)

## Installation

- Local PC

    - Install pipenv dependency manager

        `pip install pipenv`

    - Create a python 3 virtualenv

        `pipenv --python 3.9`

    - Install pip dependencies
    
        `pipenv install flask`

- Docker

    - Use included "Dockerfile" to build your docker image

        `docker build -t USER/maxmind_geoip .`

    - Run your docker image

        `docker run --name maxmind_geoip -ti jrahno/maxmind_geoip`

- Kubernetes

    - Use included YML files in "kubernetes" folder to create your 2 PODS for load balancing

        `kubectl apply -f geoip_deploy.yml`
        `kubectl apply -f geoip_service.yml`

    - Extract the service URL

        `minikube service list`

## Execution


Sample curl POST:
##### ============================================================
  curl -X POST -H "Content-Type: application/json" -d '{
 "IP": "8.8.8.8",
 "Countries" : ["Canada","United States"]}
' http://localhost:5000;
##### ============================================================
