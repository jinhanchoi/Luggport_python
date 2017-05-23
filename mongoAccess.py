import pymongo

class MongoAccessObject():
    def __init__(self,configs):
        self.configs = configs
        self.client = pymongo.MongoClient(configs['host'], 27017)
        if 'name' in configs:
            self.db = self.client[configs['name']]
        
