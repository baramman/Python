x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y
x.extend(y)
x.append(y)
lst = [1, 2, 3, 4]
result = lst * 2


# (1) 리스트 정렬
print(result)   # [1, 2, 3, 4, 1, 2, 3, 4]
result.sort()   # 오름차운 정렬
print(result)   # [1, 1, 2, 2, 3, 3, 4, 4]
result.sort(reverse=True)   # 내림차순 정렬
print(result)   # [4, 4, 3, 3, 2, 2, 1, 1]

# (2) 리스트 요소 검사
import random
r = []
for i in range(5):
    r.append(random.randint(1, 5))

print(r)
if 4 in r:
    print('있음')
else:
    print('없음')
