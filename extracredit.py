import pymongo

connection = pymongo.MongoClient("class-mongodb.cims.nyu.edu", 27017,
                                username="kw2963",
                                password="DvUUhw9D",
                                authSource="kw2963")

collection = connection["kw2963"]["listings"]

#show exactly two documents from the `listings` collection in any order
rows = collection.find({}).limit(2)
for row in rows:
    print(row)
    
