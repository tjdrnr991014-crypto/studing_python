SUBJECT = ("국어", "영어", "수학")
names = ["김민준", "이서연", "박도윤"]
scores = ["88", "95", "76"]

print(SUBJECT)
print("등록된 학생: "f'{len(names)}'"명")
print("첫 번째 학생:"f'{names[0]}'"/"f'{scores[0]}'"점")
print("마지막 학생: " f'{names[-1]}'"/"f'{scores[-1]}'"점")