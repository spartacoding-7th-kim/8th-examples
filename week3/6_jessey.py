people = [{'name':'kevin', 'age': 38, 'height': 185},
          {'name':'bob', 'age': 29, 'height': 174}, 
          {'name':'john', 'age': 21, 'height': 184}]

for person in people:
    print(person['name'], person['age'])

def getAge(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return '해당하는 사람이 없습니다.'


print(getAge('bob'))
print(getAge('tom'))