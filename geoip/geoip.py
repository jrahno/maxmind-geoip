# Title: Maxmind GeoIP lookup
# Author: Javid Rahno [https://github.com/jrahno]
# Email: javid@bell.net
# Date: May 21, 2024
# License: GNU General Public License v3.0
#
#
# RESTful API that responds to POST methods with application/json content type.
# The API receives two data elements in a json format (IPv4 address and a list of allowed countires).

# Function "chkCountry" queries the mmdb (MAXMIND DB) file to match the country that IP belongs 
# and compares the matched country with the list of allowed countries we have received in the POST 
# and returns an indication of "PASS" or "FAIL" for the request.
#
# Sample curl POST:
# ============================================================
#   curl -X POST -H "Content-Type: application/json" -d '{
#  "IP": "8.8.8.8",
#  "Countries" : ["Canada","United States"]}
# ' http://localhost:5000;
# ============================================================
# 

import geoip2.database
from flask import Flask, request

app = Flask(__name__) # Define our flask import name
    
@app.route('/', methods=['POST']) # We only accept POST method here

# Define chkCountry function to query th 
def chkCountry():
        # save received elements in separate variables
        ip = request.json['IP']
        allowed = request.json['Countries']

        # convert list of countries to lower case
        countries = [i.lower() for i in allowed]

        # Read the MAXMIND mmdb file and dump the data into a dictionary for the given IP address
        with geoip2.database.Reader('/usr/share/GeoIP/GeoLite2-Country.mmdb') as reader:
            c = reader.country(ip)

            # Return a string/code if we have a country match
            if c.country.name.lower() in countries:
                return ("PASS\n")
            
                # Option to return 200
                # return '', 200
            else:
                return ("FAIL\n")
            
                # Option to return 404
                # return '', 404
