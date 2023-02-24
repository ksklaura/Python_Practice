# score_file = open("score.txt", "w", encoding="UTF8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="UTF8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="UTF8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="UTF8")
# print(score_file.readline()) # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 한 줄 띄기를 하고 싶지 않을 경우, end="" 를 붙여줌.
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="UTF8")
# while True: # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동 but 몇 줄인지는 모를 때 while문을 돌리는 방법 사용
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r", encoding="UTF8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

print("")

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

profile_file = open("profile.pickle", "wb")
profile = {"이름":"김수경", "나이":29, "취미":["테니스", "요가", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

with open("study.txt", "w", encoding="UTF8") as study_file:
    study_file.write("수경이 열공해여")

with open("study.txt", "r", encoding="UTF8") as study_file:
    print(study_file.read())

# QUIZ) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
# - X 주차 주간 보고 -
# 부서 :
# 이름 :
# 업무 요약 :
# 1주차부터 5주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건 : 파일명은 "1주차.txt", "2주차.txt", ... 와 같이 만드시오.

for i in range(1, 6):
    with open(str(i) + "주차.txt", "w", encoding="UTF8") as report_file:
        report_file.write("- {0} 주차 주간 보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")
