from pymongo import MongoClient
client = MongoClient('localhost',27017)  # 27017 is the default port number for mongodb

# Database =>  Collections => Documents

db = client.Test   #assign database to be used

col = db.students


# Read/Retrive
# find() : find() function will return with all the documents in that collection
# find_one() : find_one() returns the first document in the collection

# print(col.find_one())  #returns first document from collection
# print(col.find_one({"name":"Prithvi"}))
# print(col.find_one({"age":"25"}))
# print(col.find({"name":"Prithvi"})) #returns cursor
# print(col.find({"age":"25"}))