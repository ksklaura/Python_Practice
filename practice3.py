# 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money: #잔액이 출금보다 많을 경우
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #밤에 출금
    commission = 100 #수수료 100원
    return commission, balance - money - commission

balance = 0 #잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

# 지역변수와 전역변수

# QUIZ) 표준 체중을 구하는 프로그램을 작성하시오
# * 표준 체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명: std_weight
#         * 전달값: 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째 자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.


def std_weight(height, gender): # 키는 m단위 (실수)
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height/100, gender), 2)
print("키 {0}cm {1}의 표중 체중은 {2}kg 입니다.".format(height, gender, weight))

# 표준 입출력

print("Python", "Java", "JavaScript", sep=" vs ")
print("Python", "Java", "JavaScript", sep=", ", end="?")
print("")

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust = 왼쪽 정렬, rjust = 오른쪽 정렬

for num in range(1, 21):
    print("대기번호 : "+str(num).zfill(3)) # zfill = 빈칸을 0으로 채움

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")

answer1 = 10
print(type(answer1))

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))

# 양수일 때는 +로 표시, 음수일 때는 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))

# 3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000000))

# 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:-,}".format(-100000000000))

# 3자리마다 콤마를 찍어주기, +- 부호도 붙이기, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
print("{0:^<+30,}".format(100000000000))

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))