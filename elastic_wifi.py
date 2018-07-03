from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

# This is just a test
doc = {"address": "Shanghai Tunnel, 211, Southwest Ankeny Street, Chinatown, Old Town, Portland, Multnomah County, Oregon, 97204, United States of America", "location": "45.5226076,-122.672583510967"}

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


# create index
# es.indices.create(index="wifi-index", body=mapping)
# es.index(index="wifi-index", doc_type="doc", body=doc)


# search through index using the Geo Distance Query
search_body = {
    "query": {
        "bool" : {
            "must" : {
                "match_all" : {}
            },
            "filter" : {
                "geo_distance" : {
                    "distance" : "5km",
                    "location" : {
                        "lat" : 45.60,
                        "lon" : -122.68
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


# # delete index
# es.indices.delete(index='wifi-index', ignore=[400, 404])
