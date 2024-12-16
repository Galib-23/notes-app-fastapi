from pymongo import MongoClient
MONGO_URI = "mongodb://localhost:27017/fastapiTest"

conn = MongoClient(MONGO_URI)