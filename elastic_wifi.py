from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

# Just a test
es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
print(es.get(index="my-index", doc_type="test-type", id=42)['_source'])
