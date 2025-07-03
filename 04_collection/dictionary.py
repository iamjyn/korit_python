#딕셔너리

profile = {
    "이름": "정유나",
    "나이": 29,
    "취미": ["음악", "영화"],
    2 : "문자" #키,값은 문자도 되고, 숫자도 됨
}

#딕셔너리 - 요소 접근
print(profile["이름"])
print(profile["취미"][1])

#딕셔너리 - 요소 수정
profile["나이"] = 30
print(profile)

#딕셔너리 - 요소 추가
profile["직업"] = "회사" # => 키가 있으면 수정, 키가 없으면 추가됨
print(profile)

#딕셔너리 - 요소 삭제
del profile["직업"]
print(profile)
# profile.clear() #전체 삭제

#딕셔너리 - 키만 불러오기
print(profile.keys())

#딕셔너리 - 값만 불러오기
print(profile.values())

#딕셔너리 - 키, 값 둘다 불러오기
print(profile.items())

python_grade = {
    "kelly": "B",
    "json": "A",
    "ian": "C",
    "elly": "D"
}

print(sorted(python_grade.items())) #키 기준으로 오름차순 정렬
print(sorted(python_grade.items(), reverse=True)) #키 기준 내림차순 정렬

#값 기준 정렬 (일단 참고만 하고 있음 / 어려워서 나중에 배우기로함)
print(sorted(python_grade.items(), key=lambda x: x[1]))
print(sorted(python_grade.items(), key=lambda x: x[1], reverse=True))

student = {}
#이름을 입력 받고 해당 이름을 키로, 점수를 입력 받고 값으로 추가

# student = {"정유나" : 80}

name = input("이름 : ")
score = input(f"{name}의 점수 : ")
student[name] = score
# student = {input("이름:") : input("점수:")}
print(student)
