import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
my_db = myclient['mongo_test']

