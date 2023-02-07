# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("안녕안녕")

a = 3
if a > 1:
    print("a is greater than 1")
elif a < 1:
    print("a is less than 1")

for a in [1, 2, 3]:
    print(a)

i = 0
while i < 3:
    i = i+1
    print(i)

def sum(a, b):
    return a+b

print(sum(3,4))

# hello.py
print("Hello World")

"""
안녕 여긴 주석
"""

a = 3
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b) # ** = 제곱
print(7 % 3)
print(3 % 7)
print(7 // 4) # // = 나눗셈 후 소수점 아랫자리를 버림 (1.75의 소수점 부분인 0.75가 제거되어 결과로 1이 나옴.
print("한글 잘 나오니?")
print("\"Python is very easy.\" he says.")
print('Python\'s favorite food is perl.')
print("Life is too short.\nYou need Python.")
print("""
Life is too short.
You need Python.
""")

a = "python"
print(a*2)

print("="*50)
print("My Program")
print("="*50)

a = "Life is too short, You need Python"
print(a[3])
print(a[4])
print(a[5])
print(a[-1]) # 뒤에서 첫번째 문자를 나타냄.

a = "20230331Rainy"
date = a[:8] # 8 미포함
weather = a[8:] # 8 포함
print(date)
print(weather)
year = a[:4] # 처음부터 3까지
day = a[4:8] # 4부터 7까지
weather = a[8:] #8부터 마지막까지

print("I eat %d apples." %3) # %d = 문자열 포맷 코드
print("I eat %s apples." %"five") # %s = 문자열 바로 대입

number = 3
print("I eat %d apples." %number)

number = 10
day = "three"
print("I ate %d apples, so I was sick for %s days." %(number, day))

a = "Python is best choice"
print(a.find('k'))

print(4 > 10)
print(not True)

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 "+animal+"의 이름은 "+name+"입니다.")
hobby = "공놀이"
print(name+"는 "+str(age)+"살이며, "+hobby+"를 아주 좋아해요.")
print(name, "는 어른일까요? ", is_adult)

# QUIZ) 변수를 이용하여 다음 문장을 출력하시오.
# 변수명 : station
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력문장 : XX행 열차가 들어오고 있습니다.

station = "사당"
print(station+"행 열차가 들어오고 있습니다.")

print(1 != 3)
print(not(1 != 3))
print((3 > 0) & (3 < 5))
print((3 > 0) | (3 < 5))

print(abs(-5)) # -5의 절대값 = 5
print(pow(4, 2)) # 4^2 = 16
print(max(5, 12)) # 최대값 = 12
print(min(5, 12)) # 최소값 = 5
print(round(3.14)) # 반올림 = 3
print(round(4.99)) # 반올림 = 5

from math import *
print(floor(4.99)) # 내림 = 4
print(ceil(3.14)) # 올림 = 4
print(sqrt(16)) # 제곱근 = 4

from random import *
print(random()) # 0.0 ~ 1.0 사이의 임의값 생성
print(randint(1, 10)) # 1 ~ 10 사이의 임의값 생성
print(random() < 0.5) # 0.0 ~ 0.5 사이의 임의값 생성
print(random() > 0.5) # 0.5 ~ 1.0 사이의 임의값 생성
print(random() <= 0.5) # 0.0 ~ 0.5 사이의 임의값 생성
print(random() >= 0.5) # 0.5 ~ 1.0 사이의 임의값 생성
print(random()!= 0.5) # 0.5 ~ 1.0 사이의 임의값 생성
print(random() == 0.5) # 0.5 ~ 1.0 사이의 임의값 생성
print(random()!= 0.5) # 0.5 ~ 1.0 사이의 임의값 생성
print(random() == 0.5) # 0.5 ~ 1.0 사이의 임의값 생성
print(random() * 10) # 0.0 ~ 10.0 사이의 임의값 생성
print(int(random() * 10 + 1)) # 1 ~ 10 사이의 임의값 생성
print(randrange(1,46)) # 1~46 미만의 임의값 생성

# QUIZ) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건 1 : 랜덤으로 날짜를 뽑아야 함
# 조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

from random import *
date = randint(4, 28) # 4~28 사이의 임의값 생성 (4와 28 포함)
print("오프라인 스터디 모임 날짜는 매월 "+str(date)+"일로 선정되었습니다.")