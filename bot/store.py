from datetime import datetime

from pymongo import MongoClient

from settings import DATABASE_URL, DATABASE_NAME


class SearchQueryStore:
    collection_name = 'queries'

    def __init__(self):
        self._mongo_client = MongoClient(DATABASE_URL)
        self.store_collection = self._mongo_client[DATABASE_NAME][SearchQueryStore.collection_name]
    
    def get_recent_searches(self, userid, keyword, limit):
        keyword = keyword if keyword else ''
        recent_searches = self.store_collection.find({
            'userid': userid,
            'query': {
                '$regex': f'.*{keyword}.*'
            } 
        })
        return [rs['query'] for rs in recent_searches][:limit]

    def push_search_query(self, userid, query):
        self.store_collection.insert_one({
            'userid': userid, 
            'query': query,
            'timestamp': datetime.utcnow()
        })


search_store = SearchQueryStore()
