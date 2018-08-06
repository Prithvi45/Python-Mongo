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
# find()
# find_one()
