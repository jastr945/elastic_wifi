import unittest
from elasticsearch import Elasticsearch
from geopy.geocoders import Nominatim


es = Elasticsearch()
geolocator = Nominatim()


# es.indices.delete(index='test-index', ignore=[400, 404])

class ESTestCase(unittest.TestCase):

    def test_index_view(self):
        """Checking if the index view accepts requests and searches the index correctly."""


    def test_es_creation(self):


        # mapping = {
        #             "mappings": {
        #                 "doc": {
        #                     "properties": {
        #                         "address": {
        #                             "type": "text"
        #                         },
        #                         "location": {
        #                             "type": "geo_point"
        #                         }
        #                     }
        #                 }
        #             }
        #         }
        #
        # es.indices.create(index="test-index", body=mapping)

        doc = {
            "address": "204, Southeast Oak Street, Portland",
            "location": {
                "lat": 45.51995395,
                "lon": -122.66349373542
            }
        }

        doc2 = {
            'address': 'Shanghai Tunnel, 211, Southwest Ankeny Street, Chinatown, Old Town, Portland, Multnomah County, Oregon, 97204, United States ',
            'location': {
                'lat': 45.5226076,
                'lon': -122.672583510967
            }
        }


        es.index(index="test-index", doc_type="doc", body=doc)
        es.index(index="test-index", doc_type="doc", body=doc2)

        search_body = {
            "query": {
                "bool" : {
                    "must" : {
                        "match_all" : {}
                    },
                    "filter" : {
                        "geo_distance" : {
                            "distance" : "10mi",
                            "location" : {
                                "lat" : 45.5208233333333,
                                "lon" : -122.663885
                            }
                        }
                    }
                }
            }
        }

        res = es.search(index="test-index", size=100, body=search_body)
        for r in res["hits"]["hits"]:
            print(r)
