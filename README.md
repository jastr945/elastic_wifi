# elastic_wifi

This program extracts free WiFi locations in Portland, OR from www.openwifispots.com, converts them into geographic coordinates and allows users to find the closest WiFi spot.

Tools used:

- ```elasticsearch-py```, Python client for Elasticsearch;
- ```GeoPy```, Python client for for several popular geocoding web services;
- ```sqlite3``` database for saving locations and coordinates.
