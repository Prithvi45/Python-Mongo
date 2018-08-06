from pymongo import MongoClient
client = MongoClient('localhost',27017)  # 27017 is the default port number for mongodb

# Database =>  Collections => Documents

db = client.Test   #assign database to be used

col = db.students


# Create Operations
#insert_one() : to insert single document

#insert_many() : to insert multiple document

#insert() : to insert single or array or documents


# col.insert_one({"name":"test","age":"25"})


# col.insert_many(
#    [
#      { "name": "a", "age": "100"},
#      { "name": "b", "age": "100"},
#      { "name": "c", "age": "100"}
#    ]
# )



# single document
# col.insert({ "name": "Jeorge", "age": 10})

# array of documents
# col.insert([{ "name": "Jeorge", "age": 10}, { "name": "Steve", "age": 10}])



# Read/Retrive
# find() : find() function will return with all the documents in that collection
# find_one() : find_one() returns the first document in the collection

# print(col.find_one())  #returns first document from collection
# print(col.find_one({"name":"Prithvi"}))
# print(col.find({"name":"Prithvi"})) #returns cursor


#Update:
# update() : returns dict
# update_one() : returns Update Result Objects
# update_many() : returns Update Result Objects
# replace_one() : returns Update Result Objects


# col.update_one({"name":"a"}, {"$set":{"name":"aa","age":"10"} })

# col.update_many({"name":"aa"}, {"$set":{"name":"Joseph"}})  #for all name=aa it will replace by name=joseph

# print(col.update({"name":"aa"},{"$set":{"name":"aaa"}}))

# print(col.replace_one({"name":"aaa"}, {"name":"a"}))



#Delete 
# delete_one(): deletes one document, returns DeleteResults obj
# delete_many() : deletes multiple documents, returns DeleteResults
# col.delete_one({"name":"a"})
# col.delete_many({"name":"a"})  #deletes all documents where name=a