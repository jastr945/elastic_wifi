import re
import requests
import boto3
import click
from geopy.geocoders import Nominatim
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth


geolocator = Nominatim()

# Connecting to AWS Elasticsearch Service
host = 'search-elastic-wifi2-tj7nwqymkpo4rxoe3mpdvpxjqi.us-west-2.es.amazonaws.com'
region = 'us-west-2'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service)

es = Elasticsearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

# Creating the mapping with a Geo-Point
mapping = {
        "mappings": {
            "doc": {
                "properties": {
                    "address": {
                        "type": "text"
                    },
                    "location": {
                        "type": "geo_point"
                    }
                }
            }
        }
    }


# es.indices.create(index="wifi-index", body=mapping)


# def get_wifi():
#     """Extracts WiFi locations from a website and saves them into a database."""
#
#     resp = requests.get("http://www.openwifispots.com/citylist_free_wifi_wireless_hotspot-Portland_OR.aspx")
#     fulltext = resp.text
#     middlecut = fulltext[fulltext.find("""<div id="location5952"""):fulltext.find("""Been here? <a href="javascript:addComment(265904)""")]
#     multiple_commas = re.sub("<[^<]+?>", ",", middlecut)
#     single_commas = re.sub(r"[,]+", ",", multiple_commas)[1:-1]
#     result = single_commas.split(",Been here? ,Add a comment...,")
#
#     for r in result:
#
#         doc = {}
#
#         addresscut = r.split(",")
#         for a in addresscut:
#             if "..." in a:
#                 addresscut.remove(a)
#         address_total = addresscut[1] + ", " + addresscut[2] + "," + addresscut[3]
#
#         try:
#             location = geolocator.geocode(address_total, timeout=None)
#             doc["address"] = location.address
#             doc["location"] = str(location.latitude) + "," + str(location.longtitude)
#             es.index(index="wifi-index", doc_type="doc", body=doc)  # adding the data into the Elastcsearch index
#             print("{} was saved into the database".format(addresscut[0]))
#         except AttributeError:
#             print("Couldn't convert this one: {}".format(address_total))
#
#     return("Finished manipulating data.")


def populate_es():
    """Populates the Elasticsearch index with the data from wifi.txt, in case geopy throws timeout error."""

    f = open("wifi.txt", "r")
    for line in f:
        doc = {}
        address = line.split("of America ")[0]
        lat = (line.split("of America ")[1]).split(" ")[0]
        lng = ((line.split("of America ")[1]).split(" ")[1]).split("\n")[0]
        location = lat + "," + lng
        doc["address"] = address
        doc["location"] = location
        es.index(index="wifi-index", doc_type="doc", body=doc)  # adding the data into the Elastcsearch index
    return("Finished populating wifi-index.")

#
print(populate_es())

# # delete index
# es.indices.delete(index='wifi-index', ignore=[400, 404])
