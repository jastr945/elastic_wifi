import boto3
from chalice import Chalice
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth


app = Chalice(app_name='elastic_wifi')
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


document = {
    "title": "Moneyball",
    "director": "Bennett Miller",
    "year": "2011"
}

es.indices.delete(index='movies', ignore=[400, 404])



# @app.route('/')
# def index():
#     resp = es.get(index="movies", doc_type="movie", id="5")
#     return resp
