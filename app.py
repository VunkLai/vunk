'''Where is the test?
'''

from elasticsearch import Elasticsearch

es = Elasticsearch(host='https://HOST:PORT')

if not es.index.exists('INDEX_NAME'):
    es.index.create('INDEX_NAME')

es.document.create('INDEX_NAME', doc={'KEY': 'VALUE'})
