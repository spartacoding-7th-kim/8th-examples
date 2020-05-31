from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbnavermovie


target_movie = db.users.find_one({'title':'매트릭스'})
print (target_movie['star'])