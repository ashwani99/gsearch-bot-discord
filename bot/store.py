from datetime import datetime

from pymongo import MongoClient, errors, DESCENDING

from settings import DATABASE_URL, DATABASE_NAME


class SearchQueryStore:
    collection_name = 'queries'

    def __init__(self):
        try:
            self._mongo_client = MongoClient(DATABASE_URL)
            self.store_collection = self._mongo_client[DATABASE_NAME][SearchQueryStore.collection_name]
        except errors.ConnectionFailure:
            print('''Could not establish a connection to the database
                  
                  Please check environment variable GSEARCH_BOT_DB_URL
                  
                  Set the environment variable:
                    export GSEARCH_BOT_DB_URL=<your-database-url>''')
    
    def get_recent_searches(self, guild_id, user_id, keyword, limit):
        keyword = keyword if keyword else ''
        
        recent_searches = self.store_collection.find({
            'guild_id': guild_id,
            'user_id': user_id,
            'query': {
                '$regex': f'.*{keyword}.*'
            }
        }).sort('timestamp', DESCENDING)

        return [rs['query'] for rs in recent_searches][:limit]

    def push_search_query(self, guild_id, user_id, query):
        self.store_collection.insert_one({
            'guild_id': guild_id,
            'user_id': user_id, 
            'query': query,
            'timestamp': datetime.utcnow()
        })


search_store = SearchQueryStore()
