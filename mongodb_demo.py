import sys
import pymongo
from datetime import datetime
from pymongo import MongoClient
from pymongo import ReturnDocument
import os


class MongoDBTest:
    def __init__(self):

        self.host =some_value = os.environ["MONGODB_URL"]
        self.port = os.environ["MONGODB_PORT"]
        self.database_name = "test"
        self.collection_name = "collection1"
        
        self.client = MongoClient(self.host, self.port)
        self.database = self.client[self.database_name]
        self.collection = self.database[self.collection_name]
        
    def create(self, name):
        data = {"name": name,
            "created_date": datetime.utcnow()}
        print self.collection.insert_one(data)
        
    def read(self, name):
        print self.collection.find_one({"name": name})
        
    def update(self, name, new_name):
        print self.collection.find_one_and_update({"name": name}, {'$set': {'name': new_name}}, return_document=ReturnDocument.AFTER)
        
    def delete(self, name):
        print self.collection.delete_one({"name": name})
        
    def read_all(self):
        for data in self.collection.find():
            print data

    def read_all_user(self, ulist=None):
  

       ulist=""
       for data in self.collection.find():
            ulist = ulist+data['name'] + " "
  
       return ulist

if len(sys.argv) < 2:
    print "Usage: python mongodb_demo.py [create (name)|read (name)|update (name) (new_name)|delete (name)|read_all]"
else:
    mongodb_test = MongoDBTest()
    action = sys.argv[1]
    if action == "create":
        if len(sys.argv) == 3:
            mongodb_test.create(sys.argv[2])
        else:
            print "Usage: python mongodb_demo.py create (name)"
    elif action == "read":
        if len(sys.argv) == 3:
            mongodb_test.read(sys.argv[2])
        else:
            print "Usage: python mongodb_demo.py read (name)"
    elif action == "update":
        if len(sys.argv) == 4:
            mongodb_test.update(sys.argv[2], sys.argv[3])
        else:
            print "Usage: python mongodb_demo.py update (name) (new_name)"
    elif action == "delete":
        if len(sys.argv) == 3:
            mongodb_test.delete(sys.argv[2])
        else:
            print "Usage: python mongodb_demo.py delete (name)"
    elif action == "read_all":
        if len(sys.argv) == 2:
            mongodb_test.read_all()
        else:
            print "Usage: python mongodb_demo.py read_all"
    else:
        print "Usage: python mongodb_demo.py [create (name)|read (name)|update (name) (new_name)|delete (name)|read_all]"