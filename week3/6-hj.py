people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

for i in people:
    print(i['name'], i['age'])

def yourage(yourname):
    for i in people:
        if i['name'] == yourname:
            return i['age']
    return '해당하는 사람이 없습니다.'


print(yourage('john'))
print(yourage('zoe'))