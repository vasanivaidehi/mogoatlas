from pymongo import MongoClient

client = MongoClient("mongodb+srv://vasanivaidehi42_db_user:pymongo@pymongo.xaivciv.mongodb.net/")

db = client["testdb"]
collection = db["users"]

data =[ {"name": "Vaidehi","age": 21,"city": "Rajkot"},
        {"name": "Krishna","age": 20,"city": "Rajkot"},
        {"name": "Aarti","age": 22,"city": "Rajkot"}
]

#collection.insert_one(data)
collection.insert_many(data)

print("Multiple Data Inserted Successfully ")