from .session import ElasticsearchSession
from .api import Cluster, Index, Document


class Elasticsearch:
    _cluster = None
    _index = None
    _document = None

    def __init__(self, host):
        self.session = ElasticsearchSession(host)

        self.cluster = Cluster(self.session)
        self.index = Index(self.session)
        self.document = Document(self.session)
