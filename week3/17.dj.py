from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movie.find_one({'title':'매트릭스'})
target_star = target_movie['star']
print(target_star)

movies = list(db.movie.find({'star':target_star}))
# print(movies)
for movie in movies :
    print(movie['title'])

db.movie.update_one({'star':target_star},{'$set':{'star':'0'}})