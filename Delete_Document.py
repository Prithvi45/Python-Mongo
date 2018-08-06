from pymongo import MongoClient
client = MongoClient('localhost',27017)  # 27017 is the default port number for mongodb

# Database =>  Collections => Documents

db = client.Test   #assign database to be used

col = db.students


#Delete 
# delete_one(): deletes one document, returns DeleteResults obj
# delete_many() : deletes multiple documents, returns DeleteResults

# col.delete_one({"name":"aaa"})
# col.delete_many({"name":"aaaa"})  #deletes all documents where name=a