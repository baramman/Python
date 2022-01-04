"""
날짜 : 2022/01/03
이름 : 양성민
내용 : 파이썬 3장 연습문제 p77
"""

# [문제1]
weight = int(input('짐의 무게는 얼마입니까? '))

# A형
"""
if weight >= 10:
    print('수수료는 10,000원 입니다.')
else:
    print('수수료는 없습니다.')
    pass
"""

# B형
if weight >= 10:
    pay = weight // 10
    print('수수료는 ', pay,',000원입니다.')
else:
    print('수수료는 없습니다.')
    pass


# [문제2] while 반복문을 이용한 '숫자 맞추기 게임'
"""
import random

print('>>숫자 맞추기 게임<< ')
com = random.randint(1, 10) # 1~10 사이 난수 정수 발생

while True:
    my = int(input('예상 숫자를 입력하시오 : '))  # 숫자 입력

    if com == my:
        print('~~ 성공 ~~')
        break

    if com < my:
        print('더 작은 수 입력')
        continue
    if com > my:
        print('더 큰 수 입력')
        continue
"""

# [문제3]


# [문제4]
