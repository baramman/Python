person = {'name': '홍길동', 'age': 35, 'address': '서울시'}
person['age'] = 45
del person['address']
person['pay'] = 350

# (1) 요소 검사
print(person['age'])    # 45
print('age' in person)  # True

# (2) 요소 반복
for key in person.keys():   # key 넘김
    print(key)  # key 출력

for v in person.values():   # value 넘김
    print(v)    # value 출력

for i in person.items():    # (key, value) 넘김
    print(i)    # ('name', '홍길동')
