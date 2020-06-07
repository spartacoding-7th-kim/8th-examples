from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbnavermovie

target_movie = db.movie.find_one({'title': '매트릭스'})
target_star = target_movie['star']
# print(target_movie['star'])

movies = list(db.movie.find({'star': target_star}))
print(movies)
for movie in movies:
    print(movie['title'])


db.movie.update_many({'star': target_star}, {'$set': {'star:0'}})
