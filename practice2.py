# 조건문 if

temp = int(input("기온은 어때요?"))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요 네버.")
elif 10 <= temp and temp < 30:
    print("상쾌해요.")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요 네버.")

# 반복문 for

starbucks = ["수경", "김수경", "김수"]
for customer in starbucks:
    print("{0} 고객님, 커피가 준비되었습니다.".format(customer))

# 반복문 while

customer = "수경"
index = 5
while index >= 1:
    print("{0} 고객님, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("죄송하지만 커피는 폐기처분이 되었습니다.")

customer = "수경"
person = "Unknown"

while person != customer:
    print("{0} 고객님, 커피가 준비 되었습니다.".format(customer))
    person = input("성함이 어떻게 되세요?")

# continue 와 break

absent = [2, 5] #결석
no_book = [7] #책을 가져오지 않음

for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지. {0}번 학생은 교무실로 따라오세요.".format(student))
        break
    print("{0}번 학생, 책 읽어보세요.".format(student))

# 한 줄 for문

students = ["hi", "hiiiii", "hello", "helllllooooo"]
students = [len(i) for i in students]
print(students)

# QUIZ) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 떄, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2명

from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1 ~ 50 사이의 수 (승객)
    time = randrange(5, 51) # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15: # 5분 ~ 15분 이내로 소요되는 손님, 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}명".format(cnt))