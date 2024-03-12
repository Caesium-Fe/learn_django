from django.core.cache.backends.base import BaseCache
from pymongo import MongoClient
import pickle


class MongoDBCache(BaseCache):
    def __init__(self, server, params):
        super().__init__(params)
        self.client = MongoClient(server)
        self.db = self.client[params.get('db', 'cache')]
        self.collection = self.db[params.get('collection', 'cache')]

    def add(self, key, value, timeout=None, version=None):
        data = {
            'key': key,
            'value': pickle.dumps(value),
            'timeout': timeout
        }
        self.collection.insert_one(data)

    def get(self, key, default=None, version=None):
        data = self.collection.find_one({'key': key})
        if data and (data['timeout'] is None or data['timeout'] >= time.time()):
            return pickle.loads(data['value'])
        return default

    def set(self, key, value, timeout=None, version=None):
        data = {
            'key': key,
            'value': pickle.dumps(value),
            'timeout': timeout
        }
        self.collection.update_one({'key': key}, {'$set': data}, upsert=True)

    def delete(self, key, version=None):
        self.collection.delete_many({'key': key})

    def clear(self):
        self.collection.delete_many({})

    def close(self, **kwargs):
        self.client.close()