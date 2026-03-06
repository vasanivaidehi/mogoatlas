from pymongo import MongoClient

client = MongoClient("mongodb+srv://vasanivaidehi42_db_user:pymongo@pymongo.xaivciv.mongodb.net/")

db = client["testdb"]
collection = db["admin"]

data =[ {"name": "Aarti","city": "Rajkot","email":"G@gmail.com"},
        {"name": "Banshi","city": "Rajkot","email":"P@gmail.com"},
        {"name": "Mansi","city": "Rajkot","email":"D@gmail.com"}
]

#collection.insert_one(data)
collection.insert_many(data)
#prev={"name":"Aarti"}
#nextt={"$set":{"city":"surat"}}
    #collection.update_one(prev,nextt)
#up=collection.update_one(prev,nextt)
#print(up.modified_count)
#print("Data Updated Successfully ")
print("Multiple Data inserted Successfully ")
