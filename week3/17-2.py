from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

target_movie = db.movies.find_one({'title': '매트릭스'})
target_star = target_movie['star']

movies = list(db.movie.find({'star': target_star}))

for movie in movies:
    print(movie['title'])
