# elastic_wifi

This program extracts free WiFi locations in Portland, OR from www.openwifispots.com, converts them into geographic coordinates and allows users to find the closest WiFi spot.

Tools used:

- ```elasticsearch-py```, Python client for Elasticsearch;
- ```GeoPy```, Python client for for several popular geocoding web services;
- ```chalice```, for deploying Flask backend on AWS Lambda

## Demo

[work in progress...]

## Run

Pull and run the official Elasticsearch image:

```sh
  $ docker pull docker.elastic.co/elasticsearch/elasticsearch:6.3.0
  $ docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.3.0
```

Install the dependencies:

```sh
  $ pip install -r requirements.txt
```
