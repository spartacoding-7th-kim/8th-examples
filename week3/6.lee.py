a = 3      # 3을 a에 넣는다
b = a      # a를 b에 넣는다
a = a + 1  # a+1을 다시 a에 넣는다

num1 = a*b  # a*b의 값을 num1이라는 변수에 넣는다
num2 = 99  # 99의 값을 num2이라는 변수에 넣는다

# 변수의 이름은 마음대로 지을 수 있음!
# 진짜 "마음대로" 짓는 게 좋을까? var1, var2 이렇게?
print(num1)
print(num2)


people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

for person in people:
    print(person['name'], person['age'])


dogs = [{'name': 'A', 'age': 2},
        {'name': 'B', 'age': 12},
        {'name': 'C', 'age': 9}]


# for dog in dogs:
#     print(dog['name'], dog['age'])


def get_age(dog_name):
    for dog in dogs:
        if dog['name'] == dog_name:
            return dog['age']
    return '해당하는 이름이 없습니다'


print(get_age('C'))
