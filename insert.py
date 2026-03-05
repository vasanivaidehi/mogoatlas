from pymongo import MongoClient

client = MongoClient("mongodb+srv://vasanivaidehi42_db_user:pymongo@pymongo.xaivciv.mongodb.net/")

db = client["testdb"]
collection = db["users"]

#data =[ {"name": "Grishma","age": 21,"city": "Rajkot"},
#        {"name": "Palak","age": 20,"city": "Rajkot"},
#        {"name": "Disha","age": 22,"city": "Rajkot"}
#]

#collection.insert_one(data)
#collection.insert_many(data)
prev={"name":"vishva"}
nextt={"$set":{"city":"mumbai"}}
    #collection.update_one(prev,nextt)
up=collection.update_one(prev,nextt)
print(up.modified_count)
print("Data Updated Successfully ")