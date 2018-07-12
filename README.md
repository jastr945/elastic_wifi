# elastic_wifi

This program extracts free WiFi locations in Portland, OR from www.openwifispots.com, converts them into geographic coordinates and allows users to find the closest WiFi spot.

Tools used:

- ```elasticsearch-py```, Python client for Elasticsearch;
- ```GeoPy```, Python client for for several popular geocoding web services;
- ```chalice```, for deploying Flask backend on AWS Lambda;
- ```boto3```, the Amazon Web Services (AWS) SDK for Python;
- Google Maps API and Google Places API for displaying the map and auto-suggesting the addresses;
- ```@angular/cli```, for creating a one-page frontend app;

## Demo

http://wifi.mee.how/
