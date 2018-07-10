import boto3
from chalice import Chalice, Response, NotFoundError
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from geopy.geocoders import Nominatim


app = Chalice(app_name='search_wifi')

host = 'search-elastic-wifi2-tj7nwqymkpo4rxoe3mpdvpxjqi.us-west-2.es.amazonaws.com'
region = 'us-west-2'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

es = Elasticsearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

geolocator = Nominatim()


@app.route('/', methods=['GET', 'POST'], cors=True)
def index():
    """Converting the address received from the client into geographic coordinates and performing Geo Distance searches to find free WiFi spots within a certain distance."""

    request = app.current_request
    street = request.json_body["address"]
    current_address = (street + ", Portland").upper()
    coordinates = geolocator.geocode(current_address, timeout=None)

    if not coordinates:
        raise NotFoundError("Something went wrong. Please double-check your address or try another location.")
    else:

        search_body = {
            "query": {
                "bool" : {
                    "must" : {
                        "match_all" : {}
                    },
                    "filter" : {
                        "geo_distance" : {
                            "distance" : str(request.json_body["distance"]) + "mi",
                            "location" : {
                                "lat" : coordinates.latitude,
                                "lon" : coordinates.longitude
                            }
                        }
                    }
                }
            }
        }

        res = es.search(index="wifi-index", size=100, body=search_body)
        locations_list = []
        for r in res["hits"]["hits"]:
            location_object = {"address": r["_source"]["address"], "coordinates": r["_source"]["location"]}
            locations_list.append(location_object)
        return Response(body={"locations": locations_list}, status_code=200)
