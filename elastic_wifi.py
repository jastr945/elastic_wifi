import time
from elasticsearch import Elasticsearch
from geopy.geocoders import Nominatim

es = Elasticsearch()
geolocator = Nominatim()


def find_locations():
    """Taking user input, converting into coordinates and searching through the Elasticsearch index to find the closest WiFi spots."""

    street = input("Enter your location: ")
    current_address = street + ", Portland"
    try:
        coordinates = geolocator.geocode(current_address, timeout=None)
        print("Your coordinates: {}, {}...".format(coordinates.latitude, coordinates.longitude))

        time.sleep(2)
        print("Searching for free WiFi spots near you...")
        time.sleep(3)

        # search through index using the Geo Distance Query
        search_body = {
            "query": {
                "bool" : {
                    "must" : {
                        "match_all" : {}
                    },
                    "filter" : {
                        "geo_distance" : {
                            "distance" : "0.2mi",
                            "location" : {
                                "lat" : coordinates.latitude,
                                "lon" : coordinates.longitude
                            }
                        }
                    }
                }
            }
        }

        res = es.search(index="wifi-index", body=search_body)

        print("Got %d Hits:" % res['hits']['total'])
        for hit in res['hits']['hits']:
            print(hit["_source"], "\n")

    except AttributeError:
        print("Couldn't find coordinates for this address: {}".format(current_address))

    return("Search finished.")


print(find_locations())
