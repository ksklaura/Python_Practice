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