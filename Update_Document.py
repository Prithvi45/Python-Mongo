from pymongo import MongoClient
client = MongoClient('localhost',27017)  # 27017 is the default port number for mongodb

# Database =>  Collections => Documents

db = client.Test   #assign database to be used

col = db.students


#Update:
# update() : returns dict
# update_one() : returns Update Result Objects
# update_many() : returns Update Result Objects
# replace_one() : returns Update Result Objects


# col.update_one({"name":"a"}, {"$set":{"name":"aa","age":"12"} })

# col.update_many({"name":"aa"}, {"$set":{"name":"aaa"}})  #for all name=aa it will replace by name=joseph

# print(col.update({"name":"aaaa"},{"$set":{"name":"aaa"}}))

# print(col.replace_one({"name":"aaa"}, {"name":"a"}))